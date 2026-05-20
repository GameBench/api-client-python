from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_collections_response_200 import ListCollectionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    company_id: str | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["companyId"] = company_id

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListCollectionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListCollectionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListCollectionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    company_id: str | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 50,

) -> Response[Error | ListCollectionsResponse200]:
    r""" List session collections visible to the caller

     **The response shape depends on the caller's permissions.**

    If the caller has the `collections.list` permission on the
    target company (in practice: company-admins on their own
    company, global-admins anywhere), the response is the
    company-scoped, paginated form:

    ```
    { \"collections\": [...], \"count\": <totalHits> }
    ```

    Otherwise the server falls back to the user-scoped form, which
    returns ALL of the caller's own collections, ignores `page` /
    `pageSize`, and omits `count`:

    ```
    { \"collections\": [...] }
    ```

    The two paths also return slightly different fields per
    collection — the user-scoped form includes `role` and
    `permissions`; the company-scoped form does not.

    Unlike `/v1/users` and `/v1/companies`, this endpoint does NOT
    take a `global=true` flag or a JSON `filter` parameter.

    Args:
        company_id (str | Unset):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListCollectionsResponse200]
     """


    kwargs = _get_kwargs(
        company_id=company_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    company_id: str | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 50,

) -> Error | ListCollectionsResponse200 | None:
    r""" List session collections visible to the caller

     **The response shape depends on the caller's permissions.**

    If the caller has the `collections.list` permission on the
    target company (in practice: company-admins on their own
    company, global-admins anywhere), the response is the
    company-scoped, paginated form:

    ```
    { \"collections\": [...], \"count\": <totalHits> }
    ```

    Otherwise the server falls back to the user-scoped form, which
    returns ALL of the caller's own collections, ignores `page` /
    `pageSize`, and omits `count`:

    ```
    { \"collections\": [...] }
    ```

    The two paths also return slightly different fields per
    collection — the user-scoped form includes `role` and
    `permissions`; the company-scoped form does not.

    Unlike `/v1/users` and `/v1/companies`, this endpoint does NOT
    take a `global=true` flag or a JSON `filter` parameter.

    Args:
        company_id (str | Unset):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListCollectionsResponse200
     """


    return sync_detailed(
        client=client,
company_id=company_id,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    company_id: str | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 50,

) -> Response[Error | ListCollectionsResponse200]:
    r""" List session collections visible to the caller

     **The response shape depends on the caller's permissions.**

    If the caller has the `collections.list` permission on the
    target company (in practice: company-admins on their own
    company, global-admins anywhere), the response is the
    company-scoped, paginated form:

    ```
    { \"collections\": [...], \"count\": <totalHits> }
    ```

    Otherwise the server falls back to the user-scoped form, which
    returns ALL of the caller's own collections, ignores `page` /
    `pageSize`, and omits `count`:

    ```
    { \"collections\": [...] }
    ```

    The two paths also return slightly different fields per
    collection — the user-scoped form includes `role` and
    `permissions`; the company-scoped form does not.

    Unlike `/v1/users` and `/v1/companies`, this endpoint does NOT
    take a `global=true` flag or a JSON `filter` parameter.

    Args:
        company_id (str | Unset):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListCollectionsResponse200]
     """


    kwargs = _get_kwargs(
        company_id=company_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    company_id: str | Unset = UNSET,
    page: int | Unset = 0,
    page_size: int | Unset = 50,

) -> Error | ListCollectionsResponse200 | None:
    r""" List session collections visible to the caller

     **The response shape depends on the caller's permissions.**

    If the caller has the `collections.list` permission on the
    target company (in practice: company-admins on their own
    company, global-admins anywhere), the response is the
    company-scoped, paginated form:

    ```
    { \"collections\": [...], \"count\": <totalHits> }
    ```

    Otherwise the server falls back to the user-scoped form, which
    returns ALL of the caller's own collections, ignores `page` /
    `pageSize`, and omits `count`:

    ```
    { \"collections\": [...] }
    ```

    The two paths also return slightly different fields per
    collection — the user-scoped form includes `role` and
    `permissions`; the company-scoped form does not.

    Unlike `/v1/users` and `/v1/companies`, this endpoint does NOT
    take a `global=true` flag or a JSON `filter` parameter.

    Args:
        company_id (str | Unset):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListCollectionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
company_id=company_id,
page=page,
page_size=page_size,

    )).parsed
