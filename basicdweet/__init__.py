"""A python module for very basic APIs of the free dweet service.

- Author: Quan Lin
- License: MIT
"""

__version__ = "0.3.0"
__all__ = ["BasicDweetError", "dweet_for", "get_latest_dweet_for", "get_dweets_for"]

import json

try:
    import urequests as requests
except ImportError:
    import requests

BASE_URL = "https://dweet.io"


class BasicDweetError(Exception):
    pass


def _request(method, url, base_url=BASE_URL, **kwargs):
    url = base_url.rstrip("/") + "/" + url.lstrip("/")

    request_func = getattr(requests, method)
    response = request_func(url, **kwargs)
    if not (200 <= response.status_code < 300):
        raise BasicDweetError(f"HTTP {response.status_code} response")
    response_json = response.json()
    if response_json["this"] == "failed":
        raise BasicDweetError(response_json["because"])
    return response_json["with"]


def dweet_for(thing_name, payload, base_url=BASE_URL, **kwargs):
    """The `dweet for` API.

    Parameters
    ----------
    thing_name : str
        The name of the thing to dweet.
    payload : dict
        The content of the thing to dweet.
        It is passed to `json.dumps`. So a dict fits it the best.
    base_url : str, optional
        The base url of the dweet server.
        (default is "https://dweet.io")

    Returns
    -------
    dict
        The dweet transaction dict returned from dweet service.
        It should include the keys of 'thing', 'content', 'created' and 'transaction'.
    """
    kwargs["data"] = json.dumps(payload)
    kwargs.setdefault("headers", {})
    kwargs["headers"].update({"Content-Type": "application/json"})
    return _request(
        "post",
        f"/dweet/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


def get_latest_dweet_for(thing_name, base_url=BASE_URL, **kwargs):
    """The `get latest dweet for` API.

    Parameters
    ----------
    thing_name : str
        The name of the thing to dweet.
    base_url : str, optional
        The base url of the dweet server.
        (default is "https://dweet.io")

    Returns
    -------
    list
        The list of dweet transaction dicts.
        There is only the latest transaction dict in it.
    """
    return _request(
        "get",
        f"/get/latest/dweet/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


def get_dweets_for(thing_name, base_url=BASE_URL, **kwargs):
    """The `get dweets for` API.

    Parameters
    ----------
    thing_name : str
        The name of the thing to dweet.
    base_url : str, optional
        The base url of the dweet server.
        (default is "https://dweet.io")

    Returns
    -------
    list
        The list of dweet transaction dicts.
        There are at most 5 latest transaction dicts in it.
    """
    return _request(
        "get",
        f"/get/dweets/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )
