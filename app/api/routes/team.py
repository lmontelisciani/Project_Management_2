from fastapi import APIRouter, Body, Depends, HTTPException, Query
from starlette import status

from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.database import get_repository
from app.db.errors import EntityDoesNotExist
from app.db.repositories.teams import TeamRepository
from app.models.domain.users import User
from app.models.schemas.teams import (
    TeamInResponse,
    TeamInCreate,
    ListOfTeamsInResponse,
    DEFAULT_TEAMS_LIMIT,
    DEFAULT_TEAMS_OFFSET
)
from app.resources import strings
from app.services.team import check_team_name_is_taken

router = APIRouter()


@router.post(
    '',
    response_model=TeamInResponse,
    name='team:create'
)
async def create_team(
        team_create: TeamInCreate = Body(..., embed=True, alias='team'),
        team_repo: TeamRepository = Depends(get_repository(TeamRepository)),
        user: User = Depends(get_current_user_authorizer())
) -> TeamInResponse:
    if await check_team_name_is_taken(team_repo, team_name=team_create.team_name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.TEAM_ALREADY_EXISTS
        )

    team = await team_repo.create(**team_create.dict())
    return TeamInResponse(
        team_name=team.team_name,
    )


@router.get(
    '/{id}',
    response_model=TeamInResponse,
    name='team:get_by_id'
)
async def get_team_by_id(
        id_: int,
        team_repo: TeamRepository = Depends(get_repository(TeamRepository))
) -> TeamInResponse:
    try:
        team_row = await team_repo.get_by_id(id_=id_)
        return TeamInResponse(**team_row.dict())
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.TEAM_DOES_NOT_EXIST
        )


@router.get(
    '/',
    response_model=ListOfTeamsInResponse,
    name='team:get_all_teams'
)
async def get_all_teams(
        limit: int = Query(DEFAULT_TEAMS_LIMIT, ge=1),
        offset: int = Query(DEFAULT_TEAMS_OFFSET, ge=0),
        teams_repo: TeamRepository = Depends(get_repository(TeamRepository))
) -> ListOfTeamsInResponse:
    if teams := await teams_repo.get_all(limit=limit, offset=offset):
        teams_for_response = [TeamInResponse(**team.dict()) for team in teams]
        return ListOfTeamsInResponse(
            teams=teams_for_response,
            teams_count=len(teams_for_response)
        )
    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=strings.TEAMS_DOES_NOT_EXIST
    )
