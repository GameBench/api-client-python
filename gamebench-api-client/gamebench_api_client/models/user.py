from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_company import UserCompany
  from ..models.user_person import UserPerson





T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ 
        Attributes:
            id (str | Unset):
            role (str | Unset):
            person (UserPerson | Unset):
            company (UserCompany | Unset):
     """

    id: str | Unset = UNSET
    role: str | Unset = UNSET
    person: UserPerson | Unset = UNSET
    company: UserCompany | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_company import UserCompany
        from ..models.user_person import UserPerson
        id = self.id

        role = self.role

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if role is not UNSET:
            field_dict["role"] = role
        if person is not UNSET:
            field_dict["person"] = person
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_company import UserCompany
        from ..models.user_person import UserPerson
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        role = d.pop("role", UNSET)

        _person = d.pop("person", UNSET)
        person: UserPerson | Unset
        if isinstance(_person,  Unset):
            person = UNSET
        else:
            person = UserPerson.from_dict(_person)




        _company = d.pop("company", UNSET)
        company: UserCompany | Unset
        if isinstance(_company,  Unset):
            company = UNSET
        else:
            company = UserCompany.from_dict(_company)




        user = cls(
            id=id,
            role=role,
            person=person,
            company=company,
        )


        user.additional_properties = d
        return user

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
