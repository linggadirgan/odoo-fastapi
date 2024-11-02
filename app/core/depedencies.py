from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Placeholder logic to validate user
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "test_user"}
