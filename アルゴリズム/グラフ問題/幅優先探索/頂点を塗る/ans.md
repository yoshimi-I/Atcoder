# 頂点を塗る
## 問題
- [頂点を塗る(アルゴ式より出題)](https://algo-method.com/tasks/414)
## 解答
```
from collections import deque
que = deque()
N,M = map(int,input().split())
path = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    path[A].append(B)
    path[B].append(A)
check = [0] * (N)
ans = []
que.append(0)
check[0] = 1
print(0)
while len(que) > 0:
    for k in range(len(que)):
        now = que.popleft()
        for i in path[now]:
            if check[i] == 0:
                ans.append(i)
                que.append(i)
                check[i] = 1
    ans.sort()
    print(*ans)
    ans = []
```
## 解説
- while文の前までは前回の問題と方針は同じ
- 今回のポイントはn回目の処理でキューに追加される値全ての色を塗らないと次の処理に進めないようにしなくては行けないということである。
    - 例えば、1の次に2,3,4の色を塗ることができる時,キューには2,3,4が追加される。またその次は2から塗れるところ、3から塗れるところ、４から塗れる
    ところを同時に出力しなくては行けない。
    - そのためには追加されたキューの長さを受け取りその回数処理を行なって、n回目に追加されるキューをn+1回目に残さないようにしなくては行けない。
```
for k in range(len(que)):
```
この文章である