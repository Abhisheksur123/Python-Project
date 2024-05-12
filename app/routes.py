from fastapi import APIRouter, HTTPException
from .services import *

router = APIRouter()

@router.get("/blogs", response_model=List[Blog])
def read_blogs():
    return get_all_blogs()

@router.get("/blogs/{blog_id}", response_model=Blog)
def read_blog(blog_id: str):
    blog = get_blog_by_id(blog_id)
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.post("/blogs", response_model=str)
def create_blog(blog: Blog):
    return create_blog(blog)

@router.put("/blogs/{blog_id}", response_model=bool)
def update_blog(blog_id: str, blog: Blog):
    return update_blog(blog_id, blog)

@router.delete("/blogs/{blog_id}", response_model=bool)
def delete_blog(blog_id: str):
    return delete_blog(blog_id)

@router.post("/blogs/{blog_id}/comments", response_model=bool)
def add_comment_to_blog(blog_id: str, comment: Comment):
    return add_comment(blog_id, comment)

@router.put("/blogs/{blog_id}/like", response_model=bool)
def like_blog(blog_id: str):
    return like_blog(blog_id)

@router.put("/blogs/{blog_id}/dislike", response_model=bool)
def dislike_blog(blog_id: str):
    return dislike_blog(blog_id)
