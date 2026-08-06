from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from datetime import datetime


#class Post(BaseModel):
#    title: str
#    content: str
#    published: bool = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

#class User(UserCreate):
    #id: int
    #created_at: datetime



class UserLogin(BaseModel):
    email: EmailStr
    password: str   

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1, ge=0)  # type: ignore # dir can only be 0 or 1        

##class CreatePost(BaseModel):
    #title: str
    #content: str
    #published: bool = True


#class UpdatePost(BaseModel):
    #title: str
    #content: str
    #published: bool

