import sys

n = int(sys.stdin.readline().strip())


def hoje(a, b):
    if a % b == 0:
        return b
    else:
        return hoje(b, a%b)


for _ in range(n):
    m, n, x, y = map(int, sys.stdin.readline().strip().split())

    max_divide = hoje(m, n)

    n_times = m // max_divide
    m_times = n // max_divide


    min_times = n * n_times
    bigger = max(m, n)

    not_found_flag = True
    if bigger == n:
        for i in range(0, n_times +1):
            if ( n*i + y - x) % m == 0:
                sys.stdout.write(str(n*i + y))
                not_found_flag = False
                break


    else:
        for i in range(0, m_times +1):
            if (m*i + x - y ) %n == 0:
                sys.stdout.write(str(m*i + x))
                not_found_flag = False
                break

    if not_found_flag:
        sys.stdout.write('-1')
    sys.stdout.write('\n')
    


    
