from pydantic import EmailStr

from app.models.schemas.base import BaseSchema


class User(BaseSchema):
    username: str
    email: EmailStr
    first_name: str
    last_name: str


class UserInLogin(BaseSchema):
    email: EmailStr
    password: str


class UserInCreate(User):
    password: str


class UserInUpdate(BaseSchema):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserWithToken(User):
    token: str


class UserInResponse(BaseSchema):
    user: UserWithToken


class ListOfUsersInResponse(BaseSchema):
    users: list[User]
    count_users: int
