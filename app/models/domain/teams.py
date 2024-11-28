from app.models.common import IDModelMixin
from app.models.domain.base import BaseDomainModel


class Team(BaseDomainModel):
    team_name: str


class TeamInDB(IDModelMixin, Team):
    ...
