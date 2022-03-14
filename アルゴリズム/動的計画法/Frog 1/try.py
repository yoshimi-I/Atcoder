N = int(input())
h = list(map(int,input().split()))
table = [0]*N
a = 0
b = 0
for i in range(1,N):
    if i == 1:
        table[1] = abs(h[1]-h[0])
    else:
        a = table[i-1] + abs(h[i] -h[i-1])
        b = table[i-2] + abs(h[i] -h[i-2])
        table[i] = min(a,b)
print(table[N-1])