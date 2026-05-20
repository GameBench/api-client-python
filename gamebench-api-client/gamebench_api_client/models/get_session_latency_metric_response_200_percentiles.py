from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSessionLatencyMetricResponse200Percentiles")



@_attrs_define
class GetSessionLatencyMetricResponse200Percentiles:
    """ 
        Attributes:
            field_95 (float | Unset):
            field_99 (float | Unset):
     """

    field_95: float | Unset = UNSET
    field_99: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_95 = self.field_95

        field_99 = self.field_99


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if field_95 is not UNSET:
            field_dict["95"] = field_95
        if field_99 is not UNSET:
            field_dict["99"] = field_99

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_95 = d.pop("95", UNSET)

        field_99 = d.pop("99", UNSET)

        get_session_latency_metric_response_200_percentiles = cls(
            field_95=field_95,
            field_99=field_99,
        )


        get_session_latency_metric_response_200_percentiles.additional_properties = d
        return get_session_latency_metric_response_200_percentiles

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
