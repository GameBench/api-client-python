from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_session_response_200 import GetSessionResponse200
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetSessionResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSessionResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetSessionResponse200]:
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

) -> Response[Error | GetSessionResponse200]:
    r""" Fetch a single session by id

     Returns the full session document, with an extra `url` field
    appended server-side that points to the dashboard summary page
    for this session.

    Requires the `sessions.get` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Callers whose data scope is restricted to their own data (e.g.
    `editor-own-data-only`) receive a 404 — not a 403 — when the
    session belongs to another user. Treat 404 as \"unknown or
    hidden\", not as proof of non-existence.

    The response body is the raw session object: dozens of
    top-level fields covering app, device, user, metrics (fps,
    cpu, gpu, mem, power, latency), timing, location, tags,
    markersSummary, etc. Only the most stable fields are listed
    here; consumers should treat the object as open.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionResponse200]
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

) -> Error | GetSessionResponse200 | None:
    r""" Fetch a single session by id

     Returns the full session document, with an extra `url` field
    appended server-side that points to the dashboard summary page
    for this session.

    Requires the `sessions.get` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Callers whose data scope is restricted to their own data (e.g.
    `editor-own-data-only`) receive a 404 — not a 403 — when the
    session belongs to another user. Treat 404 as \"unknown or
    hidden\", not as proof of non-existence.

    The response body is the raw session object: dozens of
    top-level fields covering app, device, user, metrics (fps,
    cpu, gpu, mem, power, latency), timing, location, tags,
    markersSummary, etc. Only the most stable fields are listed
    here; consumers should treat the object as open.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetSessionResponse200]:
    r""" Fetch a single session by id

     Returns the full session document, with an extra `url` field
    appended server-side that points to the dashboard summary page
    for this session.

    Requires the `sessions.get` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Callers whose data scope is restricted to their own data (e.g.
    `editor-own-data-only`) receive a 404 — not a 403 — when the
    session belongs to another user. Treat 404 as \"unknown or
    hidden\", not as proof of non-existence.

    The response body is the raw session object: dozens of
    top-level fields covering app, device, user, metrics (fps,
    cpu, gpu, mem, power, latency), timing, location, tags,
    markersSummary, etc. Only the most stable fields are listed
    here; consumers should treat the object as open.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionResponse200]
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

) -> Error | GetSessionResponse200 | None:
    r""" Fetch a single session by id

     Returns the full session document, with an extra `url` field
    appended server-side that points to the dashboard summary page
    for this session.

    Requires the `sessions.get` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Callers whose data scope is restricted to their own data (e.g.
    `editor-own-data-only`) receive a 404 — not a 403 — when the
    session belongs to another user. Treat 404 as \"unknown or
    hidden\", not as proof of non-existence.

    The response body is the raw session object: dozens of
    top-level fields covering app, device, user, metrics (fps,
    cpu, gpu, mem, power, latency), timing, location, tags,
    markersSummary, etc. Only the most stable fields are listed
    here; consumers should treat the object as open.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
