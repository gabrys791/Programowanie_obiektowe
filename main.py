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

list_b = [2, 3, 7]


def uzupelnij_kolejne(alist: list):
    n = 0
    while len(alist) < 10:
        if not (n in alist):
            alist.append(n)
        n += 1


uzupelnij_kolejne(list_b)
print(list_b)


# Zadanie 8


# list_c = []


# for i in range(2, 10000):
#     list_c.append(i)

# print(len(list_c))
# for k in range(2, 100):
#     i = len(list_c) - 1
#     while i > 0:
#         if (list_c[i] != k) and (list_c[i] % k) == 0:
#             del list_c[i]
#         i -= 1

print(list_c)


# Zadanie 9



# def list_swap_first_last(alist: list):
#     alist[0], alist[-1] = alist[-1], alist[0]


# print(list_b)
# list_swap_first_last(list_b)
# print(f'Zad 9a: {list_b}')


# def list_move_right(alist: list):
#     last = alist[-1]
#     n = len(alist) - 2
#     while n >= 0:
#         alist[n+1] = alist[n]
#         n -= 1
#     alist[0] = last


# list_move_right(list_b)
# print(f'Zad 9b: {list_b}')


# def par_zero(alist: list):
#     for n in range(len(alist) - 1):
#         if alist[n] % 2 == 0:
#             alist[n] = 0


# par_zero(list_b)
# print(f'Zad 9c: {list_b}')


# def zastap_suma_sasiadow(alist: list):
#     for n in range(1, len(alist) - 2):
#         alist[n] = alist[n-1] + alist[n+1]
#         # print(f'Zad 9d_{n}: {list_b}')


# zastap_suma_sasiadow(list_b)
# print(f'Zad 9d: {list_b}')


# def usun_srodek(alist: list):
#     if (len(alist) % 2) == 0:
#         del alist[len(alist) // 2]
#         del alist[len(alist) // 2]
#     else:
#         del alist[len(alist) // 2]


# usun_srodek(list_b)
# print(f'Zad 9e_1: {list_b}')
# list_b.append(9)
# usun_srodek(list_b)
# print(f'Zad 9e_2: {list_b}')


# def par_poczatek(alist: list):
#     temp = []
#     for x in alist:
#         if (x % 2) == 0:
#             temp.append(x)
#     for x in alist:
#         if (x % 2) == 1:
#             temp.append(x)
#     for n in range(len(alist) - 1):
#         alist[n] = temp[n]


# par_poczatek(list_b)
# print(f'Zad 9f: {list_b}')


# def second_biggest(alist: list):
#     gmax = alist[0]
#     result = alist[0]
#     for x in alist:
#         if x > gmax:
#             gmax = x
#     for x in alist:
#         if (x > result) and (x < gmax):
#             result = x
#     return result


# print(f'Zad 9g: {second_biggest(list_b)}')


#def is_asc(alist):
#    for n in range(len(alist) - 1):
#        if alist[n+1] < alist[n]:
#            return False
#    return True


#print(f'Zad 9h: {is_asc(list_b)}')


#def has_eq_neighbours(alist):
#    for n in range(len(alist) - 1):
#        if alist[n+1] == alist[n]:
#            return True
#    return False


#print(f'Zad 9i: {has_eq_neighbours(list_b)}')


#def has_eq(alist):
#    temp = []
#    for x in alist:
#        if x not in temp:
#            temp.append(x)
#        else:
#            return True
#   return False


#print(f'Zad 9j_1: {has_eq([3,4,6,4,7,8,6])}')
#print(f'Zad 9j_2: {has_eq([1,2,3,4,5])}')


#def equals(list1, list2):
#    if len(list1) != len(list2):
#       return False
#    for n in range(len(list1)):
#        if list1[n] != list2[n]:
#            return False
#    return True


#print(f'Zad 10_1: {equals([2,3,4], [2,3,4])}')
#print(f'Zad 10_2: {equals([0,0,0,9], [0,0,0])}')











