from fastapi import APIRouter

from config.db import conn
from schemas.user import usersEntity
from schemas.media import mediasEntity

userRoute = APIRouter()


@userRoute.get("/u/")
async def userPage():
    return {
        "code": 400,
        "error": "bad request",
        "message": "No user handle provided."
    }


@userRoute.get("/aid/")
async def userPage():
    return {
        "code": 400,
        "error": "bad request",
        "message": "No account ID provided."
    }


@userRoute.get("/uid/")
async def userPage():
    return {
        "code": 400,
        "error": "bad request",
        "message": "No account ID provided."
    }


@userRoute.get("/u/{handle}/")
async def handlePage(handle: str):
    query = {"handle": handle}
    item = usersEntity(conn.fluffrcf.users.find(query))

    if item == []:
        return {
            "code": 404,
            "error": "user unknown or not found",
            "message": "User does not exist."
        }
    else:
        item = item[0]
        query = {"author_id": item["account_id"]}
        mediaByUser = mediasEntity(conn.fluffrcf.media.find(query))

        if mediaByUser == []:
            return {
                "account_id": item["account_id"],
                "nickname": item["nickname"],
                "handle": item['handle'],

                "social_links": item['social_links'],
                "awards": item['awards'],
                "roles": item['roles']
            }
        else:
            mediaByUser = mediaByUser[0]
            return {
                "account_id": item["account_id"],
                "nickname": item["nickname"],
                "handle": item['handle'],

                "mediaPosted": mediaByUser,
                "social_links": item['social_links'],
                "awards": item['awards'],
                "roles": item['roles']
            }


@userRoute.get("/aid/{aid}/")
async def handlePage(aid: str):
    query = {"account_id": aid}
    item = usersEntity(conn.fluffrcf.users.find(query))

    if item == []:
        return {
            "code": 404,
            "error": "user unknown or not found",
            "message": "User does not exist."
        }
    else:
        item = item[0]
        return {
            "account_id": item["account_id"],
            "nickname": item["nickname"],
            "handle": item['handle'],

            "social_links": item['social_links'],
            "awards": item['awards'],
            "roles": item['roles']
        }


@userRoute.get("/uid/{uid}/")
async def handlePage(uid: str):
    query = {"user_id": uid}
    item = usersEntity(conn.fluffrcf.users.find(query))

    if item == []:
        return {
            "code": 404,
            "error": "user unknown or not found",
            "message": "User does not exist."
        }
    else:
        item = item[0]
        return {
            "account_id": item["account_id"],
            "nickname": item["nickname"],
            "handle": item['handle'],

            "social_links": item['social_links'],
            "awards": item['awards'],
            "roles": item['roles']
        }
