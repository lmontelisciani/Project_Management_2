from app.db.errors import EntityDoesNotExist
from app.db.repositories.clients import ClientsRepository


async def check_client_name_is_taken(repo: ClientsRepository, client_name: str) -> bool:
    try:
        await repo.get_by_client_name(client_name=client_name)
    except EntityDoesNotExist:
        return False
    return True
