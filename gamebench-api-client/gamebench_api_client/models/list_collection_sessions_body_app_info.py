from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListCollectionSessionsBodyAppInfo")



@_attrs_define
class ListCollectionSessionsBodyAppInfo:
    """ 
        Attributes:
            name (list[str] | Unset):
            version (list[str] | Unset):
            package (list[str] | Unset):
     """

    name: list[str] | Unset = UNSET
    version: list[str] | Unset = UNSET
    package: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: list[str] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name



        version: list[str] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version



        package: list[str] | Unset = UNSET
        if not isinstance(self.package, Unset):
            package = self.package




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if package is not UNSET:
            field_dict["package"] = package

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = cast(list[str], d.pop("name", UNSET))


        version = cast(list[str], d.pop("version", UNSET))


        package = cast(list[str], d.pop("package", UNSET))


        list_collection_sessions_body_app_info = cls(
            name=name,
            version=version,
            package=package,
        )


        list_collection_sessions_body_app_info.additional_properties = d
        return list_collection_sessions_body_app_info

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
