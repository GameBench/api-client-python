from enum import Enum

class GetSessionFrametimesFormat(str, Enum):
    CSV = "csv"

    def __str__(self) -> str:
        return str(self.value)
