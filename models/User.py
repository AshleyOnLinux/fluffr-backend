from pydantic import BaseModel


class User(BaseModel):
    userid: int
    handle: str
    name: str
    password: str
