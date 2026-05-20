from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListCollectionSessionsBodyDeviceInfo")



@_attrs_define
class ListCollectionSessionsBodyDeviceInfo:
    """ 
        Attributes:
            model (list[str] | Unset):
            manufacturer (list[str] | Unset):
     """

    model: list[str] | Unset = UNSET
    manufacturer: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model: list[str] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model



        manufacturer: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer, Unset):
            manufacturer = self.manufacturer




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if model is not UNSET:
            field_dict["model"] = model
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = cast(list[str], d.pop("model", UNSET))


        manufacturer = cast(list[str], d.pop("manufacturer", UNSET))


        list_collection_sessions_body_device_info = cls(
            model=model,
            manufacturer=manufacturer,
        )


        list_collection_sessions_body_device_info.additional_properties = d
        return list_collection_sessions_body_device_info

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
