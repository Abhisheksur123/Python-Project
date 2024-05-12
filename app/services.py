from pymongo import MongoClient
from bson import ObjectId
from .models import Blog, Comment

client = MongoClient("mongodb://localhost:27017/")
db = client["blog_db"]
collection = db["blogs"]

def get_all_blogs():
    return [Blog(**blog) for blog in collection.find()]

def get_blog_by_id(blog_id: str):
    return Blog(**collection.find_one({"_id": ObjectId(blog_id)}))

def create_blog(blog: Blog):
    blog_dict = blog.dict()
    del blog_dict['id']
    inserted = collection.insert_one(blog_dict)
    return str(inserted.inserted_id)

def update_blog(blog_id: str, blog: Blog):
    updated = collection.update_one({"_id": ObjectId(blog_id)}, {"$set": blog.dict()})
    return updated.modified_count > 0

def delete_blog(blog_id: str):
    deleted = collection.delete_one({"_id": ObjectId(blog_id)})
    return deleted.deleted_count > 0

def add_comment(blog_id: str, comment: Comment):
    updated = collection.update_one({"_id": ObjectId(blog_id)}, {"$push": {"comments": comment.dict()}})
    return updated.modified_count > 0

def like_blog(blog_id: str):
    updated = collection.update_one({"_id": ObjectId(blog_id)}, {"$inc": {"likes": 1}})
    return updated.modified_count > 0

def dislike_blog(blog_id: str):
    updated = collection.update_one({"_id": ObjectId(blog_id)}, {"$inc": {"dislikes": 1}})
    return updated.modified_count > 0
