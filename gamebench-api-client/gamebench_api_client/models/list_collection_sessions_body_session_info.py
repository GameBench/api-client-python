from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListCollectionSessionsBodySessionInfo")



@_attrs_define
class ListCollectionSessionsBodySessionInfo:
    """ 
        Attributes:
            duration_start (int | Unset): Session duration lower bound in ms.
            duration_end (int | Unset): Session duration upper bound in ms.
            title (str | Unset): Wildcard-matched session title.
            notes (str | Unset): Wildcard-matched session notes.
            user_email (list[str] | Unset):
            date_start (int | Unset): Unix epoch milliseconds.
            date_end (int | Unset): Unix epoch milliseconds.
            time_pushed_start (int | Unset): Unix epoch milliseconds.
            time_pushed_end (int | Unset): Unix epoch milliseconds.
            shared (bool | Unset):
            screenshots (bool | Unset):
            markers (bool | Unset):
            imported (bool | Unset):
            wireless (bool | Unset):
            tags (list[str] | Unset):
            recording_software (list[str] | Unset):
     """

    duration_start: int | Unset = UNSET
    duration_end: int | Unset = UNSET
    title: str | Unset = UNSET
    notes: str | Unset = UNSET
    user_email: list[str] | Unset = UNSET
    date_start: int | Unset = UNSET
    date_end: int | Unset = UNSET
    time_pushed_start: int | Unset = UNSET
    time_pushed_end: int | Unset = UNSET
    shared: bool | Unset = UNSET
    screenshots: bool | Unset = UNSET
    markers: bool | Unset = UNSET
    imported: bool | Unset = UNSET
    wireless: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    recording_software: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        duration_start = self.duration_start

        duration_end = self.duration_end

        title = self.title

        notes = self.notes

        user_email: list[str] | Unset = UNSET
        if not isinstance(self.user_email, Unset):
            user_email = self.user_email



        date_start = self.date_start

        date_end = self.date_end

        time_pushed_start = self.time_pushed_start

        time_pushed_end = self.time_pushed_end

        shared = self.shared

        screenshots = self.screenshots

        markers = self.markers

        imported = self.imported

        wireless = self.wireless

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        recording_software: list[str] | Unset = UNSET
        if not isinstance(self.recording_software, Unset):
            recording_software = self.recording_software




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if duration_start is not UNSET:
            field_dict["durationStart"] = duration_start
        if duration_end is not UNSET:
            field_dict["durationEnd"] = duration_end
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email
        if date_start is not UNSET:
            field_dict["dateStart"] = date_start
        if date_end is not UNSET:
            field_dict["dateEnd"] = date_end
        if time_pushed_start is not UNSET:
            field_dict["timePushedStart"] = time_pushed_start
        if time_pushed_end is not UNSET:
            field_dict["timePushedEnd"] = time_pushed_end
        if shared is not UNSET:
            field_dict["shared"] = shared
        if screenshots is not UNSET:
            field_dict["screenshots"] = screenshots
        if markers is not UNSET:
            field_dict["markers"] = markers
        if imported is not UNSET:
            field_dict["imported"] = imported
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if tags is not UNSET:
            field_dict["tags"] = tags
        if recording_software is not UNSET:
            field_dict["recordingSoftware"] = recording_software

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_start = d.pop("durationStart", UNSET)

        duration_end = d.pop("durationEnd", UNSET)

        title = d.pop("title", UNSET)

        notes = d.pop("notes", UNSET)

        user_email = cast(list[str], d.pop("userEmail", UNSET))


        date_start = d.pop("dateStart", UNSET)

        date_end = d.pop("dateEnd", UNSET)

        time_pushed_start = d.pop("timePushedStart", UNSET)

        time_pushed_end = d.pop("timePushedEnd", UNSET)

        shared = d.pop("shared", UNSET)

        screenshots = d.pop("screenshots", UNSET)

        markers = d.pop("markers", UNSET)

        imported = d.pop("imported", UNSET)

        wireless = d.pop("wireless", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        recording_software = cast(list[str], d.pop("recordingSoftware", UNSET))


        list_collection_sessions_body_session_info = cls(
            duration_start=duration_start,
            duration_end=duration_end,
            title=title,
            notes=notes,
            user_email=user_email,
            date_start=date_start,
            date_end=date_end,
            time_pushed_start=time_pushed_start,
            time_pushed_end=time_pushed_end,
            shared=shared,
            screenshots=screenshots,
            markers=markers,
            imported=imported,
            wireless=wireless,
            tags=tags,
            recording_software=recording_software,
        )


        list_collection_sessions_body_session_info.additional_properties = d
        return list_collection_sessions_body_session_info

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
