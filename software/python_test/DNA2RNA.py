input_file = open('in.txt', 'r')

for line in input_file:

    line = line.rstrip()

    for c in line:
        if c is 'T':
            c = 'U'
        print(c,end='')
