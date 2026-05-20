from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_session_notes_response_200_item import ListSessionNotesResponse200Item
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/notes".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[ListSessionNotesResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ListSessionNotesResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[ListSessionNotesResponse200Item]]:
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

) -> Response[Error | list[ListSessionNotesResponse200Item]]:
    """ List the notes attached to a session

     Returns the notes on a session as a flat array — no
    pagination, no envelope. Empty sessions return `200 []`.

    Each note includes the author's `firstName` / `surname`
    joined in from the user table for display.

    Requires the `sessions.get` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[ListSessionNotesResponse200Item]]
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

) -> Error | list[ListSessionNotesResponse200Item] | None:
    """ List the notes attached to a session

     Returns the notes on a session as a flat array — no
    pagination, no envelope. Empty sessions return `200 []`.

    Each note includes the author's `firstName` / `surname`
    joined in from the user table for display.

    Requires the `sessions.get` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[ListSessionNotesResponse200Item]
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | list[ListSessionNotesResponse200Item]]:
    """ List the notes attached to a session

     Returns the notes on a session as a flat array — no
    pagination, no envelope. Empty sessions return `200 []`.

    Each note includes the author's `firstName` / `surname`
    joined in from the user table for display.

    Requires the `sessions.get` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[ListSessionNotesResponse200Item]]
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

) -> Error | list[ListSessionNotesResponse200Item] | None:
    """ List the notes attached to a session

     Returns the notes on a session as a flat array — no
    pagination, no envelope. Empty sessions return `200 []`.

    Each note includes the author's `firstName` / `surname`
    joined in from the user table for display.

    Requires the `sessions.get` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[ListSessionNotesResponse200Item]
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
