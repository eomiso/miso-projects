from pydantic import BaseModel, BaseSettings, root_validator


class Setting(BaseSettings):
    lower_case: str | None = None
    UPPER_CASE: str | None = None

    @root_validator(pre=True)
    def pre_validator(cls, values):
        print("PreRootValidator")
        print(values)
        return values

    @root_validator(pre=False)
    def none_pre_validator(cls, values):
        print("RootValidator")
        print(values)
        return values

    class Config:
        case_sensitive = False


import os

os.environ["LOWER_CASE"] = "os_var"
config = {
    "LOWER_CASE": "config_var",
}
try:
    Setting(**config)
except Exception as e:
    print(e)


class ModelSettings(BaseModel):
    lower_case: str | None = None
    UPPER_CASE: str | None = None

    @root_validator(pre=True)
    def pre_validator(cls, values):
        print("PreRootValidator")
        print(values)
        return values

    @root_validator(pre=False)
    def none_pre_validator(cls, values):
        print("RootValidator")
        print(values)
        return values

    class Config:
        anystr_lower = True


ModelSettings(**config)
