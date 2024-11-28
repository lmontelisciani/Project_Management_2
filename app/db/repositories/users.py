from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB
from app.db.queries.queries import queries


class UsersRepository(BaseRepository):

    async def get_by_email(self, *, email: str) -> UserInDB:
        if user_row := await queries.get_user_by_email(self.connection, email=email):
            return UserInDB(**user_row)

        raise EntityDoesNotExist('user with this email {0} does not exist'.format(email))

    async def get_by_username(self, *, username: str) -> UserInDB:
        if user_row := await queries.get_user_by_username(self.connection, username=username):
            return UserInDB(**user_row)

        raise EntityDoesNotExist('user with this username {0} does not exist'.format(username))

    async def create(
            self,
            *,
            username: str,
            email: str,
            first_name: str,
            last_name: str,
            password: str,
            photo: bytes = b''
    ) -> UserInDB:
        user = UserInDB(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            photo=photo,
            is_active=True,
            is_project_manager=False
        )
        user.generate_password(password=password)

        async with self.connection.transaction():
            user_row = await queries.create_new_user(
                self.connection,
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                photo=user.photo,
                salt=user.salt,
                hashed_password=user.hashed_password
            )
        return user.copy(update=dict(user_row))

    async def update(
            self,
            *,
            user: User,
            username: str = None,
            email: str = None,
            password: str = None,
            first_name: str = None,
            last_name: str = None,
            photo: bytes = b''
    ) -> UserInDB:
        user_id_db = await self.get_by_username(username=user.username)

        user_id_db.username = username or user_id_db.username
        user_id_db.email = email or user_id_db.email
        user_id_db.first_name = first_name or user_id_db.first_name
        user_id_db.last_name = last_name or user_id_db.last_name
        user_id_db.photo = photo or user_id_db.photo

        if password:
            user_id_db.generate_password(password=password)

        async with self.connection.transaction():
            user_row = await queries.update_user_by_username(
                self.connection,
                username=user.username,
                new_username=user_id_db.username,
                new_email=user_id_db.email,
                new_first_name=user_id_db.first_name,
                new_last_name=user_id_db.last_name,
                new_photo=user_id_db.photo,
                new_salt=user_id_db.salt,
                new_hashed_password=user_id_db.hashed_password
            )
        return UserInDB(**user_row)

    async def assign_user_to_team(
            self,
            *,
            username: str,
            team_name: str,
            role_name: str
    ) -> UserInDB:
        ...

    async def get_users_by_team(self, *, team_name: str = None) -> list[UserInDB]:
        if team_name:
            users_row = await queries.get_users_by_team(
                self.connection,
                team_name=team_name
            )
        else:
            users_row = await queries.get_all_users(
                self.connection
            )
        return [UserInDB(**user_row) for user_row in users_row]
