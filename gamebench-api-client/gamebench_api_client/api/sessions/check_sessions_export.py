from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.check_sessions_export_body import CheckSessionsExportBody
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: CheckSessionsExportBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sessions/export/check",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[str] | None:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckSessionsExportBody,

) -> Response[Error | list[str]]:
    r""" Pre-flight a session-zip export

     Validates that a set of sessions can be exported as a single
    zip before calling `GET /v2/sessions/export/sessions/{sessionIds}`.
    Returns the subset of requested ids whose backup files are
    NOT currently available on the server (so the client can warn
    the user that those sessions will be missing from the zip).

    Also rejects the request up-front when the combined backup
    size would exceed the server's export cap (currently **1 GB**).

    Requires the `sessions.export` permission on every requested
    session's collection / company. Same all-or-nothing
    authorization and 404-overload semantics as the export route:
    if ANY requested session fails the permission or data-scope
    check, the entire request returns 404, indistinguishable from
    a non-existent id. (Deliberate, so this endpoint cannot be
    used to probe for unauthorized session ids.)

    **A `[]` response is ambiguous.** If none of the requested
    ids exist at all, the response is `200 []`, not a 404.
    Combined with the partial-existence behavior (ids that do not
    exist are simply omitted from the response), a `[]` response
    can mean either \"all sessions present (none missing backups)\"
    or \"none of the requested ids exist\" — disambiguate by
    checking against your request.

    Args:
        body (CheckSessionsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[str]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CheckSessionsExportBody,

) -> Error | list[str] | None:
    r""" Pre-flight a session-zip export

     Validates that a set of sessions can be exported as a single
    zip before calling `GET /v2/sessions/export/sessions/{sessionIds}`.
    Returns the subset of requested ids whose backup files are
    NOT currently available on the server (so the client can warn
    the user that those sessions will be missing from the zip).

    Also rejects the request up-front when the combined backup
    size would exceed the server's export cap (currently **1 GB**).

    Requires the `sessions.export` permission on every requested
    session's collection / company. Same all-or-nothing
    authorization and 404-overload semantics as the export route:
    if ANY requested session fails the permission or data-scope
    check, the entire request returns 404, indistinguishable from
    a non-existent id. (Deliberate, so this endpoint cannot be
    used to probe for unauthorized session ids.)

    **A `[]` response is ambiguous.** If none of the requested
    ids exist at all, the response is `200 []`, not a 404.
    Combined with the partial-existence behavior (ids that do not
    exist are simply omitted from the response), a `[]` response
    can mean either \"all sessions present (none missing backups)\"
    or \"none of the requested ids exist\" — disambiguate by
    checking against your request.

    Args:
        body (CheckSessionsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[str]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckSessionsExportBody,

) -> Response[Error | list[str]]:
    r""" Pre-flight a session-zip export

     Validates that a set of sessions can be exported as a single
    zip before calling `GET /v2/sessions/export/sessions/{sessionIds}`.
    Returns the subset of requested ids whose backup files are
    NOT currently available on the server (so the client can warn
    the user that those sessions will be missing from the zip).

    Also rejects the request up-front when the combined backup
    size would exceed the server's export cap (currently **1 GB**).

    Requires the `sessions.export` permission on every requested
    session's collection / company. Same all-or-nothing
    authorization and 404-overload semantics as the export route:
    if ANY requested session fails the permission or data-scope
    check, the entire request returns 404, indistinguishable from
    a non-existent id. (Deliberate, so this endpoint cannot be
    used to probe for unauthorized session ids.)

    **A `[]` response is ambiguous.** If none of the requested
    ids exist at all, the response is `200 []`, not a 404.
    Combined with the partial-existence behavior (ids that do not
    exist are simply omitted from the response), a `[]` response
    can mean either \"all sessions present (none missing backups)\"
    or \"none of the requested ids exist\" — disambiguate by
    checking against your request.

    Args:
        body (CheckSessionsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[str]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CheckSessionsExportBody,

) -> Error | list[str] | None:
    r""" Pre-flight a session-zip export

     Validates that a set of sessions can be exported as a single
    zip before calling `GET /v2/sessions/export/sessions/{sessionIds}`.
    Returns the subset of requested ids whose backup files are
    NOT currently available on the server (so the client can warn
    the user that those sessions will be missing from the zip).

    Also rejects the request up-front when the combined backup
    size would exceed the server's export cap (currently **1 GB**).

    Requires the `sessions.export` permission on every requested
    session's collection / company. Same all-or-nothing
    authorization and 404-overload semantics as the export route:
    if ANY requested session fails the permission or data-scope
    check, the entire request returns 404, indistinguishable from
    a non-existent id. (Deliberate, so this endpoint cannot be
    used to probe for unauthorized session ids.)

    **A `[]` response is ambiguous.** If none of the requested
    ids exist at all, the response is `200 []`, not a 404.
    Combined with the partial-existence behavior (ids that do not
    exist are simply omitted from the response), a `[]` response
    can mean either \"all sessions present (none missing backups)\"
    or \"none of the requested ids exist\" — disambiguate by
    checking against your request.

    Args:
        body (CheckSessionsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[str]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
