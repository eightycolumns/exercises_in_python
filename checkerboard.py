import sys

def main():
    for i in range(0, 8):
        for j in range(0, 8):
            if is_even(i + j):
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')

        sys.stdout.write('\n')

def is_even(d):
    return d % 2 == 0

if __name__ == '__main__': main()
