print("-------------------------------------------------")

with open('digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


filename = 'digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

print("-------------------------------------------------")

with open(filename) as file_object:
     lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
