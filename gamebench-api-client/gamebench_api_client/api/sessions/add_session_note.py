from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_session_note_body import AddSessionNoteBody
from ...models.add_session_note_response_200 import AddSessionNoteResponse200
from ...models.error import Error
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: AddSessionNoteBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sessions/{session_id}/notes".format(session_id=quote(str(session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AddSessionNoteResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = AddSessionNoteResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AddSessionNoteResponse200 | Error]:
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
    body: AddSessionNoteBody,

) -> Response[AddSessionNoteResponse200 | Error]:
    """ Add a new note to a session

     Inserts a note. The server stamps `authorId = req.user.id`
    regardless of what the body sends — clients cannot
    impersonate another author by writing `authorId` in the
    payload.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Per-user rate limit, shared across POST / PUT / DELETE on
    `/notes`.** All three mutating note routes share a single
    per-user quota — a 429 from any one verb means the user's
    note-mutation quota is exhausted across all three.

    Args:
        session_id (str):
        body (AddSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSessionNoteResponse200 | Error]
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
    body: AddSessionNoteBody,

) -> AddSessionNoteResponse200 | Error | None:
    """ Add a new note to a session

     Inserts a note. The server stamps `authorId = req.user.id`
    regardless of what the body sends — clients cannot
    impersonate another author by writing `authorId` in the
    payload.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Per-user rate limit, shared across POST / PUT / DELETE on
    `/notes`.** All three mutating note routes share a single
    per-user quota — a 429 from any one verb means the user's
    note-mutation quota is exhausted across all three.

    Args:
        session_id (str):
        body (AddSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSessionNoteResponse200 | Error
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
    body: AddSessionNoteBody,

) -> Response[AddSessionNoteResponse200 | Error]:
    """ Add a new note to a session

     Inserts a note. The server stamps `authorId = req.user.id`
    regardless of what the body sends — clients cannot
    impersonate another author by writing `authorId` in the
    payload.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Per-user rate limit, shared across POST / PUT / DELETE on
    `/notes`.** All three mutating note routes share a single
    per-user quota — a 429 from any one verb means the user's
    note-mutation quota is exhausted across all three.

    Args:
        session_id (str):
        body (AddSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSessionNoteResponse200 | Error]
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
    body: AddSessionNoteBody,

) -> AddSessionNoteResponse200 | Error | None:
    """ Add a new note to a session

     Inserts a note. The server stamps `authorId = req.user.id`
    regardless of what the body sends — clients cannot
    impersonate another author by writing `authorId` in the
    payload.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Per-user rate limit, shared across POST / PUT / DELETE on
    `/notes`.** All three mutating note routes share a single
    per-user quota — a 429 from any one verb means the user's
    note-mutation quota is exhausted across all three.

    Args:
        session_id (str):
        body (AddSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSessionNoteResponse200 | Error
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
