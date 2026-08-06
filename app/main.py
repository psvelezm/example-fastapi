from fastapi import FastAPI
from pydantic import BaseModel
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
from .database import SessionLocal
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
print(settings.database_username)

#models.base.metadata.create_all(bind=engine). 
#no longer needed since we are using alembic to handle migrations


pwd_context = PasswordHash([BcryptHasher()])

app = FastAPI()

origins = ["*","http://google.com"]  


app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

#while True:
    #try:
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', port='5433', password='junior26', cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print("Database connection was successful!")
        #break
    #except Exception as error:
        #print("Connecting to database failed")
        #print("Error: ", error)
        #time.sleep(2)


#my_posts = [{"title": "Title of post 1", "content": "content of post 1", "id":1},
#            {"title": "favorite foods", "content": "I like pizza", "id": 2 }]

#def find_post(id):
#     for p in my_posts:
#        if p["id"] == id:
#            return p 

#def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p ['id'] == id:
#            return i

app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router) 
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my PROD Heroku-API application!!!"}

#@app.get("/sqlalchemy")
#def test_posts(db: Session = Depends(get_db)):
#    posts = db.query(models.Post).all()
#    print(posts) 
#    return {"data": posts}
