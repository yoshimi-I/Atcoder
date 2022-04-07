N = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(N):
    min_num = A[i]
    for j in range(i,N):
        min_num = min(min_num,A[j])
        ans = max(ans,min_num*(j-i+1))
print(ans)