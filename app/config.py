from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    database_hostname: str 
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


    class Config:
        env_file = ".env"



    #database_username: str = "postgres"
    #database_password: str = "junior26"
    #secret_key: str = "your-secret-key"

    #model_config = SettingsConfigDict(env_file=".env")


settings = Settings()