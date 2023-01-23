from pizza import Pizza


class Slice(Pizza):
    __how_many_slices: int

    def __init__(self, diameter, toppings, how_many_slices):
        super().__init__(diameter, toppings)
        if how_many_slices < 4 or how_many_slices > 12:
            print("bledna ilosc kwalkow")
            exit(-10)
        else:
            self.__how_many_slices = how_many_slices

    @property
    def how_many_slices(self):
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, value):
        if value < 4 or value > 12:
            print("bledna ilosc kwalkow")
            exit(-10)
        else:
            self.__how_many_slices = value

    def part_price(self, ordered_slices):
        return self.price * (ordered_slices/self.__how_many_slices)

    def __str__(self):
        if self.toppings is None:
            return f'Pizza:\nśrednica:{self.diameter}\ncena:{self.price}\nkawalki{self.__how_many_slices}\ncena za kawalek{self.price/self.__how_many_slices}'
        else:
            return f'Pizza:\nśrednica:{self.diameter}\ndodatki{self.toppings}\ncena:{self.price}\nkawalki:{self.__how_many_slices}\ncena za kawalek:{self.price/self.__how_many_slices}'