import sys


input_file = open('in.txt', 'r')

for line in input_file:
    line = line.rstrip()
    nucl = {}

    for c in line:
        if c in nucl:
            nucl[c] += 1
        else:
            nucl[c] = 1

    character_list = ['A', 'C', 'G', 'T']
    for i in range(0, len(character_list)):
        key = character_list[i]
        if i > 0:
            print(' ', end='')
        print(nucl[key], end='')
    print()