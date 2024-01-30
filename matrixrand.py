# Simple python dice using random 

from random import randint

def gen_randomlist(num):
    randlist = []
    counter = 0
    while counter < num:
        number_rolled = randint(1, 6)
        randlist.append(number_rolled)
        counter += 1
    return randlist

def Make_matrix(num):
    baselist = []
    counter = 0
    while counter < num:
        randlist = gen_randomlist(6)
        baselist.append(randlist)
        counter += 1
    return baselist

Matrix01 = Make_matrix(6)
for row in Matrix01:
    print(row)