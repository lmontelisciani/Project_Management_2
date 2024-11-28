from fastapi import APIRouter, Depends, Query
from starlette import status

from app.api.dependencies.database import get_repository
from app.db.repositories.users import UsersRepository
from app.models.schemas.users import User, ListOfUsersInResponse


router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=ListOfUsersInResponse,
    name='user:check'
)
async def get_users(
        team_name: str | None = Query(None,),
        users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> ListOfUsersInResponse:
    if users := await users_repo.get_users_by_team(team_name=team_name):
        return ListOfUsersInResponse(
            users=[User(**user.dict()) for user in users],
            count_users=len(users)
        )
    else:
        return ListOfUsersInResponse(
            users=[],
            count_users=0
        )
