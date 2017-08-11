import sys

for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 == 0:
            sys.stdout.write('*')
        else:
            sys.stdout.write(' ')

    sys.stdout.write('\n')
