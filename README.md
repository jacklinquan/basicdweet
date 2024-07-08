# Basic Dweet

[![PyPI version][pypi_img]][pypi_link]
[![Downloads][downloads_img]][downloads_link]

  [pypi_img]: https://badge.fury.io/py/basicdweet.svg
  [pypi_link]: https://badge.fury.io/py/basicdweet
  [downloads_img]: https://pepy.tech/badge/basicdweet
  [downloads_link]: https://pepy.tech/project/basicdweet

[Documentation](https://jacklinquan.github.io/basicdweet)

Basic APIs of the free dweet service.
Dweet is a simple machine-to-machine (M2M) service from [dweet.io](https://dweet.io).

This module only supports these dweet APIs of the free dweet service:

- `dweet for`
- `get latest dweet for`
- `get dweets for`

It also can be used in MicroPython.

## Installation

### Synchronous Programming

```shell
pip install basicdweet
```

### Asynchronous Programming

```shell
pip install basicdweet[aiohttp]
```

## Usage

### Synchronous Programming

<details open><summary>Code</summary>

```python
import time
import basicdweet

print(basicdweet.dweet_for("YOUR_THING", {"YOUR_DATA": "YOUR_VALUE"}))
time.sleep(2)
print(basicdweet.get_latest_dweet_for("YOUR_THING"))
time.sleep(2)
print(basicdweet.dweet_for("YOUR_THING", {"YOUR_DATA": "YOUR_VALUE_2"}))
time.sleep(2)
print(basicdweet.get_latest_dweet_for("YOUR_THING"))
time.sleep(2)
print(basicdweet.get_dweets_for("YOUR_THING"))
```
</details>

<details open><summary>Output</summary>

```
{'thing': 'YOUR_THING', 'created': '2024-07-05T04:53:36.896Z', 'content': {'YOUR_DATA': 'YOUR_VALUE'}, 'transaction': '9cd0b361-05fc-451d-be7b-280172242f25'}
[{'thing': 'YOUR_THING', 'created': '2024-07-05T04:53:36.896Z', 'content': {'YOUR_DATA': 'YOUR_VALUE'}}]
{'thing': 'YOUR_THING', 'created': '2024-07-05T04:53:42.697Z', 'content': {'YOUR_DATA': 'YOUR_VALUE_2'}, 'transaction': '926d396d-cf41-4feb-89c3-46ffb0960053'}
[{'thing': 'YOUR_THING', 'created': '2024-07-05T04:53:42.697Z', 'content': {'YOUR_DATA': 'YOUR_VALUE_2'}}]
[{'thing': 'YOUR_THING', 'created': '2024-07-05T04:53:42.697Z', 'content': {'YOUR_DATA': 'YOUR_VALUE_2'}}, {'thing': 'YOUR_THING', 'created': '2024-07-05T04:53:36.896Z', 'content': {'YOUR_DATA': 'YOUR_VALUE'}}]
```
</details>

### Asynchronous Programming

<details><summary>Code</summary>

```python
import asyncio
import basicdweet

async def async_test():
    print(await basicdweet.async_dweet_for("YOUR_THING", {"YOUR_DATA": "YOUR_VALUE"}))
    await asyncio.sleep(2)
    print(await basicdweet.async_get_latest_dweet_for("YOUR_THING"))
    await asyncio.sleep(2)
    print(await basicdweet.async_dweet_for("YOUR_THING", {"YOUR_DATA": "YOUR_VALUE_2"}))
    await asyncio.sleep(2)
    print(await basicdweet.async_get_latest_dweet_for("YOUR_THING"))
    await asyncio.sleep(2)
    print(await basicdweet.async_get_dweets_for("YOUR_THING"))

asyncio.run(async_test())
```
</details>

<details><summary>Output</summary>

```
{'thing': 'YOUR_THING', 'created': '2024-07-05T04:58:08.829Z', 'content': {'YOUR_DATA': 'YOUR_VALUE'}, 'transaction': '12d7e422-e8ce-408c-be0c-d61cc5d3d730'}
[{'thing': 'YOUR_THING', 'created': '2024-07-05T04:58:08.829Z', 'content': {'YOUR_DATA': 'YOUR_VALUE'}}]
{'thing': 'YOUR_THING', 'created': '2024-07-05T04:58:14.650Z', 'content': {'YOUR_DATA': 'YOUR_VALUE_2'}, 'transaction': 'ffbb2f4e-f954-4b4c-887e-7a492c0ce0ba'}
[{'thing': 'YOUR_THING', 'created': '2024-07-05T04:58:14.650Z', 'content': {'YOUR_DATA': 'YOUR_VALUE_2'}}]
[{'thing': 'YOUR_THING', 'created': '2024-07-05T04:58:14.650Z', 'content': {'YOUR_DATA': 'YOUR_VALUE_2'}}, {'thing': 'YOUR_THING', 'created': '2024-07-05T04:58:08.829Z', 'content': {'YOUR_DATA': 'YOUR_VALUE'}}]
```
</details>

## Test

```shell
python -m pytest
```

## Build documentation

```shell
mkdocs build
```
