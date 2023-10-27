import asyncio
from datetime import datetime
import click


async def sleep_five():

    five_seconds = 5

    print(f"starting {five_seconds} sleep 😴")

    await asyncio.sleep(five_seconds)

    print(f"finished {five_seconds} sleep ⏰")

    return five_seconds


async def sleep_three_then_five():

    three_seconds = 3

    print(f"starting {three_seconds} sleep 😴")

    await asyncio.sleep(three_seconds)

    print(f"finished {three_seconds} sleep ⏰")

    await sleep_five()

    return three_seconds + 5


async def main():

    results = await asyncio.gather(
        sleep_five(),
        sleep_three_then_five())

    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
