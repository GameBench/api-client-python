from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.metric_response_samples_item import MetricResponseSamplesItem
  from ..models.metric_stats import MetricStats





T = TypeVar("T", bound="MetricResponse")



@_attrs_define
class MetricResponse:
    """ Generic envelope for `/v2/sessions/{sessionId}/metrics/*` responses.
    Sample objects vary per metric class, so `samples[]` is left open;
    most metrics also return a `usage` block of summary statistics.

        Attributes:
            samples (list[MetricResponseSamplesItem] | Unset):
            usage (MetricStats | Unset): Summary statistics over a metric's samples.
     """

    samples: list[MetricResponseSamplesItem] | Unset = UNSET
    usage: MetricStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_response_samples_item import MetricResponseSamplesItem
        from ..models.metric_stats import MetricStats
        samples: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.samples, Unset):
            samples = []
            for samples_item_data in self.samples:
                samples_item = samples_item_data.to_dict()
                samples.append(samples_item)



        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if samples is not UNSET:
            field_dict["samples"] = samples
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_response_samples_item import MetricResponseSamplesItem
        from ..models.metric_stats import MetricStats
        d = dict(src_dict)
        _samples = d.pop("samples", UNSET)
        samples: list[MetricResponseSamplesItem] | Unset = UNSET
        if _samples is not UNSET:
            samples = []
            for samples_item_data in _samples:
                samples_item = MetricResponseSamplesItem.from_dict(samples_item_data)



                samples.append(samples_item)


        _usage = d.pop("usage", UNSET)
        usage: MetricStats | Unset
        if isinstance(_usage,  Unset):
            usage = UNSET
        else:
            usage = MetricStats.from_dict(_usage)




        metric_response = cls(
            samples=samples,
            usage=usage,
        )


        metric_response.additional_properties = d
        return metric_response

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
