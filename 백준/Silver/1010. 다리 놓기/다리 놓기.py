from itertools import combinations

T = int(input())

fact_list = [1, 1]
for i in range(2, 31):
    fact_list.append(fact_list[i-1] * i)

for i in range(T):
    n, m = map(int, input().split())

    print(fact_list[m] // (fact_list[n] * fact_list[m-n]))
