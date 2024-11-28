from asyncpg import Connection, Record


class UsersQueriesMixin:
    async def get_user_by_email(self, conn: Connection, *, email: str) -> Record: ...
    async def get_user_by_username(self, conn: Connection, *, username: str) -> Record: ...
    async def create_new_user(
        self,
        conn: Connection,
        *,
        username: str,
        email: str,
        salt: str | None,
        hashed_password: str | None,
        first_name: str,
        last_name: str,
        is_active: bool = True,
        is_project_manager: bool = False,
        photo: bytes | None = b''
    ) -> Record: ...
    async def update_user_by_username(
            self,
            conn: Connection,
            *,
            username: str,
            new_username: str,
            new_email: str,
            new_salt: str | None,
            new_hashed_password: str | None,
            new_first_name: str,
            new_last_name: str,
            new_photo: bytes | None
    ) -> Record: ...
    async def get_users_by_team(self, conn: Connection, *, team_name: str) -> list[Record]: ...
    async def get_all_users(self, conn: Connection) -> list[Record]: ...

class TeamQueriesMixin:
    async def create_new_team(self, conn: Connection, *, team_name: str) -> Record: ...
    async def get_team_by_id(self, conn: Connection, *, team_id: int) -> Record: ...
    async def get_team_by_name(self, conn: Connection, *, team_name: str) -> Record: ...
    async def get_all_teams(self, conn: Connection, *, limit: int, offset: int) -> list[Record]: ...


class ClientsQueriesMixin:
    async def create_new_client(self, conn: Connection, *, client_name: str) -> Record: ...
    async def get_client_by_id(self, conn: Connection, *, client_id: int) -> Record: ...
    async def get_client_by_name(self, conn: Connection, *, client_name: str) -> Record: ...
    async def get_all_clients(self, conn: Connection, *, limit: int, offset: int) -> list[Record]: ...


class Queries(
    UsersQueriesMixin,
    TeamQueriesMixin,
    ClientsQueriesMixin
): ...

queries: Queries
