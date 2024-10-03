import sys

input = sys.stdin.readline


T = int(input())


def calculate(calculated_weight, key):
    global dictionary
    global weight

    if calculated_weight[key] != -1:
        return calculated_weight[key]
    # 후보가 여러 개라면
    if len(dictionary[key]) > 1:
        _max = -1
        for candidate in dictionary[key]:
            if calculated_weight[candidate] == -1:
                calculated_weight[candidate] = calculate(calculated_weight, candidate)
            if calculated_weight[candidate] > _max:
                _max = calculated_weight[candidate]
                
        calculated_weight[key] = _max + weight[key]
    else:
        if calculated_weight[dictionary[key][0]] == -1:
            calculated_weight[dictionary[key][0]] = calculate(calculated_weight, dictionary[key][0])
            
        calculated_weight[key] = weight[key] + calculated_weight[dictionary[key][0]]




    return calculated_weight[key]



    



for _ in range(T):
    N, K = map(int, input().split())

    nodes = {n for n in range(1, N+1)}

    weight = [0] + list(map(int, input().split()))
    calculated_weight = [-1] * (N+1)
    
    dictionary = dict()
    for i in range(K):
        s, e = map(int, input().split())

        nodes.discard(e)
        if e in dictionary:
            dictionary[e].append(s)
        else:
            dictionary[e] = [s]

    for n in nodes:
        calculated_weight[n] = weight[n]
        
    Q = int(input())
        
    calculate(calculated_weight, Q)

    print(calculated_weight[Q])
