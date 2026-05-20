from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.page_results_item import PageResultsItem





T = TypeVar("T", bound="PageOfUser")



@_attrs_define
class PageOfUser:
    """ 
        Attributes:
            results (list[PageResultsItem]):
            total_hits (int):
            total_pages (int):
            page (int):
            size (int):
     """

    results: list[PageResultsItem]
    total_hits: int
    total_pages: int
    page: int
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.page_results_item import PageResultsItem
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        total_hits = self.total_hits

        total_pages = self.total_pages

        page = self.page

        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
            "totalHits": total_hits,
            "totalPages": total_pages,
            "page": page,
            "size": size,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_results_item import PageResultsItem
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = PageResultsItem.from_dict(results_item_data)



            results.append(results_item)


        total_hits = d.pop("totalHits")

        total_pages = d.pop("totalPages")

        page = d.pop("page")

        size = d.pop("size")

        page_of_user = cls(
            results=results,
            total_hits=total_hits,
            total_pages=total_pages,
            page=page,
            size=size,
        )


        page_of_user.additional_properties = d
        return page_of_user

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
