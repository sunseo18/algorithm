n = int(input())

dictionary = dict()

for _ in range(n):
    name, eorl = input().split()
    if eorl == "enter":
        dictionary[name] = 1
    else:
        del dictionary[name]

    
    
for name in sorted(dictionary.keys(), reverse = True):
    print(name)
