from app.models.domain.base import BaseDomainModel


class BaseSchema(BaseDomainModel):
    class Config(BaseDomainModel.Config):
        orm_mode = True
