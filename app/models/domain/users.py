from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.base import BaseDomainModel
from app.services import security


class User(BaseDomainModel):
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_project_manager: bool
    photo: bytes | None


class UserInDB(IDModelMixin, DateTimeModelMixin, User):
    salt: str = ''
    hashed_password: str = ''

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def generate_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)

