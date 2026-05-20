from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO






T = TypeVar("T", bound="ImportSessionBody")



@_attrs_define
class ImportSessionBody:
    """ 
        Attributes:
            file (File): The GameBench session zip. Must be larger than
                22 bytes (the size of an empty zip's central
                directory) — anything `<= 22` is rejected as
                "Zip is empty".
            source (str | Unset): Tag the upload's origin. Setting to `"sdk"`
                activates the per-company SDK rate limit and
                license check; other values bypass both. Passed
                through to the queue worker.
                 Example: sdk.
            import_ (Any | Unset): Opaque flag passed through to the parsing
                worker, used to mark this as an "imported"
                session (vs a fresh capture). Worker-defined
                semantics.
            preserve_uuid (Any | Unset): Opaque flag passed through to the parsing
                worker. When set, instructs the worker to reuse
                the UUID inside the zip rather than minting a
                new session UUID.
     """

    file: File
    source: str | Unset = UNSET
    import_: Any | Unset = UNSET
    preserve_uuid: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        source = self.source

        import_ = self.import_

        preserve_uuid = self.preserve_uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
        })
        if source is not UNSET:
            field_dict["source"] = source
        if import_ is not UNSET:
            field_dict["import"] = import_
        if preserve_uuid is not UNSET:
            field_dict["preserveUuid"] = preserve_uuid

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.source, Unset):
            files.append(("source", (None, str(self.source).encode(), "text/plain")))



        if not isinstance(self.import_, Unset):
            files.append(("import", (None, str(self.import_).encode(), "text/plain")))



        if not isinstance(self.preserve_uuid, Unset):
            files.append(("preserveUuid", (None, str(self.preserve_uuid).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        source = d.pop("source", UNSET)

        import_ = d.pop("import", UNSET)

        preserve_uuid = d.pop("preserveUuid", UNSET)

        import_session_body = cls(
            file=file,
            source=source,
            import_=import_,
            preserve_uuid=preserve_uuid,
        )


        import_session_body.additional_properties = d
        return import_session_body

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
