from HardwareMonitor._util.types import IReadOnlyList
from HardwareMonitor.Hardware import ISettings
from typing import overload, overload, Tuple, Set, Iterable, List


class AeroCoolGroup:
    def __init__(self, settings: ISettings): ...
    def Close(self) -> None: ...
    @property
    def Hardware(self) -> IReadOnlyList: ...
    def GetReport(self) -> str: ...
