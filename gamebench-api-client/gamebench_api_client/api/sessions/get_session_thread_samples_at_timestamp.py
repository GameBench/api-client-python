from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_session_thread_samples_at_timestamp_response_200_item import GetSessionThreadSamplesAtTimestampResponse200Item
from typing import cast



def _get_kwargs(
    session_id: str,
    ts: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/metrics/threads/{ts}".format(session_id=quote(str(session_id), safe=""),ts=quote(str(ts), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[GetSessionThreadSamplesAtTimestampResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GetSessionThreadSamplesAtTimestampResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    ts: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]]:
    """ Per-thread CPU samples at a specific timestamp

     Returns the per-thread CPU usage breakdown captured nearest
    to `{ts}` (a millisecond timestamp).

    Args:
        session_id (str):
        ts (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
ts=ts,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    ts: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | list[GetSessionThreadSamplesAtTimestampResponse200Item] | None:
    """ Per-thread CPU samples at a specific timestamp

     Returns the per-thread CPU usage breakdown captured nearest
    to `{ts}` (a millisecond timestamp).

    Args:
        session_id (str):
        ts (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]
     """


    return sync_detailed(
        session_id=session_id,
ts=ts,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    ts: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]]:
    """ Per-thread CPU samples at a specific timestamp

     Returns the per-thread CPU usage breakdown captured nearest
    to `{ts}` (a millisecond timestamp).

    Args:
        session_id (str):
        ts (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
ts=ts,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    ts: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | list[GetSessionThreadSamplesAtTimestampResponse200Item] | None:
    """ Per-thread CPU samples at a specific timestamp

     Returns the per-thread CPU usage breakdown captured nearest
    to `{ts}` (a millisecond timestamp).

    Args:
        session_id (str):
        ts (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GetSessionThreadSamplesAtTimestampResponse200Item]
     """


    return (await asyncio_detailed(
        session_id=session_id,
ts=ts,
client=client,

    )).parsed
