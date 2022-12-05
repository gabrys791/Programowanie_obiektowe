import datetime


class Court:
    _width: float
    _length: float
    _adress: str
    _year_built: int

    def __init__(self, year_built, adress, length=150, width=68):

        if length < 90 or length > 120:
            self._length = 150
        else:
            self._length = length

        if width < 45 or width > 90:
            self.width = 68
        else:
            self.width = width

        self._adress = adress
        self._year_built = year_built

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def year_built(self):
        return self._year_built

    @year_built.setter
    def year_built(self, value):
        self._year_built = value

    def area(self):
        area = self._length * self._width
        return area

    @staticmethod
    def validate(cls):
        if cls.year_built > 2022 or cls.year_built < 0:
            cls._year_built = datetime.date.today().year


    def __str__(self):
        return f"Boisko wybudowane w roku {self._year_built},o długości {self._length} i szerokości {self._width}.\nPole powierzchni {self.area()}.\nAdres:{self._adress}"






