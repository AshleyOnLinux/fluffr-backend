from pydantic import BaseModel


class loginEntity(BaseModel):
    email: str
    handle: str
    password: str
