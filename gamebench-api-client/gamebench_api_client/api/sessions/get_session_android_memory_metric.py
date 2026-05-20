from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_session_android_memory_metric_response_200 import GetSessionAndroidMemoryMetricResponse200
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/metrics/android-memory".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetSessionAndroidMemoryMetricResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSessionAndroidMemoryMetricResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetSessionAndroidMemoryMetricResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetSessionAndroidMemoryMetricResponse200]:
    """ Android-specific memory metric samples

     Android-specific memory samples (private dirty, proportional
    set size, etc.). Returns 404 if none.

    **`usage` may be computed on-demand.** If the response's
    `usage` block (`min` / `max` / `avg` / `median` of
    `totalUsage`) is not cached, the server computes it from the
    samples at request time. The computed values are not
    guaranteed to be bit-stable across calls.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionAndroidMemoryMetricResponse200]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetSessionAndroidMemoryMetricResponse200 | None:
    """ Android-specific memory metric samples

     Android-specific memory samples (private dirty, proportional
    set size, etc.). Returns 404 if none.

    **`usage` may be computed on-demand.** If the response's
    `usage` block (`min` / `max` / `avg` / `median` of
    `totalUsage`) is not cached, the server computes it from the
    samples at request time. The computed values are not
    guaranteed to be bit-stable across calls.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionAndroidMemoryMetricResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetSessionAndroidMemoryMetricResponse200]:
    """ Android-specific memory metric samples

     Android-specific memory samples (private dirty, proportional
    set size, etc.). Returns 404 if none.

    **`usage` may be computed on-demand.** If the response's
    `usage` block (`min` / `max` / `avg` / `median` of
    `totalUsage`) is not cached, the server computes it from the
    samples at request time. The computed values are not
    guaranteed to be bit-stable across calls.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionAndroidMemoryMetricResponse200]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetSessionAndroidMemoryMetricResponse200 | None:
    """ Android-specific memory metric samples

     Android-specific memory samples (private dirty, proportional
    set size, etc.). Returns 404 if none.

    **`usage` may be computed on-demand.** If the response's
    `usage` block (`min` / `max` / `avg` / `median` of
    `totalUsage`) is not cached, the server computes it from the
    samples at request time. The computed values are not
    guaranteed to be bit-stable across calls.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionAndroidMemoryMetricResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
