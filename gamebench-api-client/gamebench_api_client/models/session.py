from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_app import SessionApp
  from ..models.session_device import SessionDevice
  from ..models.session_owners import SessionOwners
  from ..models.session_tags import SessionTags
  from ..models.session_user import SessionUser





T = TypeVar("T", bound="Session")



@_attrs_define
class Session:
    """ 
        Attributes:
            owners (SessionOwners):
            user (SessionUser):
            app (SessionApp):
            device (SessionDevice):
            id (str | Unset):
            uuid (str | Unset):
            url (str | Unset): Dashboard URL appended server-side by `GET /v2/sessions/{sessionId}`.
            collection_id (str | Unset):
            session_title (None | str | Unset):
            session_date (int | Unset): Unix epoch milliseconds.
            time_pushed (int | Unset): Unix epoch milliseconds.
            time_played (int | Unset): Duration in ms.
            is_shared (bool | Unset):
            is_active (bool | Unset):
            is_charging (bool | Unset):
            imported (bool | Unset):
            tags (SessionTags | Unset):
     """

    owners: SessionOwners
    user: SessionUser
    app: SessionApp
    device: SessionDevice
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
    is_charging: bool | Unset = UNSET
    imported: bool | Unset = UNSET
    tags: SessionTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_app import SessionApp
        from ..models.session_device import SessionDevice
        from ..models.session_owners import SessionOwners
        from ..models.session_tags import SessionTags
        from ..models.session_user import SessionUser
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

        is_charging = self.is_charging

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
        if is_charging is not UNSET:
            field_dict["isCharging"] = is_charging
        if imported is not UNSET:
            field_dict["imported"] = imported
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_app import SessionApp
        from ..models.session_device import SessionDevice
        from ..models.session_owners import SessionOwners
        from ..models.session_tags import SessionTags
        from ..models.session_user import SessionUser
        d = dict(src_dict)
        owners = SessionOwners.from_dict(d.pop("owners"))




        user = SessionUser.from_dict(d.pop("user"))




        app = SessionApp.from_dict(d.pop("app"))




        device = SessionDevice.from_dict(d.pop("device"))




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

        is_charging = d.pop("isCharging", UNSET)

        imported = d.pop("imported", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: SessionTags | Unset
        if isinstance(_tags,  Unset):
            tags = UNSET
        else:
            tags = SessionTags.from_dict(_tags)




        session = cls(
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
            is_charging=is_charging,
            imported=imported,
            tags=tags,
        )


        session.additional_properties = d
        return session

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
