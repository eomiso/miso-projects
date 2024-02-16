import asyncio


async def dependency():
    a = yield 42
    print("hello")
    print(a)


async def fn_using_dep():
    i = dependency()
    print(i)
    res = await i.asend(None)
    print(res)
    try:
        res = await i.asend("World")
    except StopAsyncIteration as e:
        pass
    # print(res)
    print("when is dependcy resumed?")


async def main():
    await fn_using_dep()


if __name__ == "__main__":
    asyncio.run(main())
