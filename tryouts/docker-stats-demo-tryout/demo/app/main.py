import asyncio
import datetime
from dataclasses import dataclass, field
from queue import Queue


def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")


@dataclass
class Event:
    name: str
    time: str = field(default_factory=current_time)


class Manager:
    def __init__(self, interval):
        self.interval = interval
        self.queue = Queue()

    async def stream(self):
        uid = 0
        while True:
            event = Event(name=uid)  # Create or fetch event somehow
            self.queue.put(event)
            await asyncio.sleep(self.interval)
            uid += 1


class Processor:
    @staticmethod
    def process_event(event: Event):
        print(f"{event.name}    {event.time}")


async def main():
    manager = Manager(0.1)  # Equivalent to time.Second / 10
    processor = Processor()

    asyncio.create_task(manager.stream())

    while True:
        if not manager.queue.empty():
            event = manager.queue.get()
            processor.process_event(event)
        await asyncio.sleep(0)  # Yield control to the event loop


if __name__ == "__main__":
    asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# if __name__ == "__main__":
#     event = Event(
#         name="test",
#     )

#     print(event.time)
