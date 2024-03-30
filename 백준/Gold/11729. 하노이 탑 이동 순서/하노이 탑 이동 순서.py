dir_list = []
no = 0
def hanoi(n, from_pos, to_pos, aux_pos):
    global no
    no += 1
    if n == 1:
        dir_list.append([from_pos, to_pos])
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    dir_list.append([from_pos, to_pos])
    hanoi(n-1, aux_pos, to_pos, from_pos)

n = int(input())

hanoi(n, 1, 3, 2)

print(no)

for dir in dir_list:
    print(dir[0], dir[1])
