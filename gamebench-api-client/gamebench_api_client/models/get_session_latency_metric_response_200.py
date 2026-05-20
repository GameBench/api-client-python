from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_session_latency_metric_response_200_frametimes_percentiles import GetSessionLatencyMetricResponse200FrametimesPercentiles
  from ..models.get_session_latency_metric_response_200_histogram import GetSessionLatencyMetricResponse200Histogram
  from ..models.get_session_latency_metric_response_200_percentiles import GetSessionLatencyMetricResponse200Percentiles
  from ..models.get_session_latency_metric_response_200_samples_item import GetSessionLatencyMetricResponse200SamplesItem





T = TypeVar("T", bound="GetSessionLatencyMetricResponse200")



@_attrs_define
class GetSessionLatencyMetricResponse200:
    """ 
        Attributes:
            samples (list[GetSessionLatencyMetricResponse200SamplesItem] | Unset):
            histogram (GetSessionLatencyMetricResponse200Histogram | Unset):
            percentiles (GetSessionLatencyMetricResponse200Percentiles | Unset):
            frametimes_percentiles (GetSessionLatencyMetricResponse200FrametimesPercentiles | Unset):
     """

    samples: list[GetSessionLatencyMetricResponse200SamplesItem] | Unset = UNSET
    histogram: GetSessionLatencyMetricResponse200Histogram | Unset = UNSET
    percentiles: GetSessionLatencyMetricResponse200Percentiles | Unset = UNSET
    frametimes_percentiles: GetSessionLatencyMetricResponse200FrametimesPercentiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_session_latency_metric_response_200_frametimes_percentiles import GetSessionLatencyMetricResponse200FrametimesPercentiles
        from ..models.get_session_latency_metric_response_200_histogram import GetSessionLatencyMetricResponse200Histogram
        from ..models.get_session_latency_metric_response_200_percentiles import GetSessionLatencyMetricResponse200Percentiles
        from ..models.get_session_latency_metric_response_200_samples_item import GetSessionLatencyMetricResponse200SamplesItem
        samples: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.samples, Unset):
            samples = []
            for samples_item_data in self.samples:
                samples_item = samples_item_data.to_dict()
                samples.append(samples_item)



        histogram: dict[str, Any] | Unset = UNSET
        if not isinstance(self.histogram, Unset):
            histogram = self.histogram.to_dict()

        percentiles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.percentiles, Unset):
            percentiles = self.percentiles.to_dict()

        frametimes_percentiles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.frametimes_percentiles, Unset):
            frametimes_percentiles = self.frametimes_percentiles.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if samples is not UNSET:
            field_dict["samples"] = samples
        if histogram is not UNSET:
            field_dict["histogram"] = histogram
        if percentiles is not UNSET:
            field_dict["percentiles"] = percentiles
        if frametimes_percentiles is not UNSET:
            field_dict["frametimesPercentiles"] = frametimes_percentiles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_session_latency_metric_response_200_frametimes_percentiles import GetSessionLatencyMetricResponse200FrametimesPercentiles
        from ..models.get_session_latency_metric_response_200_histogram import GetSessionLatencyMetricResponse200Histogram
        from ..models.get_session_latency_metric_response_200_percentiles import GetSessionLatencyMetricResponse200Percentiles
        from ..models.get_session_latency_metric_response_200_samples_item import GetSessionLatencyMetricResponse200SamplesItem
        d = dict(src_dict)
        _samples = d.pop("samples", UNSET)
        samples: list[GetSessionLatencyMetricResponse200SamplesItem] | Unset = UNSET
        if _samples is not UNSET:
            samples = []
            for samples_item_data in _samples:
                samples_item = GetSessionLatencyMetricResponse200SamplesItem.from_dict(samples_item_data)



                samples.append(samples_item)


        _histogram = d.pop("histogram", UNSET)
        histogram: GetSessionLatencyMetricResponse200Histogram | Unset
        if isinstance(_histogram,  Unset):
            histogram = UNSET
        else:
            histogram = GetSessionLatencyMetricResponse200Histogram.from_dict(_histogram)




        _percentiles = d.pop("percentiles", UNSET)
        percentiles: GetSessionLatencyMetricResponse200Percentiles | Unset
        if isinstance(_percentiles,  Unset):
            percentiles = UNSET
        else:
            percentiles = GetSessionLatencyMetricResponse200Percentiles.from_dict(_percentiles)




        _frametimes_percentiles = d.pop("frametimesPercentiles", UNSET)
        frametimes_percentiles: GetSessionLatencyMetricResponse200FrametimesPercentiles | Unset
        if isinstance(_frametimes_percentiles,  Unset):
            frametimes_percentiles = UNSET
        else:
            frametimes_percentiles = GetSessionLatencyMetricResponse200FrametimesPercentiles.from_dict(_frametimes_percentiles)




        get_session_latency_metric_response_200 = cls(
            samples=samples,
            histogram=histogram,
            percentiles=percentiles,
            frametimes_percentiles=frametimes_percentiles,
        )


        get_session_latency_metric_response_200.additional_properties = d
        return get_session_latency_metric_response_200

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
