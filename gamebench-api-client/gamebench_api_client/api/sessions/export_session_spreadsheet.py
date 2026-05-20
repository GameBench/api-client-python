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

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/export/spreadsheet".format(session_id=quote(str(session_id), safe=""),),
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
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | File]:
    """ Download a session's metric samples as an XLSX workbook

     Generates an Excel workbook (`.xlsx`) of the session's metric
    data, built in-process — no signed-URL redirect.

    Requires the `sessions.export` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.xlsx`,
    delivered via `Content-Disposition: attachment`.

    **Note — `Content-Type` is `application/octet-stream`, not
    the standard XLSX media type
    `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`.**
    Clients sniffing by MIME type may need to fall back to the
    filename extension.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
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

) -> Error | File | None:
    """ Download a session's metric samples as an XLSX workbook

     Generates an Excel workbook (`.xlsx`) of the session's metric
    data, built in-process — no signed-URL redirect.

    Requires the `sessions.export` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.xlsx`,
    delivered via `Content-Disposition: attachment`.

    **Note — `Content-Type` is `application/octet-stream`, not
    the standard XLSX media type
    `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`.**
    Clients sniffing by MIME type may need to fall back to the
    filename extension.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | File]:
    """ Download a session's metric samples as an XLSX workbook

     Generates an Excel workbook (`.xlsx`) of the session's metric
    data, built in-process — no signed-URL redirect.

    Requires the `sessions.export` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.xlsx`,
    delivered via `Content-Disposition: attachment`.

    **Note — `Content-Type` is `application/octet-stream`, not
    the standard XLSX media type
    `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`.**
    Clients sniffing by MIME type may need to fall back to the
    filename extension.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
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

) -> Error | File | None:
    """ Download a session's metric samples as an XLSX workbook

     Generates an Excel workbook (`.xlsx`) of the session's metric
    data, built in-process — no signed-URL redirect.

    Requires the `sessions.export` permission and respects the
    caller's data scope. Hidden sessions return 404, not 403.

    **Filename:**
    `<DD-MM-YYYY-HH:mm:ss>_<packageName>_<deviceModel>_<sessionId>.xlsx`,
    delivered via `Content-Disposition: attachment`.

    **Note — `Content-Type` is `application/octet-stream`, not
    the standard XLSX media type
    `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`.**
    Clients sniffing by MIME type may need to fall back to the
    filename extension.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
