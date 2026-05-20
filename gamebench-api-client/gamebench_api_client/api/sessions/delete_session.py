from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/sessions/{session_id}".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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

) -> Response[Any | Error]:
    """ Soft-delete a session

     **Soft delete.** The server sets `isActive = false` on the
    session row; the session is hidden from subsequent list/get
    endpoints but the underlying row and backing files (zip
    backup, screenshots, frametimes, etc.) are retained. There is
    no public re-activation endpoint.

    A `SessionDeactivated` entry is written to the audit log,
    attributed to the calling user.

    Requires the `sessions.delete` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Same behavior as `GET /v2/sessions/{sessionId}`: callers
    restricted to their own data receive 404 (not 403) when the
    session belongs to another user.

    Calling DELETE on an already-deactivated session is currently
    accepted (the row is rewritten with `isActive = false` and a
    new audit-log entry is written). Clients should not rely on
    this — treat it as idempotent in intent only.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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

) -> Any | Error | None:
    """ Soft-delete a session

     **Soft delete.** The server sets `isActive = false` on the
    session row; the session is hidden from subsequent list/get
    endpoints but the underlying row and backing files (zip
    backup, screenshots, frametimes, etc.) are retained. There is
    no public re-activation endpoint.

    A `SessionDeactivated` entry is written to the audit log,
    attributed to the calling user.

    Requires the `sessions.delete` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Same behavior as `GET /v2/sessions/{sessionId}`: callers
    restricted to their own data receive 404 (not 403) when the
    session belongs to another user.

    Calling DELETE on an already-deactivated session is currently
    accepted (the row is rewritten with `isActive = false` and a
    new audit-log entry is written). Clients should not rely on
    this — treat it as idempotent in intent only.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error]:
    """ Soft-delete a session

     **Soft delete.** The server sets `isActive = false` on the
    session row; the session is hidden from subsequent list/get
    endpoints but the underlying row and backing files (zip
    backup, screenshots, frametimes, etc.) are retained. There is
    no public re-activation endpoint.

    A `SessionDeactivated` entry is written to the audit log,
    attributed to the calling user.

    Requires the `sessions.delete` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Same behavior as `GET /v2/sessions/{sessionId}`: callers
    restricted to their own data receive 404 (not 403) when the
    session belongs to another user.

    Calling DELETE on an already-deactivated session is currently
    accepted (the row is rewritten with `isActive = false` and a
    new audit-log entry is written). Clients should not rely on
    this — treat it as idempotent in intent only.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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

) -> Any | Error | None:
    """ Soft-delete a session

     **Soft delete.** The server sets `isActive = false` on the
    session row; the session is hidden from subsequent list/get
    endpoints but the underlying row and backing files (zip
    backup, screenshots, frametimes, etc.) are retained. There is
    no public re-activation endpoint.

    A `SessionDeactivated` entry is written to the audit log,
    attributed to the calling user.

    Requires the `sessions.delete` permission on the session's
    collection / company.

    **404 is also returned for sessions hidden by data scope.**
    Same behavior as `GET /v2/sessions/{sessionId}`: callers
    restricted to their own data receive 404 (not 403) when the
    session belongs to another user.

    Calling DELETE on an already-deactivated session is currently
    accepted (the row is rewritten with `isActive = false` and a
    new audit-log entry is written). Clients should not rely on
    this — treat it as idempotent in intent only.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
