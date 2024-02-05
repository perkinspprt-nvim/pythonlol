from random import randint

FILENAME = 'text01.txt' 
NUMRANGE = 9
LISTLEN = 6
LINES = 2

def gen_randomlist(num):
    randlist = []
    counter = 0
    while counter < num:
        number_rolled = randint(1, NUMRANGE)
        randlist.append(number_rolled)
        counter += 1
    return randlist

for num in range(1, LINES):
    rlist = gen_randomlist(LISTLEN)
    for randnum in rlist:
        with open(FILENAME,'a') as file_object:
            file_object.write(str(randnum))
    print("Line added...")
print(f"Finished writing to {FILENAME}")
