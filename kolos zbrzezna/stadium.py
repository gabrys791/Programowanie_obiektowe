from __future__ import annotations
from court import Court


class Stadium(Court):
    _name: str
    _common_name: str
    _capacity: int

    def __init__(
        self,
        address: str,
        year_built: int,
        name: str,
        common_name: str = "",
        capacity: int = 0,
        width: float = 68.0,
        length: float = 150.0,
    ) -> None:
        super().__init__(address, year_built, width, length)
        self._name = name
        self._common_name = common_name
        self._capacity = capacity

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def set_name(self, name: str) -> None:
        self._name = name

    @property
    def common_name(self) -> str:
        return self._common_name

    @common_name.setter
    def common_name(self, common_name: str) -> None:
        self._common_name = common_name

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if capacity < 0:
            self._capacity = 0
        else:
            self._capacity = capacity

    def __eq__(self, __o: Court) -> bool:
        return self.area() == __o.area() and self.capacity == __o.capacity

    def __ne__(self, __o: Court) -> bool:
        return self.area() != __o.area() and self.capacity != __o.capacity

    def __str__(self) -> str:
        ret = f"Boisko wybudowane w {self.year_built}, o długości {self.length} i szerokości {self.width} metrów.\nPole powierzchni: {self.area()} mkw.\nAdres: {self.address}.\nNazwa: {self.name}.\n"
        if self.common_name:
            ret += f"Nazwa zwyczajowa: {self.common_name}\n"
        return ret + f"Pojemność stadionu {self.capacity}.\n"
