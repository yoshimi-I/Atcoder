# 深さ優先探索 
## 問題文
- [深さ優先探索 ](https://atcoder.jp/contests/atc001/tasks/dfs_a)
## 回答例
```
import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
h,w = map(int,input().split())
c = [list(input()) for i in range(h)]

def dfs(x,y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#": # 壁に当たったり、探索範囲外になった場合はreturn
        return # 関数内で使うbreak文みたいなもん
    if c[x][y] == "g": # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()
        
    c[x][y] = "#" #探索済みを示すためのマーキング
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j # スタート位置
            
dfs(sx, sy)
print("No")
```
## 解説
- 解説のまえにDFSでは再起関数というものを用いいるためその理解が必要となる[再起関数とは](saiki.md)
- 以上を踏まえた上で解説を行う。
- イメージとしては深さ優先のため放射状に広がっていくイメージ
    - 例えば
    ```
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    ```
    があることからも分かるとおりdfs(x+1,y)が実行されれば,次は(x+2,y)が次に実行されていき,(x+1,y)の周りが全滅した場合に初めてdfs(x-1,y)こちらの処理に入ることができる。
- なので深く深く進んでいって1つでも可能性があればそれを追っていき,全滅した場合(今回であれば壁に当たった時のみ)関数の処理自体をreturnを使って終了していると言うことである
## 参考記事
- [amateur engineer's blog](https://amateur-engineer-blog.com/dfs-bfs/#:~:text=%E6%B7%B1%E3%81%95%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2(DFS,%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92%E7%B9%B0%E3%82%8A%E8%BF%94%E3%81%97%E3%81%BE%E3%81%99%E3%80%82))