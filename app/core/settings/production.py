from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    debug: bool = False
    docs_url: str = None
    redoc_url: str = None
    openapi_url: str = None

    class Config(AppSettings.Config):
        env_file = "prod.env"
