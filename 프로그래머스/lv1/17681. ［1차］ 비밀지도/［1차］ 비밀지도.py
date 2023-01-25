def solution(n, arr1, arr2):
    binaryArr1 = []
    binaryArr2 = []
    for decimal in arr1:
        binaryArr1.append(bin(decimal)[2:].zfill(n))

    for decimal in arr2:
        binaryArr2.append(bin(decimal)[2:].zfill(n))

    return collapseMaze(n, binaryArr1, binaryArr2)

def collapseMaze(n, binaryArr1, binaryArr2):
    collapsedBinaryTotal = []
    for i in range(n):
        collapsedBinary = ''
        binary1 = binaryArr1[i] 
        binary2 = binaryArr2[i] 

        for i in range(n):
            result = int(binary1[i]) or int(binary2[i])
            if(result):
                collapsedBinary += '#'
            else:
                collapsedBinary += ' '

        collapsedBinaryTotal.append(collapsedBinary)

    return collapsedBinaryTotal