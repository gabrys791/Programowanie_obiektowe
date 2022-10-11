# def func(a, b = 4, c = 5):
#     print(a, b, c)
#
# func(1, 2)

# def func(a, b, c = 5):
#      print(a, b, c)
#
#
# func(1, c = 3, b = 2)

# def func(a, **kwargs):
#     print(a, kwargs)
# func(a = 1, c = 3, b = 2)

# def func(a, b, c = 3, d = 4):
#     print(a, b, c, d)
# func(1, *(5, 6))
#zad1
# def mult(x):
#     iloraz=1
#     for i in range(0,len(x)):
#         iloraz=iloraz*x[i]
#     return iloraz
#
# print(mult(range(3,8,2)))
#zad2
# def mult_ints(x):
#     iloraz=1
#     for i in range(0,len(x)):
#         if type(x[i]) == int :
#             iloraz=iloraz*x[i]
#     return iloraz
# print(mult_ints((3,3.14,5,"abc",7)))
#zad3
# def multiply(*args):
#     iloraz=1
#     for x in range(0,len(args)):
#         iloraz=iloraz*args[x]
#     return iloraz
#
#
# print(multiply(3, 5, 7))
#zad4
# def multiply_ints(*args):
#     iloraz=1
#     for x in range(0,len(args)):
#         if type(args[x])==int:
#           iloraz=iloraz*args[x]
#     return iloraz
#
# print(multiply_ints(3, 3.14, 5, "abc", 7))
#zad5
# def make_car(firma,model,kwargs):
#     slownik={}
#     slownik['firma']=firma
#     slownik['model']=model
#     slownik.update(kwargs)
#     return slownik
#
# print(make_car("Kia","Picanto", {"kolor": "cafemocca", "poj_silnika": 900}))
#zad1
# a=list(range(1,11,1))
# b=[number **2 for number in a]
# c=[number **3 for number in a]
# f=[a,b,c]
# print(f[1][3])
# print(f)
#zad2
# a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[]
# suma1=0
# for i in range(1,2,1):
#     a.append(i)
#     suma1 = suma1 + i
#
#
#
#
# print(suma1)
#
# suma2 = 0
# for i in range(1,3,1):
#     b.append(i)
#     suma2 = suma2 + i
#
# print(suma2)
#
# suma3 = 0
# for i in range(1,4,1):
#     c.append(i)
#     suma3 = suma3 + i
#
# print(suma3)
# suma4 = 0
# for i in range(1,5,1):
#     d.append(i)
#     suma4 = suma4 + i
#
# print(suma4)
# suma5 = 0
# for i in range(1,6,1):
#     e.append(i)
#     suma5 = suma5 + i
#
# print(suma5)
# suma6=0
# for i in range(1,7,1):
#     f.append(i)
#     suma6 = suma6 + i
#
# print(suma6)
# suma7=0
# for i in range(1,8,1):
#     g.append(i)
#     suma7 = suma7 + i
#
# print(suma7)
# suma8=0
# for i in range(1,9,1):
#     h.append(i)
#     suma8 = suma8 + i
#
# print(suma8)
# suma9=0
# for i in range(1,10,1):
#     j.append(i)
#     suma9 = suma9 + i
#
# print(suma9)
# suma10=0
# for i in range(1,11,1):
#     k.append(i)
#     suma10 = suma10 + i
#
# print(suma10)
# tablica=[a,b,c,d,e,f,g,h,j,k]
# print(tablica)
#zad1
def sum(a,b):
    a=[]
    b=[]
    lista=[a,b]
    c=[]
    d=[]
    lista2=[c,d]
    for i in a:
        for i in b:
            c.append(a[i]+b[i])

