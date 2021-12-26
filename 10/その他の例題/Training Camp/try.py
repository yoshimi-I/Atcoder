N = int(input())
first = 1
ans = 1
num = 10**9+7
for i in range(1,N+1):
    ans = first * i
    first = ans%num
print(ans%num)