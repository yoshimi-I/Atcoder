N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
check_box = list(list([0]*3) for _ in range(N))
for i in range(N):
    if i == 0:
        check_box[0] = L[0]
    else:
        for j in range(3):
            check_box[i][0] = L[i][0] + max(check_box[i-1][1],check_box[i-1][2])
            check_box[i][1] = L[i][1] + max(check_box[i-1][0],check_box[i-1][2])
            check_box[i][2] = L[i][2] + max(check_box[i-1][0],check_box[i-1][1])
print(max(check_box[N-1]))