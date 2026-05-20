from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MetricStats")



@_attrs_define
class MetricStats:
    """ Summary statistics over a metric's samples.

        Attributes:
            min_ (float | Unset):
            max_ (float | Unset):
            avg (float | Unset):
            median (float | Unset):
     """

    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    avg: float | Unset = UNSET
    median: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        avg = self.avg

        median = self.median


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if avg is not UNSET:
            field_dict["avg"] = avg
        if median is not UNSET:
            field_dict["median"] = median

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        avg = d.pop("avg", UNSET)

        median = d.pop("median", UNSET)

        metric_stats = cls(
            min_=min_,
            max_=max_,
            avg=avg,
            median=median,
        )


        metric_stats.additional_properties = d
        return metric_stats

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
