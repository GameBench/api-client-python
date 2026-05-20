from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SessionApp")



@_attrs_define
class SessionApp:
    """ 
        Attributes:
            name (str | Unset):
            package_name (str | Unset):
            version (str | Unset):
            version_code (int | Unset):
            version_code_str (str | Unset):
            icon_url (str | Unset):
     """

    name: str | Unset = UNSET
    package_name: str | Unset = UNSET
    version: str | Unset = UNSET
    version_code: int | Unset = UNSET
    version_code_str: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        package_name = self.package_name

        version = self.version

        version_code = self.version_code

        version_code_str = self.version_code_str

        icon_url = self.icon_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if version is not UNSET:
            field_dict["version"] = version
        if version_code is not UNSET:
            field_dict["versionCode"] = version_code
        if version_code_str is not UNSET:
            field_dict["versionCodeStr"] = version_code_str
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        package_name = d.pop("packageName", UNSET)

        version = d.pop("version", UNSET)

        version_code = d.pop("versionCode", UNSET)

        version_code_str = d.pop("versionCodeStr", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        session_app = cls(
            name=name,
            package_name=package_name,
            version=version,
            version_code=version_code,
            version_code_str=version_code_str,
            icon_url=icon_url,
        )


        session_app.additional_properties = d
        return session_app

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
