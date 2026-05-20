from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListSessionAdditionalFilesResponse200AdditionalFilesItem")



@_attrs_define
class ListSessionAdditionalFilesResponse200AdditionalFilesItem:
    """ 
        Attributes:
            filename (str):
            type_ (str): MIME type as captured by the recording
                tool (verbatim — not validated server-side).
            size (int | Unset): Size in bytes, sourced from the file-storage
                metadata. May be omitted if unknown.
     """

    filename: str
    type_: str
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        type_ = self.type_

        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "filename": filename,
            "type": type_,
        })
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        type_ = d.pop("type")

        size = d.pop("size", UNSET)

        list_session_additional_files_response_200_additional_files_item = cls(
            filename=filename,
            type_=type_,
            size=size,
        )


        list_session_additional_files_response_200_additional_files_item.additional_properties = d
        return list_session_additional_files_response_200_additional_files_item

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
