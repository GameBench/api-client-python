from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_session_note_body import UpdateSessionNoteBody
from ...models.update_session_note_response_200 import UpdateSessionNoteResponse200
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: UpdateSessionNoteBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/sessions/{session_id}/notes".format(session_id=quote(str(session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateSessionNoteResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateSessionNoteResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateSessionNoteResponse200]:
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
    body: UpdateSessionNoteBody,

) -> Response[Error | UpdateSessionNoteResponse200]:
    """ Update an existing note's title or message

     Updates the `title` and `message` of an existing note. The
    note is identified by `id` inside the request body — the URL
    does not include the note id.

    **Only `title` and `message` are updatable.** `authorId` and
    any other fields in the payload are ignored.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Shares the per-user rate limit with POST
    and DELETE on `/notes`.

    Args:
        session_id (str):
        body (UpdateSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateSessionNoteResponse200]
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
    body: UpdateSessionNoteBody,

) -> Error | UpdateSessionNoteResponse200 | None:
    """ Update an existing note's title or message

     Updates the `title` and `message` of an existing note. The
    note is identified by `id` inside the request body — the URL
    does not include the note id.

    **Only `title` and `message` are updatable.** `authorId` and
    any other fields in the payload are ignored.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Shares the per-user rate limit with POST
    and DELETE on `/notes`.

    Args:
        session_id (str):
        body (UpdateSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateSessionNoteResponse200
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
    body: UpdateSessionNoteBody,

) -> Response[Error | UpdateSessionNoteResponse200]:
    """ Update an existing note's title or message

     Updates the `title` and `message` of an existing note. The
    note is identified by `id` inside the request body — the URL
    does not include the note id.

    **Only `title` and `message` are updatable.** `authorId` and
    any other fields in the payload are ignored.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Shares the per-user rate limit with POST
    and DELETE on `/notes`.

    Args:
        session_id (str):
        body (UpdateSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateSessionNoteResponse200]
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
    body: UpdateSessionNoteBody,

) -> Error | UpdateSessionNoteResponse200 | None:
    """ Update an existing note's title or message

     Updates the `title` and `message` of an existing note. The
    note is identified by `id` inside the request body — the URL
    does not include the note id.

    **Only `title` and `message` are updatable.** `authorId` and
    any other fields in the payload are ignored.

    Requires the `sessions.update` permission and respects the
    caller's data scope. Shares the per-user rate limit with POST
    and DELETE on `/notes`.

    Args:
        session_id (str):
        body (UpdateSessionNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateSessionNoteResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
