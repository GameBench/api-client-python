from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_collection_sessions_body import ListCollectionSessionsBody
from ...models.page_of_session import PageOfSession
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    collection_id: str,
    *,
    body: ListCollectionSessionsBody | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 15,
    sort: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sort"] = sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collections/{collection_id}/sessions".format(collection_id=quote(str(collection_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PageOfSession | None:
    if response.status_code == 200:
        response_200 = PageOfSession.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PageOfSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListCollectionSessionsBody | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 15,
    sort: str | Unset = UNSET,

) -> Response[Error | PageOfSession]:
    """ List sessions in a collection, filtered by a body filter object

     POST is used because the body carries a filter object too rich
    to express as query-string parameters; the endpoint returns a
    page of matching sessions and does not create or modify any
    resource.

    **Permission required: `collections.sessions.list`** (read, not
    write) — same permission as the GET form. A caller with read
    access to the collection can use this endpoint.

    **Pagination and sort are query-string params, not body
    fields.** Use `page`, `pageSize`, and `sort` on the URL; the
    body is reserved for filters. Defaults: `page=0`,
    `pageSize=15`. `pageSize=-1` is accepted and clamped to 10000.

    **User-data scope is enforced server-side and cannot be
    overridden by the body.** Callers whose role on the collection
    is restricted to their own data (e.g. `editor-own-data-only`)
    see only their own sessions, regardless of the filters
    submitted.

    Unknown body fields are ignored — there is no 400 for
    unrecognised keys.

    Args:
        collection_id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 15.
        sort (str | Unset):
        body (ListCollectionSessionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PageOfSession]
     """


    kwargs = _get_kwargs(
        collection_id=collection_id,
body=body,
page=page,
page_size=page_size,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListCollectionSessionsBody | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 15,
    sort: str | Unset = UNSET,

) -> Error | PageOfSession | None:
    """ List sessions in a collection, filtered by a body filter object

     POST is used because the body carries a filter object too rich
    to express as query-string parameters; the endpoint returns a
    page of matching sessions and does not create or modify any
    resource.

    **Permission required: `collections.sessions.list`** (read, not
    write) — same permission as the GET form. A caller with read
    access to the collection can use this endpoint.

    **Pagination and sort are query-string params, not body
    fields.** Use `page`, `pageSize`, and `sort` on the URL; the
    body is reserved for filters. Defaults: `page=0`,
    `pageSize=15`. `pageSize=-1` is accepted and clamped to 10000.

    **User-data scope is enforced server-side and cannot be
    overridden by the body.** Callers whose role on the collection
    is restricted to their own data (e.g. `editor-own-data-only`)
    see only their own sessions, regardless of the filters
    submitted.

    Unknown body fields are ignored — there is no 400 for
    unrecognised keys.

    Args:
        collection_id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 15.
        sort (str | Unset):
        body (ListCollectionSessionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PageOfSession
     """


    return sync_detailed(
        collection_id=collection_id,
client=client,
body=body,
page=page,
page_size=page_size,
sort=sort,

    ).parsed

async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListCollectionSessionsBody | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 15,
    sort: str | Unset = UNSET,

) -> Response[Error | PageOfSession]:
    """ List sessions in a collection, filtered by a body filter object

     POST is used because the body carries a filter object too rich
    to express as query-string parameters; the endpoint returns a
    page of matching sessions and does not create or modify any
    resource.

    **Permission required: `collections.sessions.list`** (read, not
    write) — same permission as the GET form. A caller with read
    access to the collection can use this endpoint.

    **Pagination and sort are query-string params, not body
    fields.** Use `page`, `pageSize`, and `sort` on the URL; the
    body is reserved for filters. Defaults: `page=0`,
    `pageSize=15`. `pageSize=-1` is accepted and clamped to 10000.

    **User-data scope is enforced server-side and cannot be
    overridden by the body.** Callers whose role on the collection
    is restricted to their own data (e.g. `editor-own-data-only`)
    see only their own sessions, regardless of the filters
    submitted.

    Unknown body fields are ignored — there is no 400 for
    unrecognised keys.

    Args:
        collection_id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 15.
        sort (str | Unset):
        body (ListCollectionSessionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PageOfSession]
     """


    kwargs = _get_kwargs(
        collection_id=collection_id,
body=body,
page=page,
page_size=page_size,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListCollectionSessionsBody | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 15,
    sort: str | Unset = UNSET,

) -> Error | PageOfSession | None:
    """ List sessions in a collection, filtered by a body filter object

     POST is used because the body carries a filter object too rich
    to express as query-string parameters; the endpoint returns a
    page of matching sessions and does not create or modify any
    resource.

    **Permission required: `collections.sessions.list`** (read, not
    write) — same permission as the GET form. A caller with read
    access to the collection can use this endpoint.

    **Pagination and sort are query-string params, not body
    fields.** Use `page`, `pageSize`, and `sort` on the URL; the
    body is reserved for filters. Defaults: `page=0`,
    `pageSize=15`. `pageSize=-1` is accepted and clamped to 10000.

    **User-data scope is enforced server-side and cannot be
    overridden by the body.** Callers whose role on the collection
    is restricted to their own data (e.g. `editor-own-data-only`)
    see only their own sessions, regardless of the filters
    submitted.

    Unknown body fields are ignored — there is no 400 for
    unrecognised keys.

    Args:
        collection_id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 15.
        sort (str | Unset):
        body (ListCollectionSessionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PageOfSession
     """


    return (await asyncio_detailed(
        collection_id=collection_id,
client=client,
body=body,
page=page,
page_size=page_size,
sort=sort,

    )).parsed
