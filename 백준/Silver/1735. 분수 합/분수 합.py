A, B = map(int, input().split())
X, Y = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

moth = B*Y
child = A*Y+X*B

gcd_val = gcd(child, moth)

print(child//gcd_val, moth//gcd_val)
