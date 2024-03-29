import sys

inputs = sys.stdin.readlines()

def kanto(array, a, b):
    if a == b:
        return

    no = b-a+1
    devidedNo = no // 3
    start = a + devidedNo
    end = b - devidedNo

    i = start
    while i <= end:
        array[i] = " "
        i += 1
    

    kanto(array, a, start-1)
    kanto(array, end+1, b)

for input in inputs:
    n = int(input.strip())
    

    array = ['-'] * 3**n
    kanto(array, 0, 3**n -1)
    sys.stdout.write("".join(array))
    sys.stdout.write('\n')
