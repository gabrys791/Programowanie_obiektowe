def nwd(a,b):
    while b:
        a, b = b, a %b
        return a

class wymierna:
    licznik:int
    mianownik:int
    def __init__(self,licznik=0,mianownik=1):
        self.licznik=licznik
        if mianownik==0:
            print("tak nie wolno")
        else:
            self.mianownik=mianownik
    def get_licznik(self):
        return self.licznik
    def get_mianownik(self):
        return self.mianownik
    def __repr__(self):
        return f'{self.licznik}/{self.mianownik}'
    def __float__(self):
        return self.licznik/self.mianownik

    def __add__(self, other):
        if self.mianownik!=other.mianownik:
            lewy=self.licznik*other.mianownik
            prawy=other.licznik*self.mianownik
            return wymierna(lewy+prawy,self.mianownik*other.mianownik)
        else:
            return wymierna(self.licznik + other.licznik,self.mianownik)
    def __sub__(self,other):
        if self.mianownik!=other.mianownik:
            lewy=self.licznik*other.mianownik
            prawy=other.licznik*self.mianownik
            return wymierna(lewy-prawy,self.mianownik*other.mianownik)
        else:
            return wymierna(self.licznik - other.licznik,self.mianownik)









def main():
    liczba1=wymierna(licznik=4,mianownik=6)
    print(liczba1.get_licznik())
    print(liczba1.get_mianownik())
    print(liczba1.__repr__())
    liczba2=wymierna(licznik=2,mianownik=3)
    print(liczba1.__add__(liczba2))
    print(liczba2.__sub__(liczba1))




if __name__=="__main__":
    main()
