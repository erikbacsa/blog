from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Erik",
        "title": "My First Post",    
        "content": "Hello World!"    
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "My First Post",   
        "content": "Hello World!"  
    }
]

@app.get("/", include_in_schema=False)
@app.get("/posts",  include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
          {"request": request,
            "posts": posts,
              "title": "Home",
              } )

@app.get("/api/posts")
def get_posts():
    return posts
