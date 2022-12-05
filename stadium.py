from court import Court


class Stadium(Court):

    _name: str
    _common_name: str
    _capacity: int

    def __init__(self, year_built, adress, name, common_name="", capacity=0, length=150, width=68,):
        super().__init__(year_built,adress,length,width)
        self._name = name
        self._common_name = common_name
        if capacity < 0:
            self._capacity = 0
        else:
            self._capacity = capacity


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def common_name(self):
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        self._common_name = common_name

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def __str__(self):
        if self._common_name != "":
            return f"Boisko wybudowane w roku {self._year_built},o długości {self._length} i szerokości {self._width}.\nPole powierzchni {self.area()}.\nAdres:{self._adress}\nNazwa:{self._name}\nNazwa zwyczajowa:{self._common_name}\nPojemność:{self._capacity}"
        else:
            return f"Boisko wybudowane w roku {self._year_built},o długości {self._length} i szerokości {self._width}.\nPole powierzchni {self.area()}.\nAdres:{self._adress}\nNazwa:{self._name}\nPojemność:{self._capacity}"


