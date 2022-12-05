from __future__ import annotations
from datetime import date


class Court:
    _width: float
    _length: float
    _address: str
    _year_built: int

    def __init__(
        self, address: str, year_built: int, width: float = 68.0, length: float = 150.0
    ) -> None:
        self._width = width
        self._length = length
        self._address = address
        self._year_built = year_built

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        if width < 45 or width > 90:
            self._width = 68
        else:
            self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        if length < 90 or length > 120:
            self._length = 150
        else:
            self._length = length

    @property
    def address(self):
        return self._address

    @address.setter
    def adrress(self, address: str) -> None:
        if type(address) != str:
            raise ValueError("Address should be a string")
        else:
            self._address = address

    @property
    def year_built(self):
        return self._year_built

    @year_built.setter
    def year_built(self, year_built: int) -> None:
        if type(year_built) != int:
            raise ValueError("Year should be an int")
        else:
            self._year_built = year_built

    def area(self) -> float:
        return self.width * self.length

    @staticmethod
    def validate(cls: Court) -> None:
        current_year = date.today().year
        if cls.year_built < 0 or cls.year_built > current_year:
            cls._year_built = current_year

    def __str__(self) -> str:
        return f"Boisko wybudowane w {self.year_built}, o długości {self.length} i szerokości {self.width} metrów.\nPole powierzchni: {self.area()} mkw.\nAdres: {self.address}.\n"

    def __eq__(self, __o: Court) -> bool:
        return self.area() == __o.area()

    def __ne__(self, __o: Court) -> bool:
        return self.area() != __o.area()
