N = int(input())
max = 30_000_000

def endWordOrNull(number):
    number_str = str(number)
    if '666' in number_str:
        return number
    

count = 0
for i in range(max):
    endword = endWordOrNull(i)
    if endword:
        count += 1
        if count == N:
            print(endword)
            break
