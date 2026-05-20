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
    session_ids: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/export/sessions/{session_ids}".format(session_ids=quote(str(session_ids), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | File | None:
    if response.status_code == 200:
        response_200 = File(
             payload = BytesIO(response.content)
        )



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | File]:
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

) -> Response[Error | File]:
    """ Download a zip archive of one or more session backups

     Bundles the original `zipBackupFile` for each requested
    session into a single zip and streams it back as an
    `application/octet-stream` attachment.

    **`{sessionIds}` is a comma-separated list inside the URL
    path.** Example: `/v2/sessions/export/sessions/abc,def,ghi`.
    There is no request body. Beware URL-length limits when
    exporting many sessions at once; use
    `POST /v2/sessions/export/check` first to validate the set
    and confirm total size is under the server's export size cap
    (this endpoint does not check size — only `/export/check`
    does).

    Requires the `sessions.export` permission on every requested
    session's collection / company. The caller's data scope is
    also enforced per session: callers restricted to their own
    data (e.g. `editor-own-data-only`) cannot include sessions
    belonging to other users.

    **All-or-nothing authorization.** If any single requested
    session fails the permission check or the data-scope check,
    the entire request returns 404 — the same status used when
    the id does not exist. No partial zip is produced and no body
    indicates which id was rejected. (This is deliberate, so a
    caller cannot probe which session ids exist by diffing 404
    vs 403.)

    **Partial existence.** Ids that do not exist are simply
    omitted from the resulting zip; there is no per-id error in
    the response. A 404 is returned only when zero ids resolve.

    **Side effect on successful download:** every successfully
    sent session is marked `exported = true` server-side, after
    `res.sendFile` finishes. If the client aborts mid-download
    the flag may or may not be set.

    Server-generated filename is
    `GameBench_Export_<N>-Sessions_<localDateStamp>.zip` and is
    returned via `Content-Disposition: attachment; filename=...`.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
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

) -> Error | File | None:
    """ Download a zip archive of one or more session backups

     Bundles the original `zipBackupFile` for each requested
    session into a single zip and streams it back as an
    `application/octet-stream` attachment.

    **`{sessionIds}` is a comma-separated list inside the URL
    path.** Example: `/v2/sessions/export/sessions/abc,def,ghi`.
    There is no request body. Beware URL-length limits when
    exporting many sessions at once; use
    `POST /v2/sessions/export/check` first to validate the set
    and confirm total size is under the server's export size cap
    (this endpoint does not check size — only `/export/check`
    does).

    Requires the `sessions.export` permission on every requested
    session's collection / company. The caller's data scope is
    also enforced per session: callers restricted to their own
    data (e.g. `editor-own-data-only`) cannot include sessions
    belonging to other users.

    **All-or-nothing authorization.** If any single requested
    session fails the permission check or the data-scope check,
    the entire request returns 404 — the same status used when
    the id does not exist. No partial zip is produced and no body
    indicates which id was rejected. (This is deliberate, so a
    caller cannot probe which session ids exist by diffing 404
    vs 403.)

    **Partial existence.** Ids that do not exist are simply
    omitted from the resulting zip; there is no per-id error in
    the response. A 404 is returned only when zero ids resolve.

    **Side effect on successful download:** every successfully
    sent session is marked `exported = true` server-side, after
    `res.sendFile` finishes. If the client aborts mid-download
    the flag may or may not be set.

    Server-generated filename is
    `GameBench_Export_<N>-Sessions_<localDateStamp>.zip` and is
    returned via `Content-Disposition: attachment; filename=...`.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
     """


    return sync_detailed(
        session_ids=session_ids,
client=client,

    ).parsed

async def asyncio_detailed(
    session_ids: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | File]:
    """ Download a zip archive of one or more session backups

     Bundles the original `zipBackupFile` for each requested
    session into a single zip and streams it back as an
    `application/octet-stream` attachment.

    **`{sessionIds}` is a comma-separated list inside the URL
    path.** Example: `/v2/sessions/export/sessions/abc,def,ghi`.
    There is no request body. Beware URL-length limits when
    exporting many sessions at once; use
    `POST /v2/sessions/export/check` first to validate the set
    and confirm total size is under the server's export size cap
    (this endpoint does not check size — only `/export/check`
    does).

    Requires the `sessions.export` permission on every requested
    session's collection / company. The caller's data scope is
    also enforced per session: callers restricted to their own
    data (e.g. `editor-own-data-only`) cannot include sessions
    belonging to other users.

    **All-or-nothing authorization.** If any single requested
    session fails the permission check or the data-scope check,
    the entire request returns 404 — the same status used when
    the id does not exist. No partial zip is produced and no body
    indicates which id was rejected. (This is deliberate, so a
    caller cannot probe which session ids exist by diffing 404
    vs 403.)

    **Partial existence.** Ids that do not exist are simply
    omitted from the resulting zip; there is no per-id error in
    the response. A 404 is returned only when zero ids resolve.

    **Side effect on successful download:** every successfully
    sent session is marked `exported = true` server-side, after
    `res.sendFile` finishes. If the client aborts mid-download
    the flag may or may not be set.

    Server-generated filename is
    `GameBench_Export_<N>-Sessions_<localDateStamp>.zip` and is
    returned via `Content-Disposition: attachment; filename=...`.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
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

) -> Error | File | None:
    """ Download a zip archive of one or more session backups

     Bundles the original `zipBackupFile` for each requested
    session into a single zip and streams it back as an
    `application/octet-stream` attachment.

    **`{sessionIds}` is a comma-separated list inside the URL
    path.** Example: `/v2/sessions/export/sessions/abc,def,ghi`.
    There is no request body. Beware URL-length limits when
    exporting many sessions at once; use
    `POST /v2/sessions/export/check` first to validate the set
    and confirm total size is under the server's export size cap
    (this endpoint does not check size — only `/export/check`
    does).

    Requires the `sessions.export` permission on every requested
    session's collection / company. The caller's data scope is
    also enforced per session: callers restricted to their own
    data (e.g. `editor-own-data-only`) cannot include sessions
    belonging to other users.

    **All-or-nothing authorization.** If any single requested
    session fails the permission check or the data-scope check,
    the entire request returns 404 — the same status used when
    the id does not exist. No partial zip is produced and no body
    indicates which id was rejected. (This is deliberate, so a
    caller cannot probe which session ids exist by diffing 404
    vs 403.)

    **Partial existence.** Ids that do not exist are simply
    omitted from the resulting zip; there is no per-id error in
    the response. A 404 is returned only when zero ids resolve.

    **Side effect on successful download:** every successfully
    sent session is marked `exported = true` server-side, after
    `res.sendFile` finishes. If the client aborts mid-download
    the flag may or may not be set.

    Server-generated filename is
    `GameBench_Export_<N>-Sessions_<localDateStamp>.zip` and is
    returned via `Content-Disposition: attachment; filename=...`.

    Args:
        session_ids (str):  Example: abc123,def456,ghi789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
     """


    return (await asyncio_detailed(
        session_ids=session_ids,
client=client,

    )).parsed
