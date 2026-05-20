from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.unshare_session_response_200 import UnshareSessionResponse200
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sessions/{session_id}/unshare".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UnshareSessionResponse200 | None:
    if response.status_code == 200:
        response_200 = UnshareSessionResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UnshareSessionResponse200]:
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

) -> Response[Error | UnshareSessionResponse200]:
    """ Stop sharing a session and delete all its share links

     Sets the session's `isShared` flag to `false` and deletes
    **all** share links for the session (not just one — there is
    no per-link revoke).

    Requires the `sessions.share` permission and respects the
    caller's data scope.

    **Returns 404 for inactive (soft-deleted) sessions.** In
    addition to the usual 404 cases (does not exist, hidden by
    data scope).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnshareSessionResponse200]
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

) -> Error | UnshareSessionResponse200 | None:
    """ Stop sharing a session and delete all its share links

     Sets the session's `isShared` flag to `false` and deletes
    **all** share links for the session (not just one — there is
    no per-link revoke).

    Requires the `sessions.share` permission and respects the
    caller's data scope.

    **Returns 404 for inactive (soft-deleted) sessions.** In
    addition to the usual 404 cases (does not exist, hidden by
    data scope).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnshareSessionResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | UnshareSessionResponse200]:
    """ Stop sharing a session and delete all its share links

     Sets the session's `isShared` flag to `false` and deletes
    **all** share links for the session (not just one — there is
    no per-link revoke).

    Requires the `sessions.share` permission and respects the
    caller's data scope.

    **Returns 404 for inactive (soft-deleted) sessions.** In
    addition to the usual 404 cases (does not exist, hidden by
    data scope).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnshareSessionResponse200]
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

) -> Error | UnshareSessionResponse200 | None:
    """ Stop sharing a session and delete all its share links

     Sets the session's `isShared` flag to `false` and deletes
    **all** share links for the session (not just one — there is
    no per-link revoke).

    Requires the `sessions.share` permission and respects the
    caller's data scope.

    **Returns 404 for inactive (soft-deleted) sessions.** In
    addition to the usual 404 cases (does not exist, hidden by
    data scope).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnshareSessionResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
