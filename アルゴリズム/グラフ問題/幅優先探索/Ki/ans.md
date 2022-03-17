# Ki
## 問題
- [Ki](https://atcoder.jp/contests/abc138/tasks/abc138_d)
## 解答
```
from collections import deque
que = deque()
N,Q = map(int,input().split())
path = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)
counter = [0]*(N+1)
for j in range(Q):
    p,x = map(int,input().split())
    counter[p] += x

visited = [0]*(N+1)

que.append(1)
visited[1] = 1
while len(que) > 0:
    now = que.popleft()
    point = counter[now]
    for to in path[now]:
        if visited[to] == 0:
            counter[to] += point
            visited[to] = 1
            que.append(to)
print(*counter[1:])
```
## 解説
- [幅優先探索とは](bfs.md)を読んでほしい
1. 方針通り、まずは配列の番号と行き先が対応する配列を用意する
    ```
    入力
    4 3
    1 2
    2 3
    2 4

    出力
    [[],[2],[1,3,4],[2],[2]]
    >>> これは配列の[n]のなかに格納されている場所に行くことができるというものである。例えば配列の[２]からは1,3,4に行くことができるという風に

    ```
    - この時ポイントなのは[0]を用意し、そこは空にするという事である
    - また一方だけではなく逆側も記載する
2. 次にキューを用意する
    - こちらは前回使ったdequeを用いる
        - そうすることで末端の値をO(N)で取り出すことができる。
3. 次に行った場所をチェックする配列を用意する
    - 例えば一度行った場所は配列を0から１に変えることで戻らなくする
4. 最後にwhile文を用いてキューの中が空になるまで処理を繰り返す
- では具体的な説明に入っていきたいと思う
```
from collections import deque
que = deque()
N,Q = map(int,input().split())
path = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)
counter = [0]*(N+1)
for j in range(Q):
    p,x = map(int,input().split())
    counter[p] += x
```
- 上記のコードで配列の番号と行き先が対応する配列pathを用意する
- また各頂点のカウンターを保持する配列counterも作成する
```
visited = [0]*(N+1)
```
- 行った場所はチェックをする配列visitedを作成する
    - 一度行った場所は0から１に変えることにより一度行った場所のチェックを行う。
```
que.append(1)
visited[1] = 1
```
- あらかじめキューにスタート地点を代入し、visitedにも１を代入する
    - whileからの処理がqueに値が1つ以上あるときに処理が走るので、whileに入る前にキューに追加しておく必要がある。
```
while len(que) > 0:
    now = que.popleft()
    point = counter[now]
    for to in path[now]:
        if visited[to] == 0:
            counter[to] += point
            visited[to] = 1
            que.append(to)
```
- まずはキューから値を取り出す、その後counterに記載されている点数を保持する
- その後行き先をfor文で回して行ったことのない場所であれば移動する
    - 行き先でポイントを加算して、visitを1にして移動したことをチェックする
    - さらに移動先もキューに入れる
        - ポイントは加算してもいい、なぜなら幅優先探索は一度深いところに行ったら浅いところには戻ってこないためである
## 最後に
- とてもわかりにくと思うので、デバッグをして確認しながら理解するのがいい