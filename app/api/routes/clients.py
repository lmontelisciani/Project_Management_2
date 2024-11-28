from fastapi import APIRouter, Body, Depends, HTTPException, Query
from starlette import status

from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.database import get_repository
from app.db.errors import EntityDoesNotExist
from app.db.repositories.clients import ClientsRepository
from app.models.domain.users import User
from app.models.schemas.clients import (
    ClientInResponse,
    ClientInCreate,
    ListOfClientsInResponse,
    DEFAULT_CLIENTS_LIMIT,
    DEFAULT_CLIENTS_OFFSET
)

from app.resources import strings
from app.services.clients import check_client_name_is_taken


router = APIRouter()


@router.post(
    '',
    response_model=ClientInResponse,
    name='client:create'
)
async def create_client(
        client_create: ClientInCreate = Body(..., embed=True, alias='client'),
        client_repo: ClientsRepository = Depends(get_repository(ClientsRepository)),
        user: User = Depends(get_current_user_authorizer())
) -> ClientInResponse:
    if await check_client_name_is_taken(client_repo, client_name=client_create.client_name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.CLIENT_ALREADY_EXISTS
        )

    client = await client_repo.create(**client_create.dict())
    return ClientInResponse(
        client_name=client.client_name,
    )


@router.get(
    '/{id}',
    response_model=ClientInResponse,
    name='client:get_by_id'
)
async def get_client_by_id(
        id_: int,
        client_repo: ClientsRepository = Depends(get_repository(ClientsRepository))
) -> ClientInResponse:
    try:
        client_row = await client_repo.get_by_id(id_=id_)
        return ClientInResponse(**client_row.dict())
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.CLIENT_DOES_NOT_EXIST
        )


@router.get(
    '/',
    response_model=ListOfClientsInResponse,
    name='client:get_all_client'
)
async def get_all_clients(
        limit: int = Query(DEFAULT_CLIENTS_LIMIT, ge=1),
        offset: int = Query(DEFAULT_CLIENTS_OFFSET, ge=0),
        client_repo: ClientsRepository = Depends(get_repository(ClientsRepository))
) -> ListOfClientsInResponse:
    if clients := await client_repo.get_all(limit=limit, offset=offset):
        clients_for_response = [ClientInResponse(**client.dict()) for client in clients]
        return ListOfClientsInResponse(
            clients=clients_for_response,
            clients_count=len(clients_for_response)
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=strings.CLIENTS_DOES_NOT_EXIST
    )
