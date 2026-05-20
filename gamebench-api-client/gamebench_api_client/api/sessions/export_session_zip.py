from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...types import File, FileTypes
from io import BytesIO
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/export/zip".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | File | None:
    if response.status_code == 200:
        response_200 = File(
             payload = BytesIO(response.content)
        )



        return response_200

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | File]:
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

) -> Response[Any | Error | File]:
    """ Download a single session's backup zip

     Streams a single session's backup zip back to the caller. The
    single-session counterpart to
    `GET /v2/sessions/export/sessions/{sessionIds}` — useful when
    the caller only wants one session and wants to avoid the
    comma-list-in-path encoding.

    Requires the `sessions.export` permission and respects the
    caller's data scope (same checks as the sibling CSV /
    spreadsheet exports). Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.zip`,
    delivered via `Content-Disposition: attachment`.

    **Backing storage / redirect behavior.** The server prefers a
    local backup file on disk if present. Otherwise it falls back
    to the session's `zipBackupFile` in object storage and may
    issue a **302 redirect to a signed URL** instead of streaming
    the bytes itself. Clients must follow redirects to download
    the zip.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR no backup file is available (neither on disk nor
    in object storage).

    **Side effect:** the session is marked `exported = true`
    before the response is sent. Unlike the batch endpoint, this
    flag is set whether or not the client successfully completes
    the download.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | File]
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

) -> Any | Error | File | None:
    """ Download a single session's backup zip

     Streams a single session's backup zip back to the caller. The
    single-session counterpart to
    `GET /v2/sessions/export/sessions/{sessionIds}` — useful when
    the caller only wants one session and wants to avoid the
    comma-list-in-path encoding.

    Requires the `sessions.export` permission and respects the
    caller's data scope (same checks as the sibling CSV /
    spreadsheet exports). Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.zip`,
    delivered via `Content-Disposition: attachment`.

    **Backing storage / redirect behavior.** The server prefers a
    local backup file on disk if present. Otherwise it falls back
    to the session's `zipBackupFile` in object storage and may
    issue a **302 redirect to a signed URL** instead of streaming
    the bytes itself. Clients must follow redirects to download
    the zip.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR no backup file is available (neither on disk nor
    in object storage).

    **Side effect:** the session is marked `exported = true`
    before the response is sent. Unlike the batch endpoint, this
    flag is set whether or not the client successfully completes
    the download.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | File
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error | File]:
    """ Download a single session's backup zip

     Streams a single session's backup zip back to the caller. The
    single-session counterpart to
    `GET /v2/sessions/export/sessions/{sessionIds}` — useful when
    the caller only wants one session and wants to avoid the
    comma-list-in-path encoding.

    Requires the `sessions.export` permission and respects the
    caller's data scope (same checks as the sibling CSV /
    spreadsheet exports). Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.zip`,
    delivered via `Content-Disposition: attachment`.

    **Backing storage / redirect behavior.** The server prefers a
    local backup file on disk if present. Otherwise it falls back
    to the session's `zipBackupFile` in object storage and may
    issue a **302 redirect to a signed URL** instead of streaming
    the bytes itself. Clients must follow redirects to download
    the zip.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR no backup file is available (neither on disk nor
    in object storage).

    **Side effect:** the session is marked `exported = true`
    before the response is sent. Unlike the batch endpoint, this
    flag is set whether or not the client successfully completes
    the download.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | File]
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

) -> Any | Error | File | None:
    """ Download a single session's backup zip

     Streams a single session's backup zip back to the caller. The
    single-session counterpart to
    `GET /v2/sessions/export/sessions/{sessionIds}` — useful when
    the caller only wants one session and wants to avoid the
    comma-list-in-path encoding.

    Requires the `sessions.export` permission and respects the
    caller's data scope (same checks as the sibling CSV /
    spreadsheet exports). Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.zip`,
    delivered via `Content-Disposition: attachment`.

    **Backing storage / redirect behavior.** The server prefers a
    local backup file on disk if present. Otherwise it falls back
    to the session's `zipBackupFile` in object storage and may
    issue a **302 redirect to a signed URL** instead of streaming
    the bytes itself. Clients must follow redirects to download
    the zip.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR no backup file is available (neither on disk nor
    in object storage).

    **Side effect:** the session is marked `exported = true`
    before the response is sent. Unlike the batch endpoint, this
    flag is set whether or not the client successfully completes
    the download.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | File
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
