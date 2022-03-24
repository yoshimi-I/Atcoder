H,W,X,Y = map(int,input().split())
X = X-1
Y = Y-1
ans_up = 0
ans_down = 0
ans_right = 0
ans_left = 0
root = list(list(input()) for _ in range(H))
for i in range(1,W):
    if Y+i< W:
        if root[X][Y+i] == "#":
            break
        else:
            ans_down += 1
for j in range(1,W):
    if Y-j >= 0:   
        if root[X][Y-j]== "#":
            break
        else:
            ans_up += 1
for k in range(1,H):
    if X+k <H:
        if root[X+k][Y] == "#":
            break
        else:
            ans_right += 1
for l in range(1,H):
    if X-l >=0:
        if root[X-l][Y] == "#":
            break
        else:
            ans_left += 1
print(ans_left+ans_right+ans_down+ans_up+1)


