from fastapi import APIRouter

from schemas.login import loginEntity
from config.db import conn
from schemas.user import usersEntity

authRoute = APIRouter()


@authRoute.post("/login")
async def loginPage(data: loginEntity):
    email = str(data.email)
    if "@" in email:
        query = {"email": data.email}
        getHandleDetails = usersEntity(conn.fluffrcf.users.find(query))
        if getHandleDetails[0]['password'] == data.password:
            return {"code": 200}
        else:
            return {"code": 403}

    else:
        if data.handle == "":
            return {
                "message": "Hello! There was an error. The error message is listed below.",
                "error": "no handle or email.",
            }
        else:
            # get handles and compare with password
            query = {"handle": data.handle}
            getHandleDetails = usersEntity(conn.fluffrcf.users.find(query))
            if getHandleDetails[0]['password'] == data.password:
                return {
                    "code": 200,
                    "token": "ADD TOKEN HERE"
                }
            else:
                return {
                    "code": 401,
                    "error": "incorrect credentials",
                    "message": "Incorrect username or password."
                }
