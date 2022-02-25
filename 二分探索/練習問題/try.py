N,K = map(int,input().split())
A = list(map(int,input().split()))
left_num = 0
right_num = N-1
ans = -1
if K >= A[0] and K <= A[right_num]:
    while (right_num - left_num > 1):
        mid_num = (left_num + right_num)//2
        if A[mid_num] == K:
            print(mid_num)
            exit()
        elif A[mid_num] > K:
            right_num = mid_num
        else:
            left_num = mid_num
    ans = right_num
print(ans)