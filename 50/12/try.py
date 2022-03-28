import math
def lcm(x,y):
    return (x*y)//math.gcd(x,y)  

A,B=map(int, input().split())
print(lcm(A,B))