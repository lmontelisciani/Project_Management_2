from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.clients import Client


class ClientsRepository(BaseRepository):

    async def create(self, *, client_name: str) -> Client:
        client = Client(client_name=client_name)

        async with self.connection.transaction():
            client_row = await queries.create_new_client(
                self.connection,
                client_name=client.client_name
            )
        return client.copy(update=dict(client_row))

    async def get_by_id(self, *, id_: int) -> Client:
        if client_row := await queries.get_client_by_id(self.connection, client_id=id_):
            return Client(**client_row)

        raise EntityDoesNotExist('client with this id does not exist')

    async def get_by_client_name(self, *, client_name: str) -> Client:
        if client_row := await queries.get_client_by_name(self.connection, client_name=client_name):
            return Client(**client_row)

        raise EntityDoesNotExist('client with this name does not exist')

    async def get_all(self, *, limit: int, offset: int) -> list[Client]:
        client_rows = await queries.get_all_clients(self.connection, limit=limit, offset=offset)
        return [Client(**client_row) for client_row in client_rows]
