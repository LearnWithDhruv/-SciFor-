from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

db = []

class BlogPost(BaseModel):
    title: str
    content:str
    author: str
    published: Optional[bool] = False

@app.post("/blog/")
def create_blog_post(blog_post: BlogPost):
    db.append(blog_post)
    return {"message": "Blog Post Created Successfully"}

@app.get("/blog/", response_model=List[BlogPost])
def get_all_blogs():
    return db

@app.get("/blog/{post_id}")
def update_blog_post(post_id: int, updated_post: BlogPost):
    if post_id >= len(db):
        raise HTTPException(status_code=404, detail = "Blog post not found.")
    return db[post_id]

@app.put("/blog/{post_id}")
def update_blog(post_id: int, updated_post: BlogPost):
    if post_id >= len(db):
        raise HTTPException(status_code=404, detail="Blog post not found.")
    db[post_id] = updated_post
    return {"message": "Blog Post Updated Successfully."}

@app.delete("/blog/{post_id}")
def delete_blog_post(post_id: int):
    if post_id >= len(db):
        raise HTTPException(status_code=404, detail="Blog post not found.")
    db.pop(post_id)
    return {"message": "Blog post deleted successfully"}
