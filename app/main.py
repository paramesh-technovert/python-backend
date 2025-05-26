from fastapi import FastAPI, Depends
from app.auth import decode_token  # Dependency function to decode and validate JWT tokens
from app import api_router          # Your API route definitions
from fastapi.openapi.utils import get_openapi
import os

# Fetch Azure AD Tenant ID and Client ID from environment variables
TENANT_ID = os.getenv("AZURE_AD_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_AD_CLIENT_ID")

# Initialize FastAPI app with a global dependency that enforces authentication
app = FastAPI(
    # Every request will require a valid token decoded by decode_token
    dependencies=[Depends(decode_token)],
    # Configure Swagger UI OAuth2 settings to use PKCE with Authorization Code flow
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True
    }
)

# Include all your API routes
app.include_router(api_router)

@app.get("/")
def root():
    # A simple root endpoint that confirms API protection
    return {"message": "Welcome to the protected API"}

# Custom OpenAPI schema function to modify the default auto-generated schema
def custom_openapi():
    if app.openapi_schema:
        # Return the cached schema if already generated
        return app.openapi_schema

    # Generate the base OpenAPI schema using FastAPI's helper
    openapi_schema = get_openapi(
        title="FastAPI with Azure AD Auth",
        version="1.0.0",
        description="Protected API using Azure AD",
        routes=app.routes,
    )

    # Define OAuth2 security scheme for Azure AD using authorization code flow
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2": {
            "type": "oauth2",
            "flows": {
                "authorizationCode": {
                    # URLs for authorization and token exchange from Azure AD
                    "authorizationUrl": f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize",
                    "tokenUrl": f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token",
                    # Required scopes for accessing the API
                    "scopes": {
                        f"api://{CLIENT_ID}/userAccess": "Access the API",
                    }
                }
            },
        }
    }

    # Apply the OAuth2 security scheme to every operation in the OpenAPI paths
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"OAuth2": [f"api://{CLIENT_ID}/userAccess"]}]

    # Also apply security globally to all operations as a default
    openapi_schema["security"] = [{"OAuth2": [f"api://{CLIENT_ID}/userAccess"]}]

    # Cache the generated schema
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Override the default OpenAPI schema generator with the custom one
app.openapi = custom_openapi

