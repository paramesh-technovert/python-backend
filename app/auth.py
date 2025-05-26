from jose import jwt
import requests
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
import os

# Azure AD tenant and client info again for auth setup
TENANT_ID = os.getenv("AZURE_AD_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_AD_CLIENT_ID")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Azure AD OpenID Connect discovery endpoint URL
DISCOVERY_URL = f"{AUTHORITY}/v2.0/.well-known/openid-configuration"

def get_openid_config():
    # Fetch Azure AD OpenID Connect configuration
    r = requests.get(DISCOVERY_URL)
    if r.status_code != 200:
        raise Exception("Failed to fetch OpenID config from Azure")
    return r.json()

# Get OIDC config, including JWKS URI and issuer info
openid_config = get_openid_config()
jwks_uri = openid_config["jwks_uri"]
issuer = openid_config["issuer"]

# Fetch the JSON Web Key Set (JWKS) for verifying tokens
jwks = requests.get(jwks_uri).json()

# FastAPI security scheme for OAuth2 Authorization Code flow
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=openid_config["authorization_endpoint"],
    tokenUrl=openid_config["token_endpoint"]
)

def decode_token(token: str = Depends(oauth2_scheme)):
    """
    Dependency to decode and validate JWT access token from Azure AD.
    - Verifies token signature using Azure's public keys.
    - Checks audience and issuer claims.
    - Raises HTTP 401 if validation fails.
    """
    try:
        # Get the header to find which key was used to sign the token
        unverified_header = jwt.get_unverified_header(token)

        # Find the correct public key from JWKS that matches the token's kid
        key = next(
            (k for k in jwks["keys"] if k["kid"] == unverified_header["kid"]),
            None
        )
        if not key:
            raise HTTPException(status_code=401, detail="Key not found")

        # Decode and verify the token using the found key and expected claims
        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=CLIENT_ID,
            issuer=issuer
        )
        # Return the token payload (claims) on success
        return payload

    except Exception as e:
        # Raise an authentication error if verification fails
        raise HTTPException(status_code=401, detail=f"Authentication error: {str(e)}")