from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ai_service_env: str = "development"
    chroma_persist_directory: str = "../storage/chroma"
    chroma_collection_name: str = "finsight_filings"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
