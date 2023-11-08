import asyncio


async def nested():
    return 42


def sync_nested():
    return 43


async def main():
    loop = asyncio.get_event_loop()

    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # task로 등록조차 안되었다는 것인가?
    # await 가 있어야지 명시적으로 등록이 되는 것인지?
    # ㅇㅇ 그러함. 아니면 create_task를 써야됨
    # nested()

    # Error, Expects Coroutine
    task = loop.create_task(sync_nested())  # noqa

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())
