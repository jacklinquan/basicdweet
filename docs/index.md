# basicdweet
A python module for very basic APIs of the free dweet service.
Dweet is a simple machine-to-machine (M2M) service from [dweet.io](https://dweet.io).

This module only supports these dweet APIs of the free dweet service:

- `dweet for`
- `get latest dweet for`
- `get dweets for`

## Installation
`pip install basicdweet`

## Usage
``` python
>>> import basicdweet
>>> basicdweet.dweet_for('YOUR THING', {'YOUR DATA': 'YOUR VALUE'})
{'thing': 'YOUR THING', 'created': '2022-05-27T03:57:41.718Z', 'content': {'YOUR DATA': 'YOUR VALUE'}, 'transaction': 'da3d8f20-9b39-4d9a-aa06-2c1eebe0666f'}
>>> basicdweet.get_latest_dweet_for('YOUR THING')
[{'thing': 'YOUR THING', 'created': '2022-05-27T03:57:41.718Z', 'content': {'YOUR DATA': 'YOUR VALUE'}}]
>>> basicdweet.dweet_for('YOUR THING', {'YOUR DATA': 'YOUR VALUE 2'})
{'thing': 'YOUR THING', 'created': '2022-05-27T03:59:14.297Z', 'content': {'YOUR DATA': 'YOUR VALUE 2'}, 'transaction': 'e851fd9e-14c6-4d2b-847a-d9bf8402db18'}
>>> basicdweet.get_latest_dweet_for('YOUR THING')
[{'thing': 'YOUR THING', 'created': '2022-05-27T03:59:14.297Z', 'content': {'YOUR DATA': 'YOUR VALUE 2'}}]
>>> basicdweet.get_dweets_for('YOUR THING')
[{'thing': 'YOUR THING', 'created': '2022-05-27T03:59:14.297Z', 'content': {'YOUR DATA': 'YOUR VALUE 2'}}, {'thing': 'YOUR THING', 'created': '2022-05-27T03:57:41.718Z', 'content': {'YOUR DATA': 'YOUR VALUE'}}]
```
