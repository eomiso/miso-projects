from pydantic import BaseModel


class C1(BaseModel):
    name: str
    age: int


class C1_work:
    def __init__(name, age):
        self.name = name
        self.age = age


class C2(BaseModel):
    persons: List[C1]
    city: str


a = C1.from_json(
    {
        "persons": [
            {"name": "John", "age": 32},
            {"name": "Alice", "age": 28},
            {"name": "Bob", "age": 45},
        ],
        "city": "New York",
    }
)


type(a.persons[1])  # C1


C2(persons=[C1(i) for i in persons], city="New York")
