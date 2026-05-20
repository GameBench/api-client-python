from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ListSessionNotesResponse200Item")



@_attrs_define
class ListSessionNotesResponse200Item:
    """ 
        Attributes:
            id (str):
            session_id (str):
            author_id (str): User id of the note's author.
            title (str):
            message (str):
            first_name (str | Unset):
            surname (str | Unset):
            date (int | Unset): Unix epoch milliseconds.
            created_date_timestamp (datetime.datetime | Unset):
            user_deleted (bool | Unset):
     """

    id: str
    session_id: str
    author_id: str
    title: str
    message: str
    first_name: str | Unset = UNSET
    surname: str | Unset = UNSET
    date: int | Unset = UNSET
    created_date_timestamp: datetime.datetime | Unset = UNSET
    user_deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        session_id = self.session_id

        author_id = self.author_id

        title = self.title

        message = self.message

        first_name = self.first_name

        surname = self.surname

        date = self.date

        created_date_timestamp: str | Unset = UNSET
        if not isinstance(self.created_date_timestamp, Unset):
            created_date_timestamp = self.created_date_timestamp.isoformat()

        user_deleted = self.user_deleted


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "sessionId": session_id,
            "authorId": author_id,
            "title": title,
            "message": message,
        })
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if date is not UNSET:
            field_dict["date"] = date
        if created_date_timestamp is not UNSET:
            field_dict["createdDateTimestamp"] = created_date_timestamp
        if user_deleted is not UNSET:
            field_dict["userDeleted"] = user_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("sessionId")

        author_id = d.pop("authorId")

        title = d.pop("title")

        message = d.pop("message")

        first_name = d.pop("firstName", UNSET)

        surname = d.pop("surname", UNSET)

        date = d.pop("date", UNSET)

        _created_date_timestamp = d.pop("createdDateTimestamp", UNSET)
        created_date_timestamp: datetime.datetime | Unset
        if isinstance(_created_date_timestamp,  Unset):
            created_date_timestamp = UNSET
        else:
            created_date_timestamp = isoparse(_created_date_timestamp)




        user_deleted = d.pop("userDeleted", UNSET)

        list_session_notes_response_200_item = cls(
            id=id,
            session_id=session_id,
            author_id=author_id,
            title=title,
            message=message,
            first_name=first_name,
            surname=surname,
            date=date,
            created_date_timestamp=created_date_timestamp,
            user_deleted=user_deleted,
        )


        list_session_notes_response_200_item.additional_properties = d
        return list_session_notes_response_200_item

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
