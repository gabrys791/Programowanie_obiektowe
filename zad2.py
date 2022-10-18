class Adres:
    def __init__(self,nr_domu,ulica,miasto,kod_pocztowy,nr_mieszkania=None):
        self.nr_domu=nr_domu
        self.ulica=ulica
        self.miasto=miasto
        self.kod_pocztowy=kod_pocztowy
        if nr_mieszkania is not None:
            self.nr_mieszkania=nr_mieszkania
    def showdomek(self):
        return f'{self.ulica}/{self.nr_domu}\n{self.kod_pocztowy} {self.miasto}'
    def comes_before(self,other):
        for i in range(len(self.kod_pocztowy)):
            if self.kod_pocztowy[i]==other.kod_pocztowy[i]:
                continue
            if self.kod_pocztowy[i]<other.kod_pocztowy[i]:
                return True
            return False


my_house=Adres(6,'Pieniężnego 23','Ostróda','14-101')
print(Adres.showdomek(my_house))
your_house=Adres(7,'kos','Olsztyn','14-102',80)
print(Adres.comes_before(my_house,your_house))

