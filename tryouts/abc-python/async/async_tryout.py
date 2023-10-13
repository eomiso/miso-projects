import asyncio
import sys


async def log(msg, l=10, f="."):
    for i in range(l * 2 + 1):
        if i == l:
            for c in msg:
                sys.stdout.write(c)
                sys.stdout.flush()
                await asyncio.sleep(0.05)
        else:
            sys.stdout.write(f)
            sys.stdout.flush()
        await asyncio.sleep(0.2)
    sys.stdout.write("\n")
    sys.stdout.flush()


class AsyncCM:
    def __init__(self, i):
        self.i = i

    async def __aenter__(self):
        await log("Entering Context")
        return self

    async def __aexit__(self, *arags):
        await log("Exiting Context")
        return self


class Ticker:
    def __init__(self, to, interval=0.5):
        self.value = 0
        self.to = to
        self.interval = interval

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.value >= self.to:
            raise StopAsyncIteration

        await asyncio.sleep(self.interval)
        r, self.value = self.value, self.value + 1
        return r


async def test():
    t = Ticker(10)
    async for i in t:
        print(i)


async def main1():
    """Test Async Context Manager"""
    async with AsyncCM(2) as c:
        for i in range(c.i):
            print(i)


async def aticker(a, interval=0.5):
    i = 0
    while i < a:
        await asyncio.sleep(interval)
        yield i
        i += 1


async def test2():
    async for i in aticker(10):
        print(i)


## 실행
# asyncio.run(main1())

if __name__ == "__main__":
    fs = [test2() for _ in range(3)]

    asyncio.run(asyncio.wait(fs))
