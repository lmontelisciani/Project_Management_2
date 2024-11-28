from app.models.schemas.base import BaseSchema


DEFAULT_TEAMS_LIMIT = 5
DEFAULT_TEAMS_OFFSET = 0


class Team(BaseSchema):
    team_name: str


class TeamInCreate(Team):
    ...


class TeamInResponse(Team):
    ...


class ListOfTeamsInResponse(BaseSchema):
    teams: list[TeamInResponse]
    teams_count: int
