from HardwareMonitor._util.types import IReadOnlyList
from typing import overload, Tuple, Set, Iterable, List


class AquaComputerGroup:
    def __init__(self, settings: ISettings): ...
    def Close(self) -> None: ...
    @property
    def Hardware(self) -> IReadOnlyList: ...
    def GetReport(self) -> str: ...
