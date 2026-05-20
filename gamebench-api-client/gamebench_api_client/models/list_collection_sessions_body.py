from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_collection_sessions_body_app_info import ListCollectionSessionsBodyAppInfo
  from ..models.list_collection_sessions_body_device_info import ListCollectionSessionsBodyDeviceInfo
  from ..models.list_collection_sessions_body_session_info import ListCollectionSessionsBodySessionInfo





T = TypeVar("T", bound="ListCollectionSessionsBody")



@_attrs_define
class ListCollectionSessionsBody:
    """ 
        Attributes:
            apps (list[str] | Unset):
            app_package_names (list[str] | Unset):
            devices (list[str] | Unset):
            manufacturers (list[str] | Unset):
            app_info (ListCollectionSessionsBodyAppInfo | Unset):
            device_info (ListCollectionSessionsBodyDeviceInfo | Unset):
            session_info (ListCollectionSessionsBodySessionInfo | Unset):
            imported (bool | Unset):
     """

    apps: list[str] | Unset = UNSET
    app_package_names: list[str] | Unset = UNSET
    devices: list[str] | Unset = UNSET
    manufacturers: list[str] | Unset = UNSET
    app_info: ListCollectionSessionsBodyAppInfo | Unset = UNSET
    device_info: ListCollectionSessionsBodyDeviceInfo | Unset = UNSET
    session_info: ListCollectionSessionsBodySessionInfo | Unset = UNSET
    imported: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_collection_sessions_body_app_info import ListCollectionSessionsBodyAppInfo
        from ..models.list_collection_sessions_body_device_info import ListCollectionSessionsBodyDeviceInfo
        from ..models.list_collection_sessions_body_session_info import ListCollectionSessionsBodySessionInfo
        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps



        app_package_names: list[str] | Unset = UNSET
        if not isinstance(self.app_package_names, Unset):
            app_package_names = self.app_package_names



        devices: list[str] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices



        manufacturers: list[str] | Unset = UNSET
        if not isinstance(self.manufacturers, Unset):
            manufacturers = self.manufacturers



        app_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_info, Unset):
            app_info = self.app_info.to_dict()

        device_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

        session_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.session_info, Unset):
            session_info = self.session_info.to_dict()

        imported = self.imported


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if apps is not UNSET:
            field_dict["apps"] = apps
        if app_package_names is not UNSET:
            field_dict["appPackageNames"] = app_package_names
        if devices is not UNSET:
            field_dict["devices"] = devices
        if manufacturers is not UNSET:
            field_dict["manufacturers"] = manufacturers
        if app_info is not UNSET:
            field_dict["appInfo"] = app_info
        if device_info is not UNSET:
            field_dict["deviceInfo"] = device_info
        if session_info is not UNSET:
            field_dict["sessionInfo"] = session_info
        if imported is not UNSET:
            field_dict["imported"] = imported

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collection_sessions_body_app_info import ListCollectionSessionsBodyAppInfo
        from ..models.list_collection_sessions_body_device_info import ListCollectionSessionsBodyDeviceInfo
        from ..models.list_collection_sessions_body_session_info import ListCollectionSessionsBodySessionInfo
        d = dict(src_dict)
        apps = cast(list[str], d.pop("apps", UNSET))


        app_package_names = cast(list[str], d.pop("appPackageNames", UNSET))


        devices = cast(list[str], d.pop("devices", UNSET))


        manufacturers = cast(list[str], d.pop("manufacturers", UNSET))


        _app_info = d.pop("appInfo", UNSET)
        app_info: ListCollectionSessionsBodyAppInfo | Unset
        if isinstance(_app_info,  Unset):
            app_info = UNSET
        else:
            app_info = ListCollectionSessionsBodyAppInfo.from_dict(_app_info)




        _device_info = d.pop("deviceInfo", UNSET)
        device_info: ListCollectionSessionsBodyDeviceInfo | Unset
        if isinstance(_device_info,  Unset):
            device_info = UNSET
        else:
            device_info = ListCollectionSessionsBodyDeviceInfo.from_dict(_device_info)




        _session_info = d.pop("sessionInfo", UNSET)
        session_info: ListCollectionSessionsBodySessionInfo | Unset
        if isinstance(_session_info,  Unset):
            session_info = UNSET
        else:
            session_info = ListCollectionSessionsBodySessionInfo.from_dict(_session_info)




        imported = d.pop("imported", UNSET)

        list_collection_sessions_body = cls(
            apps=apps,
            app_package_names=app_package_names,
            devices=devices,
            manufacturers=manufacturers,
            app_info=app_info,
            device_info=device_info,
            session_info=session_info,
            imported=imported,
        )


        list_collection_sessions_body.additional_properties = d
        return list_collection_sessions_body

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
