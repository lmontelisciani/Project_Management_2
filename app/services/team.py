from app.db.errors import EntityDoesNotExist
from app.db.repositories.teams import TeamRepository


async def check_team_name_is_taken(repo: TeamRepository, team_name: str) -> bool:
    try:
        await repo.get_by_team_name(team_name=team_name)
    except EntityDoesNotExist:
        return False
    return True
