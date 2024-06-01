import sys

r, c, n = map( int, sys.stdin.readline().strip().split())

bomb_array = []

for i in range(r):
    bomb_array.append(list(sys.stdin.readline().strip()))

dir_i = [1, -1, 0, 0]
dir_j = [0, 0, -1, 1]

def reset_bomb():
    return [['O' for _ in range(c)] for _ in range(r)]

if n % 2 == 0:
    for i in range(r):
        for j in range(c):
            sys.stdout.write('O')
        sys.stdout.write('\n')
    sys.exit()


for nn in range(n//2):
    where_is_bomb = []
    for i in range(r):
        for j in range(c):
            if bomb_array[i][j] == 'O':
                where_is_bomb.append((i, j))

    bomb_array = reset_bomb()
    
    for bomb in where_is_bomb:
        cur_i, cur_j = bomb[0], bomb[1]

        bomb_array[cur_i][cur_j] = '.'
        for x in range(4):
            next_i, next_j = cur_i+dir_i[x], cur_j + dir_j[x]

            if 0<=next_i<r and 0<=next_j<c:
                bomb_array[next_i][next_j] = '.'

for i in range(r):
    for j in range(c):
        sys.stdout.write(bomb_array[i][j])
    sys.stdout.write('\n')
            

