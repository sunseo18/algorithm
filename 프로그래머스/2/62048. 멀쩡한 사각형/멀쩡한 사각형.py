import math
    

def biggest_mod(a, b):
    if a % b == 0:
        return b
    
    return biggest_mod(b, a%b)

def solution(w,h):
    
    w, h = min(w,h), max(w,h)
    gcd = biggest_mod(h, w)
    return w*h - (w + h - gcd)
    
