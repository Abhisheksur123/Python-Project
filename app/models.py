from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId

class Blog(BaseModel):
    id: Optional[ObjectId]
    title: str
    content: str
    author: str
    likes: int = 0
    dislikes: int = 0
    comments: List[str] = []

class Comment(BaseModel):
    id: Optional[ObjectId]
    text: str
    author: str
