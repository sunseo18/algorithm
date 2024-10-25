import sys
from collections import defaultdict

input = sys.stdin.readline


S, P = map(int, input().split())

word = list(input().strip())

A, C, G, T = map(int, input().split())


def check_dictionary(dictionary):

    global A
    global C
    global G
    global T

            
    if dictionary['A'] < A:
        return False
    if dictionary['C'] < C:
        return False
    if dictionary['G'] < G:
        return False
    if dictionary['T'] < T:
        return False

    return True

dictionary  = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
i, j = 0, 0

while j < P:
    dictionary[word[j]] += 1

    if j == P-1:
        break
    j+=1

answer = 0
while j < len(word):
    if check_dictionary(dictionary):
        answer += 1


    dictionary[word[i]] -= 1
    i += 1
    j += 1
    if j == len(word):
        break
    dictionary[word[j]] += 1

print(answer)

    
    
    
