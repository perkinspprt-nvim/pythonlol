with open('pi_digits.txt') as file_object:
    contents = file_object.readlines()

pi_string = "" 
for line in contents:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))