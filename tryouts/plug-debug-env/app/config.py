from enum import Enum

from pydantic import BaseModel, Field


class LogLevelEnum(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class StageEnum(str, Enum):
    TEST = "test"
    STAG = "stag"
    DEV = "dev"
    PROD = "prod"


class Settings(BaseModel):
    NAME: str = Field(..., env="NAME")
    LOG_LEVEL: LogLevelEnum
    STAGE: str = Field(..., env="STAGE")

    class Config:
        env_prefix = "API_"

    @classmethod
    def get_log_level(cls, stage: StageEnum) -> LogLevelEnum:
        if stage in (StageEnum.TEST, StageEnum.STAG):
            return LogLevelEnum.DEBUG
        elif stage == StageEnum.DEV:
            return LogLevelEnum.DEBUG
        elif stage == StageEnum.PROD:
            return LogLevelEnum.INFO


settings = Settings(
    NAME="plug-debug-env",
    STAGE=StageEnum.PROD,  # Set the appropriate stage here based on your environment
    LOG_LEVEL=Settings.get_log_level(StageEnum.PROD),
)
