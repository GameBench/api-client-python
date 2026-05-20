from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_session_response_200_app import GetSessionResponse200App
  from ..models.get_session_response_200_device import GetSessionResponse200Device
  from ..models.get_session_response_200_owners import GetSessionResponse200Owners
  from ..models.get_session_response_200_tags import GetSessionResponse200Tags
  from ..models.get_session_response_200_user import GetSessionResponse200User





T = TypeVar("T", bound="GetSessionResponse200")



@_attrs_define
class GetSessionResponse200:
    """ 
        Attributes:
            owners (GetSessionResponse200Owners):
            user (GetSessionResponse200User):
            app (GetSessionResponse200App):
            device (GetSessionResponse200Device):
            id (str | Unset):
            uuid (str | Unset):
            url (str | Unset): Dashboard URL appended server-side. Includes
                `collectionId` and `companyId` query params when
                known.
            collection_id (str | Unset):
            session_title (None | str | Unset):
            session_date (int | Unset): Unix epoch milliseconds.
            time_pushed (int | Unset): Unix epoch milliseconds.
            time_played (int | Unset): Duration in ms.
            is_shared (bool | Unset):
            is_active (bool | Unset):
            imported (bool | Unset):
            tags (GetSessionResponse200Tags | Unset):
     """

    owners: GetSessionResponse200Owners
    user: GetSessionResponse200User
    app: GetSessionResponse200App
    device: GetSessionResponse200Device
    id: str | Unset = UNSET
    uuid: str | Unset = UNSET
    url: str | Unset = UNSET
    collection_id: str | Unset = UNSET
    session_title: None | str | Unset = UNSET
    session_date: int | Unset = UNSET
    time_pushed: int | Unset = UNSET
    time_played: int | Unset = UNSET
    is_shared: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    imported: bool | Unset = UNSET
    tags: GetSessionResponse200Tags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_session_response_200_app import GetSessionResponse200App
        from ..models.get_session_response_200_device import GetSessionResponse200Device
        from ..models.get_session_response_200_owners import GetSessionResponse200Owners
        from ..models.get_session_response_200_tags import GetSessionResponse200Tags
        from ..models.get_session_response_200_user import GetSessionResponse200User
        owners = self.owners.to_dict()

        user = self.user.to_dict()

        app = self.app.to_dict()

        device = self.device.to_dict()

        id = self.id

        uuid = self.uuid

        url = self.url

        collection_id = self.collection_id

        session_title: None | str | Unset
        if isinstance(self.session_title, Unset):
            session_title = UNSET
        else:
            session_title = self.session_title

        session_date = self.session_date

        time_pushed = self.time_pushed

        time_played = self.time_played

        is_shared = self.is_shared

        is_active = self.is_active

        imported = self.imported

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "owners": owners,
            "user": user,
            "app": app,
            "device": device,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if url is not UNSET:
            field_dict["url"] = url
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id
        if session_title is not UNSET:
            field_dict["sessionTitle"] = session_title
        if session_date is not UNSET:
            field_dict["sessionDate"] = session_date
        if time_pushed is not UNSET:
            field_dict["timePushed"] = time_pushed
        if time_played is not UNSET:
            field_dict["timePlayed"] = time_played
        if is_shared is not UNSET:
            field_dict["isShared"] = is_shared
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if imported is not UNSET:
            field_dict["imported"] = imported
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_session_response_200_app import GetSessionResponse200App
        from ..models.get_session_response_200_device import GetSessionResponse200Device
        from ..models.get_session_response_200_owners import GetSessionResponse200Owners
        from ..models.get_session_response_200_tags import GetSessionResponse200Tags
        from ..models.get_session_response_200_user import GetSessionResponse200User
        d = dict(src_dict)
        owners = GetSessionResponse200Owners.from_dict(d.pop("owners"))




        user = GetSessionResponse200User.from_dict(d.pop("user"))




        app = GetSessionResponse200App.from_dict(d.pop("app"))




        device = GetSessionResponse200Device.from_dict(d.pop("device"))




        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        url = d.pop("url", UNSET)

        collection_id = d.pop("collectionId", UNSET)

        def _parse_session_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_title = _parse_session_title(d.pop("sessionTitle", UNSET))


        session_date = d.pop("sessionDate", UNSET)

        time_pushed = d.pop("timePushed", UNSET)

        time_played = d.pop("timePlayed", UNSET)

        is_shared = d.pop("isShared", UNSET)

        is_active = d.pop("isActive", UNSET)

        imported = d.pop("imported", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: GetSessionResponse200Tags | Unset
        if isinstance(_tags,  Unset):
            tags = UNSET
        else:
            tags = GetSessionResponse200Tags.from_dict(_tags)




        get_session_response_200 = cls(
            owners=owners,
            user=user,
            app=app,
            device=device,
            id=id,
            uuid=uuid,
            url=url,
            collection_id=collection_id,
            session_title=session_title,
            session_date=session_date,
            time_pushed=time_pushed,
            time_played=time_played,
            is_shared=is_shared,
            is_active=is_active,
            imported=imported,
            tags=tags,
        )


        get_session_response_200.additional_properties = d
        return get_session_response_200

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
