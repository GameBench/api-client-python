from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_collections_response_200_collections_item import ListCollectionsResponse200CollectionsItem





T = TypeVar("T", bound="ListCollectionsResponse200")



@_attrs_define
class ListCollectionsResponse200:
    """ 
        Attributes:
            collections (list[ListCollectionsResponse200CollectionsItem]):
            count (int | Unset): Total matching collections. Company-scoped path only.
     """

    collections: list[ListCollectionsResponse200CollectionsItem]
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_collections_response_200_collections_item import ListCollectionsResponse200CollectionsItem
        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)



        count = self.count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "collections": collections,
        })
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_collections_response_200_collections_item import ListCollectionsResponse200CollectionsItem
        d = dict(src_dict)
        collections = []
        _collections = d.pop("collections")
        for collections_item_data in (_collections):
            collections_item = ListCollectionsResponse200CollectionsItem.from_dict(collections_item_data)



            collections.append(collections_item)


        count = d.pop("count", UNSET)

        list_collections_response_200 = cls(
            collections=collections,
            count=count,
        )


        list_collections_response_200.additional_properties = d
        return list_collections_response_200

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
