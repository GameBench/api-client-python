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
    session_ids: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sessions/unshare/sessions/{session_ids}".format(session_ids=quote(str(session_ids), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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
    session_ids: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error]:
    """ Unshare multiple sessions in one request

     Sets `isShared = false` and deletes share links for every
    requested session. Counterpart to
    `POST /v2/sessions/{sessionId}/unshare` for batch use.

    `{sessionIds}` is a comma-separated path segment, e.g.
    `/v2/sessions/unshare/sessions/abc,def,ghi`. There is no
    request body.

    Requires the `sessions.share` permission on every requested
    session's collection / company, and the caller's data scope
    is enforced per session. If any session in the batch fails
    either check, the entire request fails with 400.

    **400 cases:** zero sessions resolved, OR any requested
    session is hidden from the caller by data scope or
    permission.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        session_ids=session_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_ids: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | Error | None:
    """ Unshare multiple sessions in one request

     Sets `isShared = false` and deletes share links for every
    requested session. Counterpart to
    `POST /v2/sessions/{sessionId}/unshare` for batch use.

    `{sessionIds}` is a comma-separated path segment, e.g.
    `/v2/sessions/unshare/sessions/abc,def,ghi`. There is no
    request body.

    Requires the `sessions.share` permission on every requested
    session's collection / company, and the caller's data scope
    is enforced per session. If any session in the batch fails
    either check, the entire request fails with 400.

    **400 cases:** zero sessions resolved, OR any requested
    session is hidden from the caller by data scope or
    permission.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        session_ids=session_ids,
client=client,

    ).parsed

async def asyncio_detailed(
    session_ids: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error]:
    """ Unshare multiple sessions in one request

     Sets `isShared = false` and deletes share links for every
    requested session. Counterpart to
    `POST /v2/sessions/{sessionId}/unshare` for batch use.

    `{sessionIds}` is a comma-separated path segment, e.g.
    `/v2/sessions/unshare/sessions/abc,def,ghi`. There is no
    request body.

    Requires the `sessions.share` permission on every requested
    session's collection / company, and the caller's data scope
    is enforced per session. If any session in the batch fails
    either check, the entire request fails with 400.

    **400 cases:** zero sessions resolved, OR any requested
    session is hidden from the caller by data scope or
    permission.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        session_ids=session_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_ids: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | Error | None:
    """ Unshare multiple sessions in one request

     Sets `isShared = false` and deletes share links for every
    requested session. Counterpart to
    `POST /v2/sessions/{sessionId}/unshare` for batch use.

    `{sessionIds}` is a comma-separated path segment, e.g.
    `/v2/sessions/unshare/sessions/abc,def,ghi`. There is no
    request body.

    Requires the `sessions.share` permission on every requested
    session's collection / company, and the caller's data scope
    is enforced per session. If any session in the batch fails
    either check, the entire request fails with 400.

    **400 cases:** zero sessions resolved, OR any requested
    session is hidden from the caller by data scope or
    permission.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        session_ids=session_ids,
client=client,

    )).parsed
