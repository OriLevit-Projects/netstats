from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from ..models.user import UserCreate, User, Token
from ..utils.auth import verify_password, get_password_hash, create_access_token
from ..config import get_settings
from pymongo import MongoClient
from bson import ObjectId

router = APIRouter()
settings = get_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# MongoDB connection
client = MongoClient(settings.mongodb_url)
db = client[settings.database_name]
users_collection = db.users

@router.post("/signup", response_model=User)
async def signup(user: UserCreate):
    # Check if email already exists
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Create new user
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user_dict["password"])
    user_dict["role"] = "player"
    user_dict["is_active"] = True
    
    result = users_collection.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    
    # Remove password from response
    del user_dict["password"]
    return user_dict

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Find user by email
    user = users_collection.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}