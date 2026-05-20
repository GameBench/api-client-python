from enum import Enum

class ListCollectionsResponse200CollectionsItemRole(str, Enum):
    EDITOR = "editor"
    EDITOR_OWN_DATA_ONLY = "editor-own-data-only"
    MANAGER = "manager"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
