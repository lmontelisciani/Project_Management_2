from asyncpg.connection import Connection


class BaseRepository:
    def __init__(self, _connection: Connection, *args, **kwargs) -> None:
        self._connection: Connection = _connection

    @property
    def connection(self) -> Connection:
        return self._connection
