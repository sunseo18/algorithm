S = input()
length = len(S)

substring = [S]
for i in range(1, length + 1):
    for j in range(0, length-i+1):
        substring.append(S[j:j+i])

print(len(set(substring)))
