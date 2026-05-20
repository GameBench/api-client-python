from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_collections_response_200_collections_item_role import ListCollectionsResponse200CollectionsItemRole
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_collections_response_200_collections_item_permissions import ListCollectionsResponse200CollectionsItemPermissions





T = TypeVar("T", bound="ListCollectionsResponse200CollectionsItem")



@_attrs_define
class ListCollectionsResponse200CollectionsItem:
    """ 
        Attributes:
            id (str):
            name (str):
            app_package_names (list[str]):
            editable (bool):
            session_count (int):
            unique_app_count (int):
            unique_device_count (int):
            company_name (str):
            company_id (str):
            role (ListCollectionsResponse200CollectionsItemRole | Unset): User-scoped path only. The caller's role on this
                collection.
            permissions (ListCollectionsResponse200CollectionsItemPermissions | Unset): User-scoped path only. Permissions
                derived from `role`.
     """

    id: str
    name: str
    app_package_names: list[str]
    editable: bool
    session_count: int
    unique_app_count: int
    unique_device_count: int
    company_name: str
    company_id: str
    role: ListCollectionsResponse200CollectionsItemRole | Unset = UNSET
    permissions: ListCollectionsResponse200CollectionsItemPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_collections_response_200_collections_item_permissions import ListCollectionsResponse200CollectionsItemPermissions
        id = self.id

        name = self.name

        app_package_names = self.app_package_names



        editable = self.editable

        session_count = self.session_count

        unique_app_count = self.unique_app_count

        unique_device_count = self.unique_device_count

        company_name = self.company_name

        company_id = self.company_id

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value


        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "appPackageNames": app_package_names,
            "editable": editable,
            "sessionCount": session_count,
            "uniqueAppCount": unique_app_count,
            "uniqueDeviceCount": unique_device_count,
            "companyName": company_name,
            "companyId": company_id,
        })
        if role is not UNSET:
            field_dict["role"] = role
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collections_response_200_collections_item_permissions import ListCollectionsResponse200CollectionsItemPermissions
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        app_package_names = cast(list[str], d.pop("appPackageNames"))


        editable = d.pop("editable")

        session_count = d.pop("sessionCount")

        unique_app_count = d.pop("uniqueAppCount")

        unique_device_count = d.pop("uniqueDeviceCount")

        company_name = d.pop("companyName")

        company_id = d.pop("companyId")

        _role = d.pop("role", UNSET)
        role: ListCollectionsResponse200CollectionsItemRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = ListCollectionsResponse200CollectionsItemRole(_role)




        _permissions = d.pop("permissions", UNSET)
        permissions: ListCollectionsResponse200CollectionsItemPermissions | Unset
        if isinstance(_permissions,  Unset):
            permissions = UNSET
        else:
            permissions = ListCollectionsResponse200CollectionsItemPermissions.from_dict(_permissions)




        list_collections_response_200_collections_item = cls(
            id=id,
            name=name,
            app_package_names=app_package_names,
            editable=editable,
            session_count=session_count,
            unique_app_count=unique_app_count,
            unique_device_count=unique_device_count,
            company_name=company_name,
            company_id=company_id,
            role=role,
            permissions=permissions,
        )


        list_collections_response_200_collections_item.additional_properties = d
        return list_collections_response_200_collections_item

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
