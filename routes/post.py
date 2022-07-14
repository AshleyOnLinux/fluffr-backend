from fastapi import APIRouter

from config.db import conn
from schemas.post import postsEntity

postRoute = APIRouter()


@postRoute.get("/p/")
async def postIndexPage():
    return {
        "code": 400,
        "error": "bad request",
        "message": "No post id provided."
    }


@postRoute.get("/p/{postid}/")
async def postPage(postid: str):
    query = {"postID": postid}
    item = postsEntity(conn.fluffrcf.posts.find(query))

    if item == []:
        return {
            "code": 404,
            "error": "post could not found",
            "message": "Post does not exist."
        }
    else:
        item = item[0]
        return {
            "author_id": item["authorID"],
            "title": item["postTitle"],
            "textContent": item['postTextContent'],
            "containsMedia": item['containsMedia'],
            "comments": item['comments'],
            "likes": item['likes'],
            "bookmarks": item['bookmarks'],
            "media_id": item['mediaID'],
            "post_id": item['postID'],
            "awards": item["awards"],
            "flair": item["flair"]
        }
