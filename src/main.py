from dataclasses import dataclass
from typing import Optional
from uuid import uuid4
from abc import ABC, abstractmethod
import re


class DomainException(Exception):
    """Base class for all domain-level exceptions."""
    pass


class EmailAlreadyExistsError(DomainException):
    pass


class ValidationError(DomainException):
    pass


class Email:
    """Value object representing an email address."""
    
    def __init__(self, value: str):
        if not self._is_valid_email(value):
            raise ValidationError(f"Invalid email format: {value}")
        self.value = value.lower()  # Normalize to lowercase
    
    def _is_valid_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)


class PasswordHash:
    """Value object representing a hashed password."""
    
    def __init__(self, value: str):
        if not value or len(value) < 8:
            raise ValidationError("Password must be at least 8 characters")
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, PasswordHash):
            return False
        return self.value == other.value


@dataclass
class RegistrationForm:
    """Form data for tenant registration."""
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None


class TenantAccount:
    """Entity representing a tenant account."""
    
    def __init__(
        self, 
        email: Email, 
        password_hash: PasswordHash,
        first_name: str,
        last_name: str,
        phone: str,
        tenant_id: Optional[str] = None
    ):
        self.id = tenant_id or str(uuid4())
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.is_verified = False


class AbstractUserRepository(ABC):
    """Repository for user operations."""
    
    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[TenantAccount]:
        pass
    
    @abstractmethod
    async def save(self, user: TenantAccount) -> TenantAccount:
        pass


class AbstractEmailService(ABC):
    """Service for sending emails."""
    
    @abstractmethod
    async def send_verification_email(self, email: str, tenant_id: str) -> None:
        pass


class TenantRegistrationService:
    """Service for registering new tenants."""
    
    def __init__(
        self, 
        user_repository: AbstractUserRepository,
        email_service: AbstractEmailService
    ):
        self.user_repository = user_repository
        self.email_service = email_service
    
    async def register_tenant(self, form: RegistrationForm) -> TenantAccount:
        """Register a new tenant with validation and email verification."""
        # Validate required fields
        self._validate_required_fields(form)
        
        # Check for duplicate email
        existing_user = await self.user_repository.find_by_email(form.email)
        if existing_user:
            raise EmailAlreadyExistsError(
                f"Email {form.email} already exists in the system"
            )
        
        # Create value objects
        email = Email(form.email)
        password_hash = PasswordHash(form.password)
        
        # Create tenant account
        tenant = TenantAccount(
            email=email,
            password_hash=password_hash,
            first_name=form.first_name,
            last_name=form.last_name,
            phone=form.phone
        )
        
        # Save to repository
        await self.user_repository.save(tenant)
        
        # Send verification email
        await self.email_service.send_verification_email(
            email=form.email,
            tenant_id=tenant.id
        )
        
        return tenant
    
    def _validate_required_fields(self, form: RegistrationForm) -> None:
        """Validate that all required fields are present."""
        missing_fields = []
        
        if not form.first_name:
            missing_fields.append("first_name")
        
        if not form.last_name:
            missing_fields.append("last_name")
        
        if not form.phone:
            missing_fields.append("phone")
        
        if missing_fields:
            raise ValidationError(
                f"Missing required fields: {', '.join(missing_fields)}"
            )