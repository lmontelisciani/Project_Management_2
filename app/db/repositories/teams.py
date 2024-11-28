from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.teams import Team


class TeamRepository(BaseRepository):

    async def create(self, *, team_name: str) -> Team:
        team = Team(team_name=team_name)

        async with self.connection.transaction():
            team_row = await queries.create_new_team(
                self.connection,
                team_name=team.team_name,
            )
        return team.copy(update=dict(team_row))

    async def get_by_id(self, *, id_: int) -> Team:
        if team_row := await queries.get_team_by_id(self.connection, team_id=id_):
            return Team(**team_row)

        raise EntityDoesNotExist('team with this id does not exist')

    async def get_by_team_name(self, *, team_name: str) -> Team:
        if team_row := await queries.get_team_by_name(self.connection, team_name=team_name):
            return Team(**team_row)

        raise EntityDoesNotExist('team with this name does not exist')

    async def get_all(self, *, limit: int, offset: int) -> list[Team]:
        team_rows = await queries.get_all_teams(self.connection, limit=limit, offset=offset)
        return [Team(**team_row) for team_row in team_rows]
