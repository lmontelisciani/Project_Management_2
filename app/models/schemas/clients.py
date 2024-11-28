from app.models.schemas.base import BaseSchema


DEFAULT_CLIENTS_LIMIT = 5
DEFAULT_CLIENTS_OFFSET = 0


class Client(BaseSchema):
    client_name: str


class ClientInCreate(Client):
    ...


class ClientInResponse(Client):
    ...


class ListOfClientsInResponse(BaseSchema):
    clients: list[ClientInResponse]
    clients_count: int
