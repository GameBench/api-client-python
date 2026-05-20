from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_session_latency_metric_response_200 import GetSessionLatencyMetricResponse200
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/metrics/latency".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetSessionLatencyMetricResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSessionLatencyMetricResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetSessionLatencyMetricResponse200]:
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

) -> Response[Error | GetSessionLatencyMetricResponse200]:
    r""" Touch / input latency samples with computed histogram + percentiles

     Returns the latency-sample series **plus** server-computed
    derived fields:

    - `samples`: filtered to only entries with `latency > 0`.
    - `histogram`: from `wink-statistics` over the filtered
      latency values.
    - `percentiles`: `{ \"95\": <ms>, \"99\": <ms> }` — note the keys
      are **string-number keys**, not nested under a property
      like `p95`.
    - `frametimesPercentiles`: spliced in from the parent session
      row, if present.

    Returns `200` with whatever the finder produces even when no
    samples exist (no 404 fallback). Clients should null-check
    `samples`.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionLatencyMetricResponse200]
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

) -> Error | GetSessionLatencyMetricResponse200 | None:
    r""" Touch / input latency samples with computed histogram + percentiles

     Returns the latency-sample series **plus** server-computed
    derived fields:

    - `samples`: filtered to only entries with `latency > 0`.
    - `histogram`: from `wink-statistics` over the filtered
      latency values.
    - `percentiles`: `{ \"95\": <ms>, \"99\": <ms> }` — note the keys
      are **string-number keys**, not nested under a property
      like `p95`.
    - `frametimesPercentiles`: spliced in from the parent session
      row, if present.

    Returns `200` with whatever the finder produces even when no
    samples exist (no 404 fallback). Clients should null-check
    `samples`.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionLatencyMetricResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetSessionLatencyMetricResponse200]:
    r""" Touch / input latency samples with computed histogram + percentiles

     Returns the latency-sample series **plus** server-computed
    derived fields:

    - `samples`: filtered to only entries with `latency > 0`.
    - `histogram`: from `wink-statistics` over the filtered
      latency values.
    - `percentiles`: `{ \"95\": <ms>, \"99\": <ms> }` — note the keys
      are **string-number keys**, not nested under a property
      like `p95`.
    - `frametimesPercentiles`: spliced in from the parent session
      row, if present.

    Returns `200` with whatever the finder produces even when no
    samples exist (no 404 fallback). Clients should null-check
    `samples`.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionLatencyMetricResponse200]
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

) -> Error | GetSessionLatencyMetricResponse200 | None:
    r""" Touch / input latency samples with computed histogram + percentiles

     Returns the latency-sample series **plus** server-computed
    derived fields:

    - `samples`: filtered to only entries with `latency > 0`.
    - `histogram`: from `wink-statistics` over the filtered
      latency values.
    - `percentiles`: `{ \"95\": <ms>, \"99\": <ms> }` — note the keys
      are **string-number keys**, not nested under a property
      like `p95`.
    - `frametimesPercentiles`: spliced in from the parent session
      row, if present.

    Returns `200` with whatever the finder produces even when no
    samples exist (no 404 fallback). Clients should null-check
    `samples`.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionLatencyMetricResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
