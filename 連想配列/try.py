N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
S = list(input())

min = dict()
max = dict()

for i in range(N):
    x = L[i][0]
    y = L[i][1] 

    #方向がR即ち右に進む
    # 最小値の更新を行う
    if S[i] == "R":
        if y in min:
            if min[y] > x:
                min[y] = x
        else:
            min[y] = x

    #方向がL即ち左に進む
    # 最大値の更新を行う
    if S[i] == "L":
        if y in max:
            if max[y] < x:
                max[y] = x
        else:
            max[y] = x
    #yをキーとする値がそれぞれmaxとminに含まれていたとき、minよりmaxの方が大きい場合処理を終了する
    if y in max and y in min:
        if max[y] > min[y]:
            print("Yes")
            exit()

print("No")
