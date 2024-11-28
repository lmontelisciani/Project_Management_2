from pydantic import BaseModel, BaseConfig


def convert_field_to_camel_case(field: str) -> str:
    return ''.join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(field.split('_'))
    )


class BaseDomainModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = convert_field_to_camel_case
