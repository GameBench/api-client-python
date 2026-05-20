from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_current_user_response_200_auth_policy import GetCurrentUserResponse200AuthPolicy
  from ..models.get_current_user_response_200_collections_item import GetCurrentUserResponse200CollectionsItem
  from ..models.get_current_user_response_200_company import GetCurrentUserResponse200Company
  from ..models.get_current_user_response_200_notification_counts import GetCurrentUserResponse200NotificationCounts
  from ..models.get_current_user_response_200_pending_invites_item import GetCurrentUserResponse200PendingInvitesItem
  from ..models.get_current_user_response_200_person import GetCurrentUserResponse200Person





T = TypeVar("T", bound="GetCurrentUserResponse200")



@_attrs_define
class GetCurrentUserResponse200:
    """ 
        Attributes:
            id (str | Unset):
            role (str | Unset):
            person (GetCurrentUserResponse200Person | Unset):
            company (GetCurrentUserResponse200Company | Unset):
            pending_invites (list[GetCurrentUserResponse200PendingInvitesItem] | Unset):
            notification_counts (GetCurrentUserResponse200NotificationCounts | Unset):
            collections (list[GetCurrentUserResponse200CollectionsItem] | Unset):
            auth_policy (GetCurrentUserResponse200AuthPolicy | Unset):
     """

    id: str | Unset = UNSET
    role: str | Unset = UNSET
    person: GetCurrentUserResponse200Person | Unset = UNSET
    company: GetCurrentUserResponse200Company | Unset = UNSET
    pending_invites: list[GetCurrentUserResponse200PendingInvitesItem] | Unset = UNSET
    notification_counts: GetCurrentUserResponse200NotificationCounts | Unset = UNSET
    collections: list[GetCurrentUserResponse200CollectionsItem] | Unset = UNSET
    auth_policy: GetCurrentUserResponse200AuthPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_current_user_response_200_auth_policy import GetCurrentUserResponse200AuthPolicy
        from ..models.get_current_user_response_200_collections_item import GetCurrentUserResponse200CollectionsItem
        from ..models.get_current_user_response_200_company import GetCurrentUserResponse200Company
        from ..models.get_current_user_response_200_notification_counts import GetCurrentUserResponse200NotificationCounts
        from ..models.get_current_user_response_200_pending_invites_item import GetCurrentUserResponse200PendingInvitesItem
        from ..models.get_current_user_response_200_person import GetCurrentUserResponse200Person
        id = self.id

        role = self.role

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        pending_invites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pending_invites, Unset):
            pending_invites = []
            for pending_invites_item_data in self.pending_invites:
                pending_invites_item = pending_invites_item_data.to_dict()
                pending_invites.append(pending_invites_item)



        notification_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_counts, Unset):
            notification_counts = self.notification_counts.to_dict()

        collections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collections, Unset):
            collections = []
            for collections_item_data in self.collections:
                collections_item = collections_item_data.to_dict()
                collections.append(collections_item)



        auth_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_policy, Unset):
            auth_policy = self.auth_policy.to_dict()


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
        if pending_invites is not UNSET:
            field_dict["pendingInvites"] = pending_invites
        if notification_counts is not UNSET:
            field_dict["notificationCounts"] = notification_counts
        if collections is not UNSET:
            field_dict["collections"] = collections
        if auth_policy is not UNSET:
            field_dict["authPolicy"] = auth_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_current_user_response_200_auth_policy import GetCurrentUserResponse200AuthPolicy
        from ..models.get_current_user_response_200_collections_item import GetCurrentUserResponse200CollectionsItem
        from ..models.get_current_user_response_200_company import GetCurrentUserResponse200Company
        from ..models.get_current_user_response_200_notification_counts import GetCurrentUserResponse200NotificationCounts
        from ..models.get_current_user_response_200_pending_invites_item import GetCurrentUserResponse200PendingInvitesItem
        from ..models.get_current_user_response_200_person import GetCurrentUserResponse200Person
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        role = d.pop("role", UNSET)

        _person = d.pop("person", UNSET)
        person: GetCurrentUserResponse200Person | Unset
        if isinstance(_person,  Unset):
            person = UNSET
        else:
            person = GetCurrentUserResponse200Person.from_dict(_person)




        _company = d.pop("company", UNSET)
        company: GetCurrentUserResponse200Company | Unset
        if isinstance(_company,  Unset):
            company = UNSET
        else:
            company = GetCurrentUserResponse200Company.from_dict(_company)




        _pending_invites = d.pop("pendingInvites", UNSET)
        pending_invites: list[GetCurrentUserResponse200PendingInvitesItem] | Unset = UNSET
        if _pending_invites is not UNSET:
            pending_invites = []
            for pending_invites_item_data in _pending_invites:
                pending_invites_item = GetCurrentUserResponse200PendingInvitesItem.from_dict(pending_invites_item_data)



                pending_invites.append(pending_invites_item)


        _notification_counts = d.pop("notificationCounts", UNSET)
        notification_counts: GetCurrentUserResponse200NotificationCounts | Unset
        if isinstance(_notification_counts,  Unset):
            notification_counts = UNSET
        else:
            notification_counts = GetCurrentUserResponse200NotificationCounts.from_dict(_notification_counts)




        _collections = d.pop("collections", UNSET)
        collections: list[GetCurrentUserResponse200CollectionsItem] | Unset = UNSET
        if _collections is not UNSET:
            collections = []
            for collections_item_data in _collections:
                collections_item = GetCurrentUserResponse200CollectionsItem.from_dict(collections_item_data)



                collections.append(collections_item)


        _auth_policy = d.pop("authPolicy", UNSET)
        auth_policy: GetCurrentUserResponse200AuthPolicy | Unset
        if isinstance(_auth_policy,  Unset):
            auth_policy = UNSET
        else:
            auth_policy = GetCurrentUserResponse200AuthPolicy.from_dict(_auth_policy)




        get_current_user_response_200 = cls(
            id=id,
            role=role,
            person=person,
            company=company,
            pending_invites=pending_invites,
            notification_counts=notification_counts,
            collections=collections,
            auth_policy=auth_policy,
        )


        get_current_user_response_200.additional_properties = d
        return get_current_user_response_200

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
