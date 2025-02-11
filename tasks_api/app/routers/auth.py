from fastapi import HTTPException, Response, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas,utils, oauth2,database


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login",response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.name == user_credentials.username).first() 

    if not user:
        raise HTTPException(status_code=403, detail=f"Invalid Credentials") 
	
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=403, detail=f"Invalid Credentials")


    access_token = oauth2.create_access_token(data={"user_id": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
    