{
  "bounded_contexts": [
    {
      "name": "User Management",
      "features": [
        {
          "name": "User Registration",
          "scenarios": [
            {
              "title": "Successful tenant registration",
              "given": "a new tenant with valid information",
              "when": "the tenant submits registration details",
              "then": "the system creates a tenant account"
            },
            {
              "title": "Successful property owner registration",
              "given": "a new property owner with valid information",
              "when": "the property owner submits registration details",
              "then": "the system creates a property owner account"
            },
            {
              "title": "Registration with duplicate email",
              "given": "a user registers with an existing email",
              "when": "the user submits registration details",
              "then": "the system shows email already in use error"
            },
            {
              "title": "Registration with invalid email format",
              "given": "a user registers with invalid email format",
              "when": "the user submits registration details",
              "then": "the system shows invalid email format error"
            },
            {
              "title": "Registration with weak password",
              "given": "a user registers with password not meeting security requirements",
              "when": "the user submits registration details",
              "then": "the system shows password security requirements error"
            }
          ]
        },
        {
          "name": "User Authentication",
          "scenarios": [
            {
              "title": "Successful user login",
              "given": "a registered user with valid credentials",
              "when": "the user submits login credentials",
              "then": "the system authenticates the user and redirects to dashboard"
            },
            {
              "title": "Login with incorrect password",
              "given": "a registered user with incorrect password",
              "when": "the user submits login credentials",
              "then": "the system shows invalid credentials error"
            },
            {
              "title": "Login with non-existent account",
              "given": "a user with non-existent account",
              "when": "the user submits login credentials",
              "then": "the system shows account not found error"
            },
            {
              "title": "Password reset request",
              "given": "a user who has forgotten their password",
              "when": "the user requests password reset",
              "then": "the system sends password reset link to registered email"
            },
            {
              "title": "Account deletion",
              "given": "a user who wants to delete their account",
              "when": "the user requests account deletion",
              "then": "the system removes the user account after confirmation"
            }
          ]
        }
      ]
    },
    {
      "name": "Tenant Profile Context",
      "features": [
        {
          "name": "Profile Management",
          "scenarios": [
            {
              "title": "Create tenant profile",
              "given": "a registered tenant without a profile",
              "when": "the tenant submits profile details",
              "then": "the system creates a tenant profile"
            },
            {
              "title": "Update tenant profile",
              "given": "a tenant with an existing profile",
              "when": "the tenant updates profile information",
              "then": "the system saves the updated profile information"
            },
            {
              "title": "Create profile with missing required fields",
              "given": "a tenant submitting incomplete profile information",
              "when": "the tenant submits profile details",
              "then": "the system shows missing required fields error"
            },
            {
              "title": "Profile with inappropriate content",
              "given": "a tenant submits profile with inappropriate content",
              "when": "the system processes the profile",
              "then": "the system rejects the profile and shows content policy violation"
            },
            {
              "title": "Exceed profile field character limits",
              "given": "a tenant submits profile information exceeding character limits",
              "when": "the tenant submits profile details",
              "then": "the system shows character limit exceeded error"
            }
          ]
        },
        {
          "name": "Profile Verification",
          "scenarios": [
            {
              "title": "Request identity verification",
              "given": "a tenant with a complete profile",
              "when": "the tenant requests identity verification",
              "then": "the system initiates verification process"
            },
            {
              "title": "Submit verification documents",
              "given": "a tenant in the verification process",
              "when": "the tenant submits verification documents",
              "then": "the system processes the documents for verification"
            },
            {
              "title": "Submit invalid verification documents",
              "given": "a tenant submits invalid verification documents",
              "when": "the system processes the documents",
              "then": "the system rejects the documents and requests valid ones"
            },
            {
              "title": "Verification approval",
              "given": "a tenant with valid verification documents",
              "when": "the verification is approved",
              "then": "the system adds verification badge to the profile"
            },
            {
              "title": "Verification rejection",
              "given": "a tenant with invalid verification documents",
              "when": "the verification is rejected",
              "then": "the system notifies the tenant of rejection with reasons"
            }
          ]
        },
        {
          "name": "Profile Visibility",
          "scenarios": [
            {
              "title": "Set profile visibility preferences",
              "given": "a tenant with an existing profile",
              "when": "the tenant sets visibility preferences",
              "then": "the system saves the visibility preferences"
            },
            {
              "title": "Upgrade to featured profile",
              "given": "a tenant with a standard profile",
              "when": "the tenant purchases featured profile upgrade",
              "then": "the system applies featured profile status after payment"
            },
            {
              "title": "Featured profile without payment",
              "given": "a tenant attempting to upgrade to featured without payment",
              "when": "the tenant submits upgrade request",
              "then": "the system shows payment required error"
            },
            {
              "title": "Property owner views tenant profiles",
              "given": "a property owner with valid subscription",
              "when": "the property owner searches for tenant profiles",
              "then": "the system displays tenant profiles matching search criteria"
            },
            {
              "title": "View profiles without subscription",
              "given": "a property owner without valid subscription",
              "when": "the property owner attempts to view tenant profiles",
              "then": "the system shows subscription required error"
            }
          ]
        }
      ]
    },
    {
      "name": "Matching Context",
      "features": [
        {
          "name": "AI Matching Algorithm",
          "scenarios": [
            {
              "title": "Generate compatibility matches",
              "given": "property owners and tenants with compatible preferences",
              "when": "the matching algorithm runs",
              "then": "the system generates compatibility matches between property owners and tenants"
            },
            {
              "title": "Display match scores",
              "given": "compatibility matches have been generated",
              "when": "a property owner views potential tenant matches",
              "then": "the system displays match scores for each potential tenant"
            },
            {
              "title": "No matches due to insufficient criteria",
              "given": "property owner with overly restrictive criteria",
              "when": "the matching algorithm runs",
              "then": "the system shows no matches found message"
            },
            {
              "title": "Inaccurate match scoring",
              "given": "matching algorithm produces inconsistent scores",
              "when": "the system detects scoring anomalies",
              "then": "the system recalculates scores and alerts administrators"
            },
            {
              "title": "Matches become unavailable",
              "given": "saved tenant matches with expired listings",
              "when": "a property owner views saved matches",
              "then": "the system indicates which matches are no longer available"
            }
          ]
        },
        {
          "name": "Search and Filter",
          "scenarios": [
            {
              "title": "Property owner searches tenants",
              "given": "a property owner with valid subscription",
              "when": "the property owner applies search criteria",
              "then": "the system returns tenant profiles matching the criteria"
            },
            {
              "title": "Search with restrictive criteria",
              "given": "a property owner applying overly restrictive search criteria",
              "when": "the property owner submits search",
              "then": "the system shows no results message with suggestions to broaden search"
            },
            {
              "title": "Save search criteria",
              "given": "a property owner with frequently used search criteria",
              "when": "the property owner saves search criteria",
              "then": "the system saves the criteria for future use"
            },
            {
              "title": "Filter by verification status",
              "given": "a property owner who wants only verified tenants",
              "when": "the property owner applies verification filter",
              "then": "the system shows only tenant profiles with verification status"
            },
            {
              "title": "Invalid search parameters",
              "given": "a property owner submits invalid search parameters",
              "when": "the system processes the search",
              "then": "the system shows invalid parameters error with correction suggestions"
            }
          ]
        }
      ]
    },
    {
      "name": "Privacy Context",
      "features": [
        {
          "name": "Property Owner Privacy",
          "scenarios": [
            {
              "title": "Anonymous browsing of tenant profiles",
              "given": "a property owner browsing tenant profiles",
              "when": "the property owner views a tenant profile",
              "then": "the system does not reveal the property owner's identity to the tenant"
            },
            {
              "title": "Property details remain hidden",
              "given": "a tenant viewing the platform",
              "when": "the tenant searches for properties",
              "then": "the system does not display property details as properties are not listed"
            },
            {
              "title": "Control contact information sharing",
              "given": "a property owner interested in a tenant",
              "when": "the property owner decides to share contact information",
              "then": "the system shares contact information only after mutual interest is established"
            },
            {
              "title": "Unauthorized access attempt",
              "given": "a malicious user attempting to access private property information",
              "when": "the unauthorized access attempt is detected",
              "then": "the system blocks the attempt and logs the security event"
            },
            {
              "title": "Privacy settings application",
              "given": "a property owner with configured privacy settings",
              "when": "the property owner's profile is accessed",
              "then": "the system applies all configured privacy settings correctly"
            }
          ]
        }
      ]
    },
    {
      "name": "Listing Context",
      "features": [
        {
          "name": "Listing Management",
          "scenarios": [
            {
              "title": "Create listing with duration",
              "given": "a tenant creating a listing",
              "when": "the tenant selects listing duration (30/60/90 days)",
              "then": "the system creates the listing with the specified duration"
            },
            {
              "title": "Listing expiration",
              "given": "a listing with approaching expiration date",
              "when": "the expiration date is reached",
              "then": "the system marks the listing as expired"
            },
            {
              "title": "Expiration notification",
              "given": "a listing nearing expiration",
              "when": "the notification threshold is reached",
              "then": "the system sends expiration alert to the tenant"
            },
            {
              "title": "Listing renewal",
              "given": "a tenant with expiring listing",
              "when": "the tenant requests renewal before expiration",
              "then": "the system extends the listing duration after payment"
            },
            {
              "title": "Attempt to create listing beyond maximum duration",
              "given": "a tenant attempting to create listing exceeding 90 days",
              "when": "the tenant submits the listing",
              "then": "the system shows maximum duration exceeded error"
            },
            {
              "title": "Expired listing removal",
              "given": "listings that have expired",
              "when": "the system processes expired listings",
              "then": "the system removes expired listings from search results"
            },
            {
              "title": "Renewal payment failure",
              "given": "a tenant with payment processing failure",
              "when": "the renewal payment fails",
              "then": "the system shows payment failure error and provides retry options"
            },
            {
              "title": "Attempt to renew expired listing",
              "given": "a tenant attempting to renew an already expired listing",
              "when": "the tenant submits renewal request",
              "then": "the system shows listing expired error and requires new listing creation"
            }
          ]
        }
      ]
    },
    {
      "name": "Communication Context",
      "features": [
        {
          "name": "Secure Messaging",
          "scenarios": [
            {
              "title": "Send contact request",
              "given": "a property owner interested in a tenant",
              "when": "the property owner sends a contact request",
              "then": "the system delivers the contact request to the tenant"
            },
            {
              "title": "Accept contact request",
              "given": "a tenant with received contact request",
              "when": "the tenant accepts the contact request",
              "then": "the system enables messaging between the tenant and property owner"
            },
            {
              "title": "Decline contact request",
              "given": "a tenant with received contact request",
              "when": "the tenant declines the contact request",
              "then": "the system notifies the property owner of the decline"
            },
            {
              "title": "Exchange secure messages",
              "given": "a tenant and property owner with established contact",
              "when": "either party sends a message",
              "then": "the system delivers the message securely to the recipient"
            },
            {
              "title": "Inappropriate message report",
              "given": "a user receives inappropriate message",
              "when": "the user reports the message",
              "then": "the system flags the message for moderation and temporarily restricts the sender"
            },
            {
              "title": "Communication before mutual interest",
              "given": "a user attempting to contact another without mutual interest",
              "when": "the user sends a message",
              "then": "the system blocks the message and shows mutual interest required error"
            },
            {
              "title": "Message history access",
              "given": "users with established communication",
              "when": "either party accesses message history",
              "then": "the system displays the complete message history between the parties"
            },
            {
              "title": "Message with contact information sharing",
              "given": "a user attempting to share external contact information",
              "when": "the system detects contact information in message",
              "then": "the system flags the message with privacy warning"
            }
          ]
        }
      ]
    },
    {
      "name": "Monetization Context",
      "features": [
        {
          "name": "Subscription Management",
          "scenarios": [
            {
              "title": "Property owner purchases subscription",
              "given": "a property owner without active subscription",
              "when": "the property owner purchases 30-day access",
              "then": "the system grants 30-day access to tenant profiles after payment"
            },
            {
              "title": "Tenant pays for subsequent listing",
              "given": "a tenant creating listing after first free listing",
              "when": "the tenant completes payment",
              "then": "the system creates the paid listing for the specified duration"
            },
            {
              "title": "First listing free",
              "given": "a new tenant creating first listing",
              "when": "the tenant submits the listing",
              "then": "the system creates the listing without payment requirement"
            },
            {
              "title": "Payment processing failure",
              "given": "a user with payment processing failure",
              "when": "the payment fails to process",
              "then": "the system shows payment failure error with retry options"
            },
            {
              "title": "Access premium features without payment",
              "given": "a user attempting to access premium features without payment",
              "when": "the user attempts to access the feature",
              "then": "the system shows payment required error"
            },
            {
              "title": "Subscription renewal failure",
              "given": "a property owner with expired payment method",
              "when": "the system attempts to renew subscription",
              "then": "the system shows renewal failure error and requests updated payment information"
            },
            {
              "title": "Refund request",
              "given": "a user requesting refund for unsatisfactory service",
              "when": "the user submits refund request",
              "then": "the system initiates refund process according to refund policy"
            },
            {
              "title": "Upgrade to premium verification",
              "given": "a tenant with standard verification",
              "when": "the tenant purchases premium verification service",
              "then": "the system upgrades verification status after payment"
            }
          ]
        }
      ]
    },
    {
      "name": "Notification Context",
      "features": [
        {
          "name": "Notification Management",
          "scenarios": [
            {
              "title": "New match notification",
              "given": "new tenant matches for a property owner",
              "when": "the matching system identifies new matches",
              "then": "the system sends new match notification to the property owner"
            },
            {
              "title": "Profile view notification",
              "given": "a tenant profile viewed by property owner",
              "when": "the profile view occurs",
              "then": "the system sends profile view notification to the tenant"
            },
            {
              "title": "Listing expiration alert",
              "given": "a tenant listing approaching expiration",
              "when": "the expiration threshold is reached",
              "then": "the system sends listing expiration alert to the tenant"
            },
            {
              "title": "New message notification",
              "given": "a user receives a new message",
              "when": "the message is delivered",
              "then": "the system sends new message notification to the recipient"
            },
            {
              "title": "Notification preference management",
              "given": "a user wanting to manage notification preferences",
              "when": "the user updates notification settings",
              "then": "the system saves and applies the new notification preferences"
            },
            {
              "title": "Critical notification delivery failure",
              "given": "a critical notification failing to deliver",
              "when": "the delivery failure is detected",
              "then": "the system logs the failure and attempts alternative delivery methods"
            },
            {
              "title": "Excessive notifications",
              "given": "a user receiving too many notifications",
              "when": "the system detects notification frequency threshold exceeded",
              "then": "the system groups notifications and suggests preference adjustment"
            },
            {
              "title": "Notification with sensitive information",
              "given": "a system preparing to send notification",
              "when": "the notification contains sensitive information",
              "then": "the system redacts sensitive information before sending"
            }
          ]
        }
      ]
    }
  ]
}