class Car:
    def __init__(self,wyd,poj,pal):
        self.wyd=wyd
        self.poj=poj
        self.pal=0
    def pokaz_auto(self):
        return f'Wydajnosc {self.wyd},pojemnosc {self.pol}'
    def tankuj(self,dodaj):
        return self.pal+dodaj.pal
my_car=Car(20,40,0)

