N = int(input())
l = list(map(int, input().split()))
num = 0
ans = 0
while True:
    for i in range(N):
        if l[i]%2 != 0:
            ans = 1
    if ans == 1:
        break 
    for i in range(N):
        l[i] = l[i]//2
    num += 1
print(num)

