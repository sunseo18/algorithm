import sys
from collections import deque
from collections import defaultdict

n, m, a, b = map(int, sys.stdin.readline().strip().split())

ab_array = [a, b]
m_array = []
visited = defaultdict(bool)

for _ in range(m):
    m_array.append(list(map(int, sys.stdin.readline().strip().split())))


queue = deque()

def between_m(number):
    for array in m_array:
        lower, higher = array

        if lower <= number <= higher:
            return True
    return False

for i in range(2):
    if not between_m(ab_array[i]):
        queue.append((ab_array[i], 1))
        visited[ab_array[i]] = True

while queue:
    cur, depth = queue.popleft()

    if cur == n:
        sys.stdout.write(str(depth))
        sys.exit()

    for i in range(2):
        next_no = cur + ab_array[i]
        next_deth = depth + 1

        if next_no <= n and not visited[next_no] and not between_m(next_no):
            visited[next_no] = True
            queue.append((next_no, depth + 1))

sys.stdout.write('-1')


