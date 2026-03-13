### Bounded Context: User Management
#### Aggregates:
- **UserAccount** (Aggregate Root)
  - Entities: TenantAccount, PropertyOwnerAccount
  - Value Objects: Email, PasswordHash, UserId, VerificationStatus, RegistrationDate
#### Domain Events:
- UserRegistered
- UserVerified
- EmailVerified
- UserAccountUpdated
#### Commands:
- RegisterUser
- VerifyEmail
- UpdateUserAccount
- VerifyUser

### Bounded Context: Tenant Profiling
#### Aggregates:
- **TenantProfile** (Aggregate Root)
  - Entities: PersonalInfo, RentalHistory, EmploymentInfo, References
  - Value Objects: TenantPreferences, TenantScore, CompletionStatus
- **VerificationDocument** (Aggregate Root)
  - Entities: DocumentFile, VerificationResult
  - Value Objects: DocumentType, DocumentStatus, VerificationDate
#### Domain Events:
- TenantProfileCreated
- TenantProfileCompleted
- TenantProfileVerified
- VerificationDocumentSubmitted
- VerificationDocumentApproved
- VerificationDocumentRejected
#### Commands:
- CreateTenantProfile
- UpdateTenantProfile
- SubmitVerificationDocument
- VerifyTenantProfile

### Bounded Context: Listing Management
#### Aggregates:
- **TenantListing** (Aggregate Root)
  - Entities: ListingVisibility, ListingStatistics
  - Value Objects: ListingDuration, ListingStatus, CreationDate, ExpirationDate, ListingFee
#### Domain Events:
- ListingCreated
- ListingActivated
- ListingExpired
- ListingRenewed
- ListingViewed
#### Commands:
- CreateListing
- ActivateListing
- RenewListing
- DeactivateListing

### Bounded Context: Matching System
#### Aggregates:
- **MatchingCriteria** (Aggregate Root)
  - Entities: Filter, Preference
  - Value Objects: MatchScore, SearchRadius, BudgetRange, MoveInDate
- **MatchResult** (Aggregate Root)
  - Entities: TenantProfileMatch
  - Value Objects: MatchScore, MatchReasons, CompatibilityFactors
#### Domain Events:
- MatchingCriteriaUpdated
- MatchCalculated
- MatchResultsGenerated
- NoMatchesFound
#### Commands:
- UpdateMatchingCriteria
- CalculateMatches
- FilterResults
- SearchTenantProfiles

### Bounded Context: Property Context
#### Aggregates:
- **Property** (Aggregate Root)
  - Entities: PropertyFeatures, PropertyAmenities
  - Value Objects: PropertyId, Location, PropertyType, RentalPrice
- **PropertyRequirements** (Aggregate Root)
  - Entities: TenantRequirement, Preference
  - Value Objects: MinCreditScore, MaxOccupants, PetPolicy, SmokingPolicy
#### Domain Events:
- PropertyRegistered
- PropertyDetailsUpdated
- PropertyRequirementsUpdated
- LocationValidated
- LocationInvalid
#### Commands:
- RegisterProperty
- UpdatePropertyDetails
- UpdatePropertyRequirements
- ValidateLocation

### Bounded Context: Billing Context
#### Aggregates:
- **Subscription** (Aggregate Root)
  - Entities: SubscriptionPlan, PaymentHistory
  - Value Objects: SubscriptionId, PlanType, RenewalDate, PaymentStatus
- **CreditBalance** (Aggregate Root)
  - Entities: CreditTransaction
  - Value Objects: CreditAmount, TransactionDate, TransactionType
#### Domain Events:
- SubscriptionPurchased
- SubscriptionActivated
- SubscriptionExpired
- CreditsPurchased
- CreditsConsumed
- CreditsExpired
#### Commands:
- PurchaseSubscription
- ActivateSubscription
- CancelSubscription
- PurchaseCredits
- ConsumeCredits

### Bounded Context: Communications Context
#### Aggregates:
- **ContactRequest** (Aggregate Root)
  - Entities: MessageThread
  - Value Objects: RequestStatus, ContactDate, ContactReason
- **Message** (Aggregate Root)
  - Entities: MessageContent, Attachment
  - Value Objects: MessageId, Timestamp, MessageStatus
#### Domain Events:
- ContactRequestInitiated
- ContactRequestAccepted
- ContactRequestRejected
- MessageSent
- MessageRead
#### Commands:
- InitiateContact
- AcceptContact
- RejectContact
- SendMessage
- MarkMessageRead

```mermaid
graph TD
    subgraph Bounded Contexts
        UM[User Management Context]
        TP[Tenant Profiling Context]
        LM[Listing Management Context]
        MS[Matching System Context]
        PC[Property Context]
        BC[Billing Context]
        CC[Communications Context]
    end
    
    subgraph "User Management Aggregates"
        UA[UserAccount]
    end
    
    subgraph "Tenant Profiling Aggregates"
        TProf[TenantProfile]
        VDoc[VerificationDocument]
    end
    
    subgraph "Listing Management Aggregates"
        TL[TenantListing]
    end
    
    subgraph "Matching System Aggregates"
        MC[MatchingCriteria]
        MR[MatchResult]
    end
    
    subgraph "Property Context Aggregates"
        P[Property]
        PR[PropertyRequirements]
    end
    
    subgraph "Billing Context Aggregates"
        SUB[Subscription]
        CB[CreditBalance]
    end
    
    subgraph "Communications Context Aggregates"
        CR[ContactRequest]
        M[Message]
    end
    
    %% Relationships between contexts
    UA -->|creates| TProf
    TProf -->|enables| TL
    TL -->|feeds into| MS
    P -->|defines requirements for| MS
    PR -->|defines criteria for| MS
    MS -->|requires| BC
    MS -->|initiates| CC
    BC -->|enables| MS
    BC -->|enables| CC
    
    %% Integration Patterns
    UM -.>|Shared Kernel| TP
    TP -.>|Domain Events| LM
    TP -.>|Open Host Service| MS
    PC -.>|Open Host Service| MS
    MS -.>|Domain Events| BC
    BC -.>|Anti-Corruption Layer| All Contexts
    CC -.>|Domain Events| All Contexts
```