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
        "method": "get",
        "url": "/v2/sessions/{session_id}/download/logcat".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | str | None:
    if response.status_code == 200:
        response_200 = response.text
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | str]:
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

) -> Response[Any | Error | str]:
    """ Download a session's logcat file

     Streams the raw Android logcat capture for a session as
    `text/plain`. Requires the **`sessions.get`** permission —
    NOT `sessions.export`. Logcat is treated as part of viewing
    the session, so any caller who can read the session can
    download its log.

    Respects the caller's data scope; hidden sessions return 404,
    not 403.

    **Note — bare `Content-Disposition: attachment`, no filename.**
    Unlike the CSV / spreadsheet / zip exports, this route emits
    `Content-Disposition: attachment` with no `filename=` clause.
    The browser will pick a default filename (typically derived
    from the URL path, i.e. `logcat`).

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs, the server returns a **302
    redirect** to a signed URL instead of streaming bytes
    directly. Clients must follow redirects to download.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR the session has no associated logcat file
    (sessions can be captured without logcat).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | str]
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

) -> Any | Error | str | None:
    """ Download a session's logcat file

     Streams the raw Android logcat capture for a session as
    `text/plain`. Requires the **`sessions.get`** permission —
    NOT `sessions.export`. Logcat is treated as part of viewing
    the session, so any caller who can read the session can
    download its log.

    Respects the caller's data scope; hidden sessions return 404,
    not 403.

    **Note — bare `Content-Disposition: attachment`, no filename.**
    Unlike the CSV / spreadsheet / zip exports, this route emits
    `Content-Disposition: attachment` with no `filename=` clause.
    The browser will pick a default filename (typically derived
    from the URL path, i.e. `logcat`).

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs, the server returns a **302
    redirect** to a signed URL instead of streaming bytes
    directly. Clients must follow redirects to download.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR the session has no associated logcat file
    (sessions can be captured without logcat).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | str
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error | str]:
    """ Download a session's logcat file

     Streams the raw Android logcat capture for a session as
    `text/plain`. Requires the **`sessions.get`** permission —
    NOT `sessions.export`. Logcat is treated as part of viewing
    the session, so any caller who can read the session can
    download its log.

    Respects the caller's data scope; hidden sessions return 404,
    not 403.

    **Note — bare `Content-Disposition: attachment`, no filename.**
    Unlike the CSV / spreadsheet / zip exports, this route emits
    `Content-Disposition: attachment` with no `filename=` clause.
    The browser will pick a default filename (typically derived
    from the URL path, i.e. `logcat`).

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs, the server returns a **302
    redirect** to a signed URL instead of streaming bytes
    directly. Clients must follow redirects to download.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR the session has no associated logcat file
    (sessions can be captured without logcat).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | str]
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

) -> Any | Error | str | None:
    """ Download a session's logcat file

     Streams the raw Android logcat capture for a session as
    `text/plain`. Requires the **`sessions.get`** permission —
    NOT `sessions.export`. Logcat is treated as part of viewing
    the session, so any caller who can read the session can
    download its log.

    Respects the caller's data scope; hidden sessions return 404,
    not 403.

    **Note — bare `Content-Disposition: attachment`, no filename.**
    Unlike the CSV / spreadsheet / zip exports, this route emits
    `Content-Disposition: attachment` with no `filename=` clause.
    The browser will pick a default filename (typically derived
    from the URL path, i.e. `logcat`).

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs, the server returns a **302
    redirect** to a signed URL instead of streaming bytes
    directly. Clients must follow redirects to download.

    **404 cases:** session does not exist, caller's data scope
    hides it, OR the session has no associated logcat file
    (sessions can be captured without logcat).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | str
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
