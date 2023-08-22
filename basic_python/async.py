#
# https://www.youtube.com/@akash071
#

import asyncio


async def delay(msg, sec):
    await asyncio.sleep(sec)
    print(msg)


async def main():
    task1 = delay("Hello", 1)
    task2 = delay("Python", 2)
    task3 = delay("Fans!", 3)

    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
