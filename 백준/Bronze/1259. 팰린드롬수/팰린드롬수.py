import sys

while True:
    text = sys.stdin.readline().strip()

    if text == '0':
        break
    

    length = len(text)

    flag = True
    if length % 2 == 0:
        for i in range(0, (length - 1) // 2 + 1):
            if text[i] != text[-i-1]:
                flag = False
                break
    else:
        for i in range(0, (length - 1) // 2):
            if text[i] != text[-i-1]:
                flag = False
                break

    if flag:
        print("yes")
    else:
        print("no")
