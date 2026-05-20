from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_session_share_link_body import UpdateSessionShareLinkBody
from ...models.update_session_share_link_response_200 import UpdateSessionShareLinkResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: UpdateSessionShareLinkBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/sessions/{session_id}/share-link".format(session_id=quote(str(session_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateSessionShareLinkResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateSessionShareLinkResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateSessionShareLinkResponse200]:
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
    body: UpdateSessionShareLinkBody | Unset = UNSET,

) -> Response[Error | UpdateSessionShareLinkResponse200]:
    """ Update the expiry of a session's share link

     Mutates the expiry of the session's share link. Returns the
    updated link.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Passing `null` (or omitting `expiresAt`) sets the link to
    never expire.

    **Does NOT toggle `isShared`.** Updating expiry alone leaves
    the session's `isShared` flag unchanged. Use `/share` or
    `/unshare` to flip that flag.

    Args:
        session_id (str):
        body (UpdateSessionShareLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateSessionShareLinkResponse200]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSessionShareLinkBody | Unset = UNSET,

) -> Error | UpdateSessionShareLinkResponse200 | None:
    """ Update the expiry of a session's share link

     Mutates the expiry of the session's share link. Returns the
    updated link.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Passing `null` (or omitting `expiresAt`) sets the link to
    never expire.

    **Does NOT toggle `isShared`.** Updating expiry alone leaves
    the session's `isShared` flag unchanged. Use `/share` or
    `/unshare` to flip that flag.

    Args:
        session_id (str):
        body (UpdateSessionShareLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateSessionShareLinkResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSessionShareLinkBody | Unset = UNSET,

) -> Response[Error | UpdateSessionShareLinkResponse200]:
    """ Update the expiry of a session's share link

     Mutates the expiry of the session's share link. Returns the
    updated link.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Passing `null` (or omitting `expiresAt`) sets the link to
    never expire.

    **Does NOT toggle `isShared`.** Updating expiry alone leaves
    the session's `isShared` flag unchanged. Use `/share` or
    `/unshare` to flip that flag.

    Args:
        session_id (str):
        body (UpdateSessionShareLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateSessionShareLinkResponse200]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSessionShareLinkBody | Unset = UNSET,

) -> Error | UpdateSessionShareLinkResponse200 | None:
    """ Update the expiry of a session's share link

     Mutates the expiry of the session's share link. Returns the
    updated link.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Passing `null` (or omitting `expiresAt`) sets the link to
    never expire.

    **Does NOT toggle `isShared`.** Updating expiry alone leaves
    the session's `isShared` flag unchanged. Use `/share` or
    `/unshare` to flip that flag.

    Args:
        session_id (str):
        body (UpdateSessionShareLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateSessionShareLinkResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
