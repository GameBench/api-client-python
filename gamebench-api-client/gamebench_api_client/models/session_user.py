from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SessionUser")



@_attrs_define
class SessionUser:
    """ 
        Attributes:
            data_set (str | Unset):
            user_play_account (str | Unset):
     """

    data_set: str | Unset = UNSET
    user_play_account: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data_set = self.data_set

        user_play_account = self.user_play_account


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if user_play_account is not UNSET:
            field_dict["userPlayAccount"] = user_play_account

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_set = d.pop("dataSet", UNSET)

        user_play_account = d.pop("userPlayAccount", UNSET)

        session_user = cls(
            data_set=data_set,
            user_play_account=user_play_account,
        )


        session_user.additional_properties = d
        return session_user

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
