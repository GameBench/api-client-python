from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_session_additional_files_response_200 import ListSessionAdditionalFilesResponse200
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/additional-files".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListSessionAdditionalFilesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListSessionAdditionalFilesResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListSessionAdditionalFilesResponse200]:
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

) -> Response[Error | ListSessionAdditionalFilesResponse200]:
    r""" List the supplementary files attached to a session

     Returns the catalogue of \"additional files\" captured alongside
    the session by the recording tool — arbitrary blobs whose
    filename and MIME type are preserved (e.g. extra logs, GFXR
    captures, screenshot bundles). Always returns
    `{ additionalFiles: [...] }`; the array is empty for sessions
    without any.

    Requires the `sessions.get` permission and respects the
    caller's data scope (404 on a mismatch).

    **Differs from the v1 list response by design.** v1's
    equivalent returns the raw `additionalFiles` array including
    the internal `meta` storage handle (bucket, path, md5 hash).
    v2 returns only `filename`, `type`, and `size` per item —
    what a client needs to enumerate and to display sizes —
    without leaking storage-layer detail.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListSessionAdditionalFilesResponse200]
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

) -> Error | ListSessionAdditionalFilesResponse200 | None:
    r""" List the supplementary files attached to a session

     Returns the catalogue of \"additional files\" captured alongside
    the session by the recording tool — arbitrary blobs whose
    filename and MIME type are preserved (e.g. extra logs, GFXR
    captures, screenshot bundles). Always returns
    `{ additionalFiles: [...] }`; the array is empty for sessions
    without any.

    Requires the `sessions.get` permission and respects the
    caller's data scope (404 on a mismatch).

    **Differs from the v1 list response by design.** v1's
    equivalent returns the raw `additionalFiles` array including
    the internal `meta` storage handle (bucket, path, md5 hash).
    v2 returns only `filename`, `type`, and `size` per item —
    what a client needs to enumerate and to display sizes —
    without leaking storage-layer detail.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListSessionAdditionalFilesResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | ListSessionAdditionalFilesResponse200]:
    r""" List the supplementary files attached to a session

     Returns the catalogue of \"additional files\" captured alongside
    the session by the recording tool — arbitrary blobs whose
    filename and MIME type are preserved (e.g. extra logs, GFXR
    captures, screenshot bundles). Always returns
    `{ additionalFiles: [...] }`; the array is empty for sessions
    without any.

    Requires the `sessions.get` permission and respects the
    caller's data scope (404 on a mismatch).

    **Differs from the v1 list response by design.** v1's
    equivalent returns the raw `additionalFiles` array including
    the internal `meta` storage handle (bucket, path, md5 hash).
    v2 returns only `filename`, `type`, and `size` per item —
    what a client needs to enumerate and to display sizes —
    without leaking storage-layer detail.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListSessionAdditionalFilesResponse200]
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

) -> Error | ListSessionAdditionalFilesResponse200 | None:
    r""" List the supplementary files attached to a session

     Returns the catalogue of \"additional files\" captured alongside
    the session by the recording tool — arbitrary blobs whose
    filename and MIME type are preserved (e.g. extra logs, GFXR
    captures, screenshot bundles). Always returns
    `{ additionalFiles: [...] }`; the array is empty for sessions
    without any.

    Requires the `sessions.get` permission and respects the
    caller's data scope (404 on a mismatch).

    **Differs from the v1 list response by design.** v1's
    equivalent returns the raw `additionalFiles` array including
    the internal `meta` storage handle (bucket, path, md5 hash).
    v2 returns only `filename`, `type`, and `size` per item —
    what a client needs to enumerate and to display sizes —
    without leaking storage-layer detail.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListSessionAdditionalFilesResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
