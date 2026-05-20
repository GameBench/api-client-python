from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.share_session_body import ShareSessionBody
from ...models.share_session_response_200 import ShareSessionResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: ShareSessionBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sessions/{session_id}/share".format(session_id=quote(str(session_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ShareSessionResponse200 | None:
    if response.status_code == 200:
        response_200 = ShareSessionResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ShareSessionResponse200]:
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
    body: ShareSessionBody | Unset = UNSET,

) -> Response[Error | ShareSessionResponse200]:
    """ Start sharing a session and mint a share link

     Sets the session's `isShared` flag to `true` and creates a new
    share link. Returns the link id and its expiry.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Each POST creates a new share link.** Calling this endpoint
    twice on the same session yields two distinct `shareId`s; the
    older one is not revoked. Use
    `GET /v2/sessions/{sessionId}/share-link` first if you want
    to reuse an existing link instead of creating another.

    Args:
        session_id (str):
        body (ShareSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ShareSessionResponse200]
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
    body: ShareSessionBody | Unset = UNSET,

) -> Error | ShareSessionResponse200 | None:
    """ Start sharing a session and mint a share link

     Sets the session's `isShared` flag to `true` and creates a new
    share link. Returns the link id and its expiry.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Each POST creates a new share link.** Calling this endpoint
    twice on the same session yields two distinct `shareId`s; the
    older one is not revoked. Use
    `GET /v2/sessions/{sessionId}/share-link` first if you want
    to reuse an existing link instead of creating another.

    Args:
        session_id (str):
        body (ShareSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ShareSessionResponse200
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
    body: ShareSessionBody | Unset = UNSET,

) -> Response[Error | ShareSessionResponse200]:
    """ Start sharing a session and mint a share link

     Sets the session's `isShared` flag to `true` and creates a new
    share link. Returns the link id and its expiry.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Each POST creates a new share link.** Calling this endpoint
    twice on the same session yields two distinct `shareId`s; the
    older one is not revoked. Use
    `GET /v2/sessions/{sessionId}/share-link` first if you want
    to reuse an existing link instead of creating another.

    Args:
        session_id (str):
        body (ShareSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ShareSessionResponse200]
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
    body: ShareSessionBody | Unset = UNSET,

) -> Error | ShareSessionResponse200 | None:
    """ Start sharing a session and mint a share link

     Sets the session's `isShared` flag to `true` and creates a new
    share link. Returns the link id and its expiry.

    Requires the `sessions.share` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Each POST creates a new share link.** Calling this endpoint
    twice on the same session yields two distinct `shareId`s; the
    older one is not revoked. Use
    `GET /v2/sessions/{sessionId}/share-link` first if you want
    to reuse an existing link instead of creating another.

    Args:
        session_id (str):
        body (ShareSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ShareSessionResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
