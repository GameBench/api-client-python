from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.import_session_body import ImportSessionBody
from ...models.import_session_response_201 import ImportSessionResponse201
from typing import cast



def _get_kwargs(
    *,
    body: ImportSessionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sessions/import",
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ImportSessionResponse201 | None:
    if response.status_code == 201:
        response_201 = ImportSessionResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ImportSessionResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportSessionBody,

) -> Response[Error | ImportSessionResponse201]:
    r""" Upload a session zip for asynchronous parsing

     Accepts a GameBench session zip (as produced by the SDK or
    capture tool) and enqueues it for parsing. The session is
    attributed to the calling user.

    **The 201 response is returned before the upload is
    persisted.** The handler validates the zip and reserves the
    upload UUID synchronously, then completes the durable store
    and queues the parsing job asynchronously. A 201 indicates
    the upload was accepted; clients should still verify the
    session appears via the session list / get APIs (or via
    notifications) before treating the upload as complete.

    **SDK-specific checks** apply only when the form field
    `source` is exactly `\"sdk\"`:

    - **Per-company rate limit** (sliding window). On exceed:
      `429`.
    - **SDK license validation** via `checkSdkLicense`. Only runs
      when the calling user is a member of a company; otherwise
      skipped. When it runs, failures surface as `400` with one
      of:
      - `\"SDK license not present\"`
      - `\"SDK license expired\"`
      - `\"Company has reached their SDK session allowance: <n>/<limit>\"`
        (only when `SDK_ENFORCE_DAILY_UPLOAD_LIMIT` is on; the
        default cap is 1000 sessions/day, or
        `company.sub.sdkDailyUploadLimit` if set).

    **Response header:** `X-GB-Session-Upload-UUID` is set to the
    same UUID returned as `jobId`. The Redis key
    `upload:<uuid>` is set with a 1-hour TTL during processing.

    **Polling status:** there is no status endpoint exposed in
    this router. The `jobId` is consumed by the parsing queue
    worker; clients track completion by polling for the resulting
    session row in the standard session list / get APIs, or via
    a separate notifications channel.

    Args:
        body (ImportSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportSessionResponse201]
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
    body: ImportSessionBody,

) -> Error | ImportSessionResponse201 | None:
    r""" Upload a session zip for asynchronous parsing

     Accepts a GameBench session zip (as produced by the SDK or
    capture tool) and enqueues it for parsing. The session is
    attributed to the calling user.

    **The 201 response is returned before the upload is
    persisted.** The handler validates the zip and reserves the
    upload UUID synchronously, then completes the durable store
    and queues the parsing job asynchronously. A 201 indicates
    the upload was accepted; clients should still verify the
    session appears via the session list / get APIs (or via
    notifications) before treating the upload as complete.

    **SDK-specific checks** apply only when the form field
    `source` is exactly `\"sdk\"`:

    - **Per-company rate limit** (sliding window). On exceed:
      `429`.
    - **SDK license validation** via `checkSdkLicense`. Only runs
      when the calling user is a member of a company; otherwise
      skipped. When it runs, failures surface as `400` with one
      of:
      - `\"SDK license not present\"`
      - `\"SDK license expired\"`
      - `\"Company has reached their SDK session allowance: <n>/<limit>\"`
        (only when `SDK_ENFORCE_DAILY_UPLOAD_LIMIT` is on; the
        default cap is 1000 sessions/day, or
        `company.sub.sdkDailyUploadLimit` if set).

    **Response header:** `X-GB-Session-Upload-UUID` is set to the
    same UUID returned as `jobId`. The Redis key
    `upload:<uuid>` is set with a 1-hour TTL during processing.

    **Polling status:** there is no status endpoint exposed in
    this router. The `jobId` is consumed by the parsing queue
    worker; clients track completion by polling for the resulting
    session row in the standard session list / get APIs, or via
    a separate notifications channel.

    Args:
        body (ImportSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportSessionResponse201
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportSessionBody,

) -> Response[Error | ImportSessionResponse201]:
    r""" Upload a session zip for asynchronous parsing

     Accepts a GameBench session zip (as produced by the SDK or
    capture tool) and enqueues it for parsing. The session is
    attributed to the calling user.

    **The 201 response is returned before the upload is
    persisted.** The handler validates the zip and reserves the
    upload UUID synchronously, then completes the durable store
    and queues the parsing job asynchronously. A 201 indicates
    the upload was accepted; clients should still verify the
    session appears via the session list / get APIs (or via
    notifications) before treating the upload as complete.

    **SDK-specific checks** apply only when the form field
    `source` is exactly `\"sdk\"`:

    - **Per-company rate limit** (sliding window). On exceed:
      `429`.
    - **SDK license validation** via `checkSdkLicense`. Only runs
      when the calling user is a member of a company; otherwise
      skipped. When it runs, failures surface as `400` with one
      of:
      - `\"SDK license not present\"`
      - `\"SDK license expired\"`
      - `\"Company has reached their SDK session allowance: <n>/<limit>\"`
        (only when `SDK_ENFORCE_DAILY_UPLOAD_LIMIT` is on; the
        default cap is 1000 sessions/day, or
        `company.sub.sdkDailyUploadLimit` if set).

    **Response header:** `X-GB-Session-Upload-UUID` is set to the
    same UUID returned as `jobId`. The Redis key
    `upload:<uuid>` is set with a 1-hour TTL during processing.

    **Polling status:** there is no status endpoint exposed in
    this router. The `jobId` is consumed by the parsing queue
    worker; clients track completion by polling for the resulting
    session row in the standard session list / get APIs, or via
    a separate notifications channel.

    Args:
        body (ImportSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportSessionResponse201]
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
    body: ImportSessionBody,

) -> Error | ImportSessionResponse201 | None:
    r""" Upload a session zip for asynchronous parsing

     Accepts a GameBench session zip (as produced by the SDK or
    capture tool) and enqueues it for parsing. The session is
    attributed to the calling user.

    **The 201 response is returned before the upload is
    persisted.** The handler validates the zip and reserves the
    upload UUID synchronously, then completes the durable store
    and queues the parsing job asynchronously. A 201 indicates
    the upload was accepted; clients should still verify the
    session appears via the session list / get APIs (or via
    notifications) before treating the upload as complete.

    **SDK-specific checks** apply only when the form field
    `source` is exactly `\"sdk\"`:

    - **Per-company rate limit** (sliding window). On exceed:
      `429`.
    - **SDK license validation** via `checkSdkLicense`. Only runs
      when the calling user is a member of a company; otherwise
      skipped. When it runs, failures surface as `400` with one
      of:
      - `\"SDK license not present\"`
      - `\"SDK license expired\"`
      - `\"Company has reached their SDK session allowance: <n>/<limit>\"`
        (only when `SDK_ENFORCE_DAILY_UPLOAD_LIMIT` is on; the
        default cap is 1000 sessions/day, or
        `company.sub.sdkDailyUploadLimit` if set).

    **Response header:** `X-GB-Session-Upload-UUID` is set to the
    same UUID returned as `jobId`. The Redis key
    `upload:<uuid>` is set with a 1-hour TTL during processing.

    **Polling status:** there is no status endpoint exposed in
    this router. The `jobId` is consumed by the parsing queue
    worker; clients track completion by polling for the resulting
    session row in the standard session list / get APIs, or via
    a separate notifications channel.

    Args:
        body (ImportSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportSessionResponse201
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
