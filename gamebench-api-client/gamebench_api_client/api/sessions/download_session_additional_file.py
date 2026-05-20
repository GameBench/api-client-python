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
    filename: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/additional-files/{filename}".format(session_id=quote(str(session_id), safe=""),filename=quote(str(filename), safe=""),),
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
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error | File]:
    """ Download a single additional file by name

     Streams (or redirects to) the named additional file for a
    session. The `{filename}` segment must exactly match the
    `filename` field of one of the entries returned by the list
    route — matching is exact, not normalised.

    Requires the `sessions.get` permission and respects the
    caller's data scope.

    **Content-Type comes verbatim from the stored entry's
    `type`.** That value is captured at upload time and not
    validated. Clients should not trust it absolutely.

    **`Content-Disposition` echoes the URL-decoded filename**
    without any quoting or escaping, e.g.
    `attachment; filename=<filename>`. Filenames containing
    whitespace, commas, semicolons or non-ASCII characters can
    produce header values that some clients parse loosely. The
    underlying data stays correct; only the display filename
    suffers.

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs the server returns a **302
    redirect** to a signed URL. Clients must follow.

    **404 cases:** session does not exist, caller's data scope
    hides it, the session has no additional files at all, the
    named file is not present in the session's list, OR the
    entry's storage handle is missing.

    Args:
        session_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | File]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
filename=filename,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | Error | File | None:
    """ Download a single additional file by name

     Streams (or redirects to) the named additional file for a
    session. The `{filename}` segment must exactly match the
    `filename` field of one of the entries returned by the list
    route — matching is exact, not normalised.

    Requires the `sessions.get` permission and respects the
    caller's data scope.

    **Content-Type comes verbatim from the stored entry's
    `type`.** That value is captured at upload time and not
    validated. Clients should not trust it absolutely.

    **`Content-Disposition` echoes the URL-decoded filename**
    without any quoting or escaping, e.g.
    `attachment; filename=<filename>`. Filenames containing
    whitespace, commas, semicolons or non-ASCII characters can
    produce header values that some clients parse loosely. The
    underlying data stays correct; only the display filename
    suffers.

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs the server returns a **302
    redirect** to a signed URL. Clients must follow.

    **404 cases:** session does not exist, caller's data scope
    hides it, the session has no additional files at all, the
    named file is not present in the session's list, OR the
    entry's storage handle is missing.

    Args:
        session_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | File
     """


    return sync_detailed(
        session_id=session_id,
filename=filename,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error | File]:
    """ Download a single additional file by name

     Streams (or redirects to) the named additional file for a
    session. The `{filename}` segment must exactly match the
    `filename` field of one of the entries returned by the list
    route — matching is exact, not normalised.

    Requires the `sessions.get` permission and respects the
    caller's data scope.

    **Content-Type comes verbatim from the stored entry's
    `type`.** That value is captured at upload time and not
    validated. Clients should not trust it absolutely.

    **`Content-Disposition` echoes the URL-decoded filename**
    without any quoting or escaping, e.g.
    `attachment; filename=<filename>`. Filenames containing
    whitespace, commas, semicolons or non-ASCII characters can
    produce header values that some clients parse loosely. The
    underlying data stays correct; only the display filename
    suffers.

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs the server returns a **302
    redirect** to a signed URL. Clients must follow.

    **404 cases:** session does not exist, caller's data scope
    hides it, the session has no additional files at all, the
    named file is not present in the session's list, OR the
    entry's storage handle is missing.

    Args:
        session_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | File]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
filename=filename,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | Error | File | None:
    """ Download a single additional file by name

     Streams (or redirects to) the named additional file for a
    session. The `{filename}` segment must exactly match the
    `filename` field of one of the entries returned by the list
    route — matching is exact, not normalised.

    Requires the `sessions.get` permission and respects the
    caller's data scope.

    **Content-Type comes verbatim from the stored entry's
    `type`.** That value is captured at upload time and not
    validated. Clients should not trust it absolutely.

    **`Content-Disposition` echoes the URL-decoded filename**
    without any quoting or escaping, e.g.
    `attachment; filename=<filename>`. Filenames containing
    whitespace, commas, semicolons or non-ASCII characters can
    produce header values that some clients parse loosely. The
    underlying data stays correct; only the display filename
    suffers.

    **Backing storage / redirect behavior.** When the file-storage
    backend supports signed URLs the server returns a **302
    redirect** to a signed URL. Clients must follow.

    **404 cases:** session does not exist, caller's data scope
    hides it, the session has no additional files at all, the
    named file is not present in the session's list, OR the
    entry's storage handle is missing.

    Args:
        session_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | File
     """


    return (await asyncio_detailed(
        session_id=session_id,
filename=filename,
client=client,

    )).parsed
