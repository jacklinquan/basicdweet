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
```python
>>> import basicdweet
>>> basicdweet.dweet_for('YOUR_THING', {'YOUR_DATA': 'YOUR_VALUE'})
{'content': {'YOUR_DATA': 'YOUR_VALUE'}, 'created': '2022-05-27T06:17:48.127Z', 'thing': 'YOUR_THING', 'transaction': '403dcd2b-99b9-44b4-b864-b682b898ac10'}
>>> basicdweet.get_latest_dweet_for('YOUR_THING')
[{'content': {'YOUR_DATA': 'YOUR_VALUE'}, 'created': '2022-05-27T06:17:48.127Z', 'thing': 'YOUR_THING'}]
>>> basicdweet.dweet_for('YOUR_THING', {'YOUR_DATA': 'YOUR_VALUE_2'})
{'content': {'YOUR_DATA': 'YOUR_VALUE_2'}, 'created': '2022-05-27T06:19:08.081Z', 'thing': 'YOUR_THING', 'transaction': '30cdc5b8-5da9-40ac-86a9-ea0df5ef8317'}
>>> basicdweet.get_latest_dweet_for('YOUR_THING')
[{'content': {'YOUR_DATA': 'YOUR_VALUE_2'}, 'created': '2022-05-27T06:19:08.081Z', 'thing': 'YOUR_THING'}]
>>> basicdweet.get_dweets_for('YOUR_THING')
[{'content': {'YOUR_DATA': 'YOUR_VALUE_2'}, 'created': '2022-05-27T06:19:08.081Z', 'thing': 'YOUR_THING'}, {'content': {'YOUR_DATA': 'YOUR_VALUE'}, 'created': '2022-05-27T06:17:48.127Z', 'thing': 'YOUR_THING'}]
```
