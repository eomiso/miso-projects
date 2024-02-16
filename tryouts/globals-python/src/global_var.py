class Foo:
    cnt = 0

    def __new__(cls, *args, **kwargs):
        cls.cnt += 1

        print(cls.cnt)

        return super().__new__(cls)

    def __init__(self, input: str):
        print(f"{input} has been created!")

    def run(self):
        print("Run foo")


foo = Foo("created")
