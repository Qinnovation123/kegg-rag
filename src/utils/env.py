from pydantic_settings import BaseSettings


class Config(BaseSettings):
    dev: bool = __debug__

    model_config = {"env_file": ".env"}


env = Config()


dev = env.dev
