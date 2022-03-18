# 迷路
## 問題
- []()
## 解答
```
from collections import deque
que = deque()
H,W = map(int,input().split())
X_0,Y_0,X_1,Y_1 = map(int,input().split())
S = list(list(input()) for _ in range(H))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = list([0]*W for _ in range(H))
check = list([0]*W for _ in range(H))
que.append([X_0,Y_0])
check[X_0][Y_0] = 1
count = 0
while len(que) > 0:
    count += 1
    for j in range(len(que)):
        x,y = que.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= 0 and next_x < H and next_y >= 0 and next_y < W:
                if check[next_x][next_y] == 0 and S[next_x][next_y] == "W":
                    que.append([next_x,next_y])
                    check[next_x][next_y] = 1
                    ans[next_x][next_y] = count
print(ans[X_1][Y_1])
```
## 解説
- 基本的に今まで通りのやり方でOK
- dx,dyの配列を作成しfor文を回すことで左右上下の移動を表している。
- また
```
if next_x >= 0 and next_x < H and next_y >= 0 and next_y < W:
```
で迷路の外に出た時の条件を取り除いている。
- 今回もfor文の中にqoqを入れることでque全ての処理が終わった後に次の処理を行うようにしている。
```
for j in range(len(que)):
        x,y = que.popleft()
```