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
        "method": "post",
        "url": "/v2/sessions/{session_id}/permanently-delete".format(session_id=quote(str(session_id), safe=""),),
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
    """ Mark a session for permanent (irreversible) deletion

     Begins permanent deletion of a session. The session row is
    immediately flagged with `isActive=false`,
    `markedForDeletion=true`, and `markedForDeletionAt=<now>`;
    the actual data purge — including backing files — is handed
    off to the asynchronous deletion queue. There is no
    re-activation path once this is called.

    **Distinct from `DELETE /v2/sessions/{sessionId}`.** That
    route is a soft delete (`isActive=false` only) and leaves
    backing files intact. This route is the irreversible one.

    **Admin-only.** Requires the `sessions.permanently-delete`
    permission. By default this is granted only to global-admins
    and company-admins of the session's owning company; it is
    intentionally absent from `company-session-editor`, all
    collection roles (`manager`, `editor`,
    `editor-own-data-only`, `viewer`), and the normal
    `sessions.delete` permission used by the soft-delete route.

    **Audit logging happens after deletion, not now.** No audit
    entry is written by this HTTP handler. The
    `SessionPermanentlyDeleted` action is written by the queue
    worker after it finishes the data purge, attributed to the
    calling user via the queued `userId`.

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
    """ Mark a session for permanent (irreversible) deletion

     Begins permanent deletion of a session. The session row is
    immediately flagged with `isActive=false`,
    `markedForDeletion=true`, and `markedForDeletionAt=<now>`;
    the actual data purge — including backing files — is handed
    off to the asynchronous deletion queue. There is no
    re-activation path once this is called.

    **Distinct from `DELETE /v2/sessions/{sessionId}`.** That
    route is a soft delete (`isActive=false` only) and leaves
    backing files intact. This route is the irreversible one.

    **Admin-only.** Requires the `sessions.permanently-delete`
    permission. By default this is granted only to global-admins
    and company-admins of the session's owning company; it is
    intentionally absent from `company-session-editor`, all
    collection roles (`manager`, `editor`,
    `editor-own-data-only`, `viewer`), and the normal
    `sessions.delete` permission used by the soft-delete route.

    **Audit logging happens after deletion, not now.** No audit
    entry is written by this HTTP handler. The
    `SessionPermanentlyDeleted` action is written by the queue
    worker after it finishes the data purge, attributed to the
    calling user via the queued `userId`.

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
    """ Mark a session for permanent (irreversible) deletion

     Begins permanent deletion of a session. The session row is
    immediately flagged with `isActive=false`,
    `markedForDeletion=true`, and `markedForDeletionAt=<now>`;
    the actual data purge — including backing files — is handed
    off to the asynchronous deletion queue. There is no
    re-activation path once this is called.

    **Distinct from `DELETE /v2/sessions/{sessionId}`.** That
    route is a soft delete (`isActive=false` only) and leaves
    backing files intact. This route is the irreversible one.

    **Admin-only.** Requires the `sessions.permanently-delete`
    permission. By default this is granted only to global-admins
    and company-admins of the session's owning company; it is
    intentionally absent from `company-session-editor`, all
    collection roles (`manager`, `editor`,
    `editor-own-data-only`, `viewer`), and the normal
    `sessions.delete` permission used by the soft-delete route.

    **Audit logging happens after deletion, not now.** No audit
    entry is written by this HTTP handler. The
    `SessionPermanentlyDeleted` action is written by the queue
    worker after it finishes the data purge, attributed to the
    calling user via the queued `userId`.

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
    """ Mark a session for permanent (irreversible) deletion

     Begins permanent deletion of a session. The session row is
    immediately flagged with `isActive=false`,
    `markedForDeletion=true`, and `markedForDeletionAt=<now>`;
    the actual data purge — including backing files — is handed
    off to the asynchronous deletion queue. There is no
    re-activation path once this is called.

    **Distinct from `DELETE /v2/sessions/{sessionId}`.** That
    route is a soft delete (`isActive=false` only) and leaves
    backing files intact. This route is the irreversible one.

    **Admin-only.** Requires the `sessions.permanently-delete`
    permission. By default this is granted only to global-admins
    and company-admins of the session's owning company; it is
    intentionally absent from `company-session-editor`, all
    collection roles (`manager`, `editor`,
    `editor-own-data-only`, `viewer`), and the normal
    `sessions.delete` permission used by the soft-delete route.

    **Audit logging happens after deletion, not now.** No audit
    entry is written by this HTTP handler. The
    `SessionPermanentlyDeleted` action is written by the queue
    worker after it finishes the data purge, attributed to the
    calling user via the queued `userId`.

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
