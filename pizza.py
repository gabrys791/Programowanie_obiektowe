from typing import Dict
import math


class Pizza:
    __price: float
    __toppings: Dict[str, int]
    __diameter: float

    def __init__(self, diameter, toppings=None):
        if toppings is None:
            toppings = {}
        else:  # iterujemy po toppings tylko jesli istnieja
            for value in toppings.values():
                if value < 0 or value > 3:  # value < 1 ? jesli value == 0 to chyba dziwnie nie? ale nwm
                    exit(-20)

        if diameter < 20:
            print("bledny promien")
            exit(-10)
        else:  # ten else jest nie potrzebny, jesli exit(-10) sie wykonał to juz program nie dziala dalej
            self.__diameter = diameter

        self.__toppings = toppings  # to sie nie wykonywalo wczesniej
        self.__price = Pizza.area(diameter) * 0.05 + len(toppings) * 2

    @staticmethod
    def area(diameter):
        return math.pi*(diameter/2)**2

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        if value < 20:
            print("bledny promien")
            exit(-10)
        else:
            self.__diameter = value
            self.__price = Pizza.area(value) * 0.05 + len(self.__toppings) * 2

    @property
    def price(self):
        return self.__price

    @property
    def toppings(self) -> Dict[str, int]:
        return self.__toppings

    def add_topping(self, topping: Dict[str,int]):
        self.__toppings.update(topping)
        self.__price = self.__price + 2

    def __str__(self):
        t = ''
        for key, value in self.__toppings.items():
            t = t + ', '.join([f'{key} x {value},'])
        if len(self.__toppings) == 0:
            return f'Pizza:\nśrednica:{self.__diameter}\ncena:{self.__price}'
        else:
            return f'Pizza:\nśrednica:{self.__diameter}\ndodatki:{t}\ncena:{self.__price}'




