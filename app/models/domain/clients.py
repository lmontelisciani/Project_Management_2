from app.models.common import IDModelMixin
from app.models.domain.base import BaseDomainModel


class Client(BaseDomainModel):
    client_name: str


class ClientInDB(IDModelMixin, Client):
    ...
