import matplotlib.pyplot as plt
from random import randint

# CONSTANTS
LENGTH_OF_RANDLIST = 10
RAND_RANGE = 30
X_AXIS_LEN = 20

def gen_randomlist(num):
    randlist = []
    counter = 0
    while counter < num:
        number_rolled = randint(1, RAND_RANGE)
        randlist.append(number_rolled)
        counter += 1
    return randlist

def lenlist(list):
    endlist = [0, ]
    counter = 0
    while counter < len(list)-1:
        counter += 1
        endlist.append(counter)
    return endlist

randlist = gen_randomlist(LENGTH_OF_RANDLIST)
lenlist = lenlist(randlist)

plt.plot(lenlist, randlist)
plt.show()
