from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCurrentUserResponse200PendingInvitesItem")



@_attrs_define
class GetCurrentUserResponse200PendingInvitesItem:
    """ 
        Attributes:
            id (str | Unset):
            company_name (str | Unset):
     """

    id: str | Unset = UNSET
    company_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_name = self.company_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        company_name = d.pop("companyName", UNSET)

        get_current_user_response_200_pending_invites_item = cls(
            id=id,
            company_name=company_name,
        )


        get_current_user_response_200_pending_invites_item.additional_properties = d
        return get_current_user_response_200_pending_invites_item

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
