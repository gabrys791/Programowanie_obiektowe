#zad1
# lista=[]

# for x in range(0,11):
#     lista.append(x)
#
#
# print(lista)
# for x in range(0,11):
#     lista.append(x*2)
# for x in range(0,11):
#     lista.append(x**2)
# for x in range(0,11):
#     lista.append(0)
# for x in range(0,11):
#     if(x%2==0):
#         lista.append(0)
#     else:
#         lista.append(1)
# for x in range(0,11):
#     lista.append(x%5)
# print(lista)
#zad2
# lista=[]
# x=0
# while(x!=11):
#     lista.append(x)
#     x=x+1
# while(x!=11):
#     lista.append(x*2)
#     x=x+1
# while(x!=11):
#     lista.append(x**2)
#     x=x+1
# while(x!=11):
#     lista.append(0)
#     x=x+1
# while(x!=11):
#     if(x%2==0):
#         lista.append(0)
#     else:
#         lista.append(1)
#     x=x+1
# while(x!=11):
#     lista.append(x%5)
#     x=x+1
# print(lista)
#zad3
# def ile_ujemnych(lista):
#     y=0
#     for x in lista:
#         if x<0:
#             y=y+1
#     return y
# lista=[4,2,1,-2]
# print(ile_ujemnych(lista))
#zad4
# def iloczyn(lista):
#     y=1
#     for x in lista:
#         y=x*y
#     return y
# lista=[4,5,2,3]
# print(iloczyn(lista))
#zad5
from typing import Tuple
# def minmax(lista):
#     max=0
#     min=999
#     for x in lista:
#         if x>max:
#             max=x
#         if x<min:
#             min=x
#     return (min,max)
# lista=[6,34,5,1,9]
# print(minmax(lista))
#zad6
# def suma(lista):
#     y=0
#     for x in range(len(lista)):
#         if x%2==0:
#             y = y + lista[x]
#         else:
#             y = y - lista[x]
#     return y
# lista=[1,3,5,2,3]
# print(suma(lista))
#zad7
# x=0
# lista=[]
# while x!=10:
#     a=input("podaj liczbe")
#     a=int(a)
#     czysamo=0
#     for b in lista:
#         if a==b:
#             czysamo=1
#             break
#         else:
#             czysamo=0
#     if czysamo!=1:
#         lista.append(a)
#         x=x+1
#zad8




print(lista)













