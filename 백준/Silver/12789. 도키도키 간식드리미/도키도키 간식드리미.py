N = int(input())


students = map(int, input().split())
number = 1
stack =[]

for s in students:
    while stack and stack[-1] == number:
        stack.pop()
        number += 1

    if s == number:
        number += 1
    else:
        stack.append(s)
                            

while stack:
    p = stack.pop()
    if p == number:
        number += 1
    else:
        print('Sad')
        break

if number == N +1:
    print('Nice')
