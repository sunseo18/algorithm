count = 0
n, k = map(int, input().split())
answer = -1
def merge(A, p, q, r):
    global count
    global k
    global answer
    i = p
    j = q+1
    t = 0
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
            t += 1
        else:
            tmp.append(A[j])
            j += 1
            t += 1

    while i <= q:
        tmp.append(A[i])
        i += 1
        t += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
        t += 1
    i = p
    t = 0
    while i <= r:
        count+= 1
        if count == k:
            answer = tmp[t]
        A[i] = tmp[t]
        i += 1
        t += 1

def merge_sort(array, p, r):
    if p < r:
        q = (p +r)// 2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)

array = list(map(int, input().split()))

merge_sort(array, 0, len(array) - 1)

print(answer)
