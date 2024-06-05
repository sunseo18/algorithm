import sys
import heapq


n, m = map(int, sys.stdin.readline().strip().split())


present_list = list(map(int, sys.stdin.readline().strip().split()))
m_list = list(map(int, sys.stdin.readline().strip().split()))

present_heap = []

for present in present_list:
    heapq.heappush(present_heap, -present)

for m in m_list:
    if present_heap:
        biggest = heapq.heappop(present_heap)

        tmp = biggest + m
        # 구매 못 함
        if tmp > 0:
            print(0)
            sys.exit()
        else:
            if tmp == 0:
                continue
            else:
                heapq.heappush(present_heap, tmp)
    else:
        print(0)
        sys.exit()

print(1)
