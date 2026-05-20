from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_session_additional_files_response_200_additional_files_item import ListSessionAdditionalFilesResponse200AdditionalFilesItem





T = TypeVar("T", bound="ListSessionAdditionalFilesResponse200")



@_attrs_define
class ListSessionAdditionalFilesResponse200:
    """ 
        Attributes:
            additional_files (list[ListSessionAdditionalFilesResponse200AdditionalFilesItem]):
     """

    additional_files: list[ListSessionAdditionalFilesResponse200AdditionalFilesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_session_additional_files_response_200_additional_files_item import ListSessionAdditionalFilesResponse200AdditionalFilesItem
        additional_files = []
        for additional_files_item_data in self.additional_files:
            additional_files_item = additional_files_item_data.to_dict()
            additional_files.append(additional_files_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "additionalFiles": additional_files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_session_additional_files_response_200_additional_files_item import ListSessionAdditionalFilesResponse200AdditionalFilesItem
        d = dict(src_dict)
        additional_files = []
        _additional_files = d.pop("additionalFiles")
        for additional_files_item_data in (_additional_files):
            additional_files_item = ListSessionAdditionalFilesResponse200AdditionalFilesItem.from_dict(additional_files_item_data)



            additional_files.append(additional_files_item)


        list_session_additional_files_response_200 = cls(
            additional_files=additional_files,
        )


        list_session_additional_files_response_200.additional_properties = d
        return list_session_additional_files_response_200

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
