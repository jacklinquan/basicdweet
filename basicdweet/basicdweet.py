import json

try:
    # Only needed for synchronous programming
    import requests
except ImportError:
    pass

try:
    # Only needed for asynchronous programming
    import aiohttp
except ImportError:
    pass

__version__ = "0.4.0"

DEFAULT_BASE_URL = "https://dweet.io"


class BasicDweetError(Exception):
    pass


def _request(
    method: str,
    api_url: str,
    base_url: str,
    **kwargs,
) -> object:
    request_func = getattr(requests, method)
    full_url = base_url.rstrip("/") + "/" + api_url.lstrip("/")
    response = request_func(full_url, **kwargs)
    if not (200 <= response.status_code < 300):
        raise BasicDweetError(f"HTTP {response.status_code} response")
    response_json = response.json()
    if response_json["this"] == "failed":
        raise BasicDweetError(response_json["because"])
    return response_json["with"]


def dweet_for(
    thing_name: str,
    payload: dict,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs,
) -> dict:
    """The `dweet for` API.

    Args:
        thing_name:
            The name of the thing to dweet.
        payload:
            The content of the thing to dweet.
            It is passed to `json.dumps`. So a dict fits it the best.
        base_url:
            The base url of the dweet server.
            (default is "https://dweet.io")

    Returns:
        The dweet transaction dict returned from dweet service.
        It should include the keys of `thing`, `content`, `created` and `transaction`.
    """
    kwargs["data"] = json.dumps(payload)
    kwargs.setdefault("headers", {})
    kwargs["headers"].update({"Content-Type": "application/json"})
    return _request(
        "post",
        api_url=f"/dweet/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


def get_latest_dweet_for(
    thing_name: str,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs,
) -> list:
    """The `get latest dweet for` API.

    Args:
        thing_name:
            The name of the thing to dweet.
        base_url:
            The base url of the dweet server.
            (default is "https://dweet.io")

    Returns:
        The list of dweet transaction dicts.
        There is only the latest transaction dict in it.
    """
    return _request(
        "get",
        api_url=f"/get/latest/dweet/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


def get_dweets_for(
    thing_name: str,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs,
) -> list:
    """The `get dweets for` API.

    Args:
        thing_name:
            The name of the thing to dweet.
        base_url:
            The base url of the dweet server.
            (default is "https://dweet.io")

    Returns:
        The list of dweet transaction dicts.
        There are a few the latest transaction dicts in it.
    """
    return _request(
        "get",
        api_url=f"/get/dweets/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


async def _async_request(
    method: str,
    api_url: str,
    base_url: str,
    **kwargs,
):
    full_url = base_url.rstrip("/") + "/" + api_url.lstrip("/")
    async with aiohttp.ClientSession() as session:
        async with session.request(method.upper(), full_url, **kwargs) as response:
            if not (200 <= response.status < 300):
                raise BasicDweetError(f"HTTP {response.status} response")
            response_json = await response.json()
            if response_json["this"] == "failed":
                raise BasicDweetError(response_json["because"])
    return response_json["with"]


async def async_dweet_for(
    thing_name: str,
    payload: dict,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs,
) -> dict:
    """The async `dweet for` API.

    The arguments have the same meaning as in `dweet_for`.
    """
    kwargs["data"] = json.dumps(payload)
    kwargs.setdefault("headers", {})
    kwargs["headers"].update({"Content-Type": "application/json"})
    return await _async_request(
        "post",
        api_url=f"/dweet/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


async def async_get_latest_dweet_for(
    thing_name: str,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs,
) -> list:
    """The async `get latest dweet for` API.

    The arguments have the same meaning as in `get_latest_dweet_for`.
    """
    return await _async_request(
        "get",
        api_url=f"/get/latest/dweet/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )


async def async_get_dweets_for(
    thing_name: str,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs,
) -> list:
    """The async `get dweets for` API.

    The arguments have the same meaning as in `get_dweets_for`.
    """
    return await _async_request(
        "get",
        api_url=f"/get/dweets/for/{thing_name}",
        base_url=base_url,
        **kwargs,
    )
