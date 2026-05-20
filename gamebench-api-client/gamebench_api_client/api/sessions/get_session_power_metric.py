from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_session_power_metric_response_200_type_0 import GetSessionPowerMetricResponse200Type0
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sessions/{session_id}/metrics/power".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetSessionPowerMetricResponse200Type0 | list[Any] | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> GetSessionPowerMetricResponse200Type0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetSessionPowerMetricResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = cast(list[Any], data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetSessionPowerMetricResponse200Type0 | list[Any]]:
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

) -> Response[Error | GetSessionPowerMetricResponse200Type0 | list[Any]]:
    r""" Instantaneous power samples

     **Returns `[]` for sessions where the device was charging.**
    When `session.isCharging === true`, the response is an empty
    array. An empty array can therefore mean either \"the device
    was charging\" or \"the session has no power samples\"; check
    the session's `isCharging` flag (via
    `GET /v2/sessions/{sessionId}`) to disambiguate.

    Note the response shape is different in the charging case
    (`[]`) versus the non-charging case (object with samples).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionPowerMetricResponse200Type0 | list[Any]]
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

) -> Error | GetSessionPowerMetricResponse200Type0 | list[Any] | None:
    r""" Instantaneous power samples

     **Returns `[]` for sessions where the device was charging.**
    When `session.isCharging === true`, the response is an empty
    array. An empty array can therefore mean either \"the device
    was charging\" or \"the session has no power samples\"; check
    the session's `isCharging` flag (via
    `GET /v2/sessions/{sessionId}`) to disambiguate.

    Note the response shape is different in the charging case
    (`[]`) versus the non-charging case (object with samples).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionPowerMetricResponse200Type0 | list[Any]
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetSessionPowerMetricResponse200Type0 | list[Any]]:
    r""" Instantaneous power samples

     **Returns `[]` for sessions where the device was charging.**
    When `session.isCharging === true`, the response is an empty
    array. An empty array can therefore mean either \"the device
    was charging\" or \"the session has no power samples\"; check
    the session's `isCharging` flag (via
    `GET /v2/sessions/{sessionId}`) to disambiguate.

    Note the response shape is different in the charging case
    (`[]`) versus the non-charging case (object with samples).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSessionPowerMetricResponse200Type0 | list[Any]]
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

) -> Error | GetSessionPowerMetricResponse200Type0 | list[Any] | None:
    r""" Instantaneous power samples

     **Returns `[]` for sessions where the device was charging.**
    When `session.isCharging === true`, the response is an empty
    array. An empty array can therefore mean either \"the device
    was charging\" or \"the session has no power samples\"; check
    the session's `isCharging` flag (via
    `GET /v2/sessions/{sessionId}`) to disambiguate.

    Note the response shape is different in the charging case
    (`[]`) versus the non-charging case (object with samples).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSessionPowerMetricResponse200Type0 | list[Any]
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
