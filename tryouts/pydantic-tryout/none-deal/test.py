from pydantic import BaseModel, Field


class TestModel(BaseModel):
    name: str | None
    age: int | None = ...
    city: str | None = "seoul"


a = TestModel(age=None)
print(a)
print(a.name)


class FooModel(BaseModel):
    id: int
    name: str = None  # this makes add | None
    description: str = "Foo"
    apple: int = Field(..., alias="pear")


print(FooModel(id=123, name=None, pear=1))
