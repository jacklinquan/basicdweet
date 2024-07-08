import time
import asyncio

import basicdweet


def test_sync_basicdweet():
    thing = "YOUR_THING"
    data = {"YOUR_DATA": "YOUR_VALUE"}

    dweet = basicdweet.dweet_for(thing, data)
    time.sleep(2)

    latest_dweet_list = basicdweet.get_latest_dweet_for(thing)
    latest_dweet = latest_dweet_list[0]
    time.sleep(2)

    assert latest_dweet["thing"] == dweet["thing"]
    assert latest_dweet["created"] == dweet["created"]
    assert latest_dweet["content"] == dweet["content"]

    dweets = basicdweet.get_dweets_for(thing)
    time.sleep(2)

    assert len(dweets) >= 1


async def async_basicdweet():
    thing = "YOUR_THING"
    data = {"YOUR_DATA": "YOUR_VALUE"}

    dweet = await basicdweet.async_dweet_for(thing, data)
    await asyncio.sleep(2)

    latest_dweet_list = await basicdweet.async_get_latest_dweet_for(thing)
    latest_dweet = latest_dweet_list[0]
    await asyncio.sleep(2)

    assert latest_dweet["thing"] == dweet["thing"]
    assert latest_dweet["created"] == dweet["created"]
    assert latest_dweet["content"] == dweet["content"]

    dweets = await basicdweet.async_get_dweets_for(thing)
    await asyncio.sleep(2)

    assert len(dweets) >= 1


def test_async_basicdweet():
    asyncio.run(async_basicdweet())
