from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_session_markers_response_200_item_android_memory_usage import ListSessionMarkersResponse200ItemAndroidMemoryUsage





T = TypeVar("T", bound="ListSessionMarkersResponse200Item")



@_attrs_define
class ListSessionMarkersResponse200Item:
    """ 
        Attributes:
            session_id (str):
            ts_start (int): Marker start, in milliseconds.
            ts_end (int): Marker end, in milliseconds. Always >= tsStart.
            id (str | Unset):
            label (str | Unset):
            group (str | Unset):
            track (int | Unset): Track index for multi-track timeline layout.
            colour (str | Unset): Persistent colour for timeline visualisation.
            fps_avg (float | Unset):
            fps_min (int | Unset):
            fps_max (int | Unset):
            fps_median (int | Unset):
            fps_stability (float | Unset):
            fps_stability_index (float | Unset):
            fps_one_percent_low (float | Unset):
            frametime_95_th_percentile (float | Unset):
            cpu_usage_min (float | Unset):
            cpu_usage_avg (float | Unset):
            cpu_usage_max (float | Unset):
            cpu_usage_median (float | Unset):
            gpu_usage_min (float | Unset):
            gpu_usage_avg (float | Unset):
            gpu_usage_max (float | Unset):
            gpu_usage_median (float | Unset):
            mem_usage_min (int | Unset):
            mem_usage_avg (int | Unset):
            mem_usage_max (int | Unset):
            app_received_bytes (int | Unset):
            app_sent_bytes (int | Unset):
            m_a_min (float | Unset):
            m_a_avg (float | Unset):
            m_a_max (float | Unset):
            big_janks_count (int | Unset):
            big_janks_10_mins (float | Unset):
            janks_count (int | Unset):
            janks_10_mins (float | Unset):
            android_memory_usage (ListSessionMarkersResponse200ItemAndroidMemoryUsage | Unset):
     """

    session_id: str
    ts_start: int
    ts_end: int
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    group: str | Unset = UNSET
    track: int | Unset = UNSET
    colour: str | Unset = UNSET
    fps_avg: float | Unset = UNSET
    fps_min: int | Unset = UNSET
    fps_max: int | Unset = UNSET
    fps_median: int | Unset = UNSET
    fps_stability: float | Unset = UNSET
    fps_stability_index: float | Unset = UNSET
    fps_one_percent_low: float | Unset = UNSET
    frametime_95_th_percentile: float | Unset = UNSET
    cpu_usage_min: float | Unset = UNSET
    cpu_usage_avg: float | Unset = UNSET
    cpu_usage_max: float | Unset = UNSET
    cpu_usage_median: float | Unset = UNSET
    gpu_usage_min: float | Unset = UNSET
    gpu_usage_avg: float | Unset = UNSET
    gpu_usage_max: float | Unset = UNSET
    gpu_usage_median: float | Unset = UNSET
    mem_usage_min: int | Unset = UNSET
    mem_usage_avg: int | Unset = UNSET
    mem_usage_max: int | Unset = UNSET
    app_received_bytes: int | Unset = UNSET
    app_sent_bytes: int | Unset = UNSET
    m_a_min: float | Unset = UNSET
    m_a_avg: float | Unset = UNSET
    m_a_max: float | Unset = UNSET
    big_janks_count: int | Unset = UNSET
    big_janks_10_mins: float | Unset = UNSET
    janks_count: int | Unset = UNSET
    janks_10_mins: float | Unset = UNSET
    android_memory_usage: ListSessionMarkersResponse200ItemAndroidMemoryUsage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_session_markers_response_200_item_android_memory_usage import ListSessionMarkersResponse200ItemAndroidMemoryUsage
        session_id = self.session_id

        ts_start = self.ts_start

        ts_end = self.ts_end

        id = self.id

        label = self.label

        group = self.group

        track = self.track

        colour = self.colour

        fps_avg = self.fps_avg

        fps_min = self.fps_min

        fps_max = self.fps_max

        fps_median = self.fps_median

        fps_stability = self.fps_stability

        fps_stability_index = self.fps_stability_index

        fps_one_percent_low = self.fps_one_percent_low

        frametime_95_th_percentile = self.frametime_95_th_percentile

        cpu_usage_min = self.cpu_usage_min

        cpu_usage_avg = self.cpu_usage_avg

        cpu_usage_max = self.cpu_usage_max

        cpu_usage_median = self.cpu_usage_median

        gpu_usage_min = self.gpu_usage_min

        gpu_usage_avg = self.gpu_usage_avg

        gpu_usage_max = self.gpu_usage_max

        gpu_usage_median = self.gpu_usage_median

        mem_usage_min = self.mem_usage_min

        mem_usage_avg = self.mem_usage_avg

        mem_usage_max = self.mem_usage_max

        app_received_bytes = self.app_received_bytes

        app_sent_bytes = self.app_sent_bytes

        m_a_min = self.m_a_min

        m_a_avg = self.m_a_avg

        m_a_max = self.m_a_max

        big_janks_count = self.big_janks_count

        big_janks_10_mins = self.big_janks_10_mins

        janks_count = self.janks_count

        janks_10_mins = self.janks_10_mins

        android_memory_usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.android_memory_usage, Unset):
            android_memory_usage = self.android_memory_usage.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessionId": session_id,
            "tsStart": ts_start,
            "tsEnd": ts_end,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if group is not UNSET:
            field_dict["group"] = group
        if track is not UNSET:
            field_dict["track"] = track
        if colour is not UNSET:
            field_dict["colour"] = colour
        if fps_avg is not UNSET:
            field_dict["fpsAvg"] = fps_avg
        if fps_min is not UNSET:
            field_dict["fpsMin"] = fps_min
        if fps_max is not UNSET:
            field_dict["fpsMax"] = fps_max
        if fps_median is not UNSET:
            field_dict["fpsMedian"] = fps_median
        if fps_stability is not UNSET:
            field_dict["fpsStability"] = fps_stability
        if fps_stability_index is not UNSET:
            field_dict["fpsStabilityIndex"] = fps_stability_index
        if fps_one_percent_low is not UNSET:
            field_dict["fpsOnePercentLow"] = fps_one_percent_low
        if frametime_95_th_percentile is not UNSET:
            field_dict["frametime95thPercentile"] = frametime_95_th_percentile
        if cpu_usage_min is not UNSET:
            field_dict["cpuUsageMin"] = cpu_usage_min
        if cpu_usage_avg is not UNSET:
            field_dict["cpuUsageAvg"] = cpu_usage_avg
        if cpu_usage_max is not UNSET:
            field_dict["cpuUsageMax"] = cpu_usage_max
        if cpu_usage_median is not UNSET:
            field_dict["cpuUsageMedian"] = cpu_usage_median
        if gpu_usage_min is not UNSET:
            field_dict["gpuUsageMin"] = gpu_usage_min
        if gpu_usage_avg is not UNSET:
            field_dict["gpuUsageAvg"] = gpu_usage_avg
        if gpu_usage_max is not UNSET:
            field_dict["gpuUsageMax"] = gpu_usage_max
        if gpu_usage_median is not UNSET:
            field_dict["gpuUsageMedian"] = gpu_usage_median
        if mem_usage_min is not UNSET:
            field_dict["memUsageMin"] = mem_usage_min
        if mem_usage_avg is not UNSET:
            field_dict["memUsageAvg"] = mem_usage_avg
        if mem_usage_max is not UNSET:
            field_dict["memUsageMax"] = mem_usage_max
        if app_received_bytes is not UNSET:
            field_dict["appReceivedBytes"] = app_received_bytes
        if app_sent_bytes is not UNSET:
            field_dict["appSentBytes"] = app_sent_bytes
        if m_a_min is not UNSET:
            field_dict["mAMin"] = m_a_min
        if m_a_avg is not UNSET:
            field_dict["mAAvg"] = m_a_avg
        if m_a_max is not UNSET:
            field_dict["mAMax"] = m_a_max
        if big_janks_count is not UNSET:
            field_dict["bigJanksCount"] = big_janks_count
        if big_janks_10_mins is not UNSET:
            field_dict["bigJanks10Mins"] = big_janks_10_mins
        if janks_count is not UNSET:
            field_dict["janksCount"] = janks_count
        if janks_10_mins is not UNSET:
            field_dict["janks10Mins"] = janks_10_mins
        if android_memory_usage is not UNSET:
            field_dict["androidMemoryUsage"] = android_memory_usage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_session_markers_response_200_item_android_memory_usage import ListSessionMarkersResponse200ItemAndroidMemoryUsage
        d = dict(src_dict)
        session_id = d.pop("sessionId")

        ts_start = d.pop("tsStart")

        ts_end = d.pop("tsEnd")

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        group = d.pop("group", UNSET)

        track = d.pop("track", UNSET)

        colour = d.pop("colour", UNSET)

        fps_avg = d.pop("fpsAvg", UNSET)

        fps_min = d.pop("fpsMin", UNSET)

        fps_max = d.pop("fpsMax", UNSET)

        fps_median = d.pop("fpsMedian", UNSET)

        fps_stability = d.pop("fpsStability", UNSET)

        fps_stability_index = d.pop("fpsStabilityIndex", UNSET)

        fps_one_percent_low = d.pop("fpsOnePercentLow", UNSET)

        frametime_95_th_percentile = d.pop("frametime95thPercentile", UNSET)

        cpu_usage_min = d.pop("cpuUsageMin", UNSET)

        cpu_usage_avg = d.pop("cpuUsageAvg", UNSET)

        cpu_usage_max = d.pop("cpuUsageMax", UNSET)

        cpu_usage_median = d.pop("cpuUsageMedian", UNSET)

        gpu_usage_min = d.pop("gpuUsageMin", UNSET)

        gpu_usage_avg = d.pop("gpuUsageAvg", UNSET)

        gpu_usage_max = d.pop("gpuUsageMax", UNSET)

        gpu_usage_median = d.pop("gpuUsageMedian", UNSET)

        mem_usage_min = d.pop("memUsageMin", UNSET)

        mem_usage_avg = d.pop("memUsageAvg", UNSET)

        mem_usage_max = d.pop("memUsageMax", UNSET)

        app_received_bytes = d.pop("appReceivedBytes", UNSET)

        app_sent_bytes = d.pop("appSentBytes", UNSET)

        m_a_min = d.pop("mAMin", UNSET)

        m_a_avg = d.pop("mAAvg", UNSET)

        m_a_max = d.pop("mAMax", UNSET)

        big_janks_count = d.pop("bigJanksCount", UNSET)

        big_janks_10_mins = d.pop("bigJanks10Mins", UNSET)

        janks_count = d.pop("janksCount", UNSET)

        janks_10_mins = d.pop("janks10Mins", UNSET)

        _android_memory_usage = d.pop("androidMemoryUsage", UNSET)
        android_memory_usage: ListSessionMarkersResponse200ItemAndroidMemoryUsage | Unset
        if isinstance(_android_memory_usage,  Unset):
            android_memory_usage = UNSET
        else:
            android_memory_usage = ListSessionMarkersResponse200ItemAndroidMemoryUsage.from_dict(_android_memory_usage)




        list_session_markers_response_200_item = cls(
            session_id=session_id,
            ts_start=ts_start,
            ts_end=ts_end,
            id=id,
            label=label,
            group=group,
            track=track,
            colour=colour,
            fps_avg=fps_avg,
            fps_min=fps_min,
            fps_max=fps_max,
            fps_median=fps_median,
            fps_stability=fps_stability,
            fps_stability_index=fps_stability_index,
            fps_one_percent_low=fps_one_percent_low,
            frametime_95_th_percentile=frametime_95_th_percentile,
            cpu_usage_min=cpu_usage_min,
            cpu_usage_avg=cpu_usage_avg,
            cpu_usage_max=cpu_usage_max,
            cpu_usage_median=cpu_usage_median,
            gpu_usage_min=gpu_usage_min,
            gpu_usage_avg=gpu_usage_avg,
            gpu_usage_max=gpu_usage_max,
            gpu_usage_median=gpu_usage_median,
            mem_usage_min=mem_usage_min,
            mem_usage_avg=mem_usage_avg,
            mem_usage_max=mem_usage_max,
            app_received_bytes=app_received_bytes,
            app_sent_bytes=app_sent_bytes,
            m_a_min=m_a_min,
            m_a_avg=m_a_avg,
            m_a_max=m_a_max,
            big_janks_count=big_janks_count,
            big_janks_10_mins=big_janks_10_mins,
            janks_count=janks_count,
            janks_10_mins=janks_10_mins,
            android_memory_usage=android_memory_usage,
        )


        list_session_markers_response_200_item.additional_properties = d
        return list_session_markers_response_200_item

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
