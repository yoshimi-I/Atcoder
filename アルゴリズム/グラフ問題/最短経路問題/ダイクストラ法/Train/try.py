import heapq
from math import ceil

N,M,X,Y = map(int,input().split())

route = [[] for _ in range(N+1)]
for i in range(M):
    A,B,T,K = map(int,input().split())
    route[A].append([B,T,K])
    route[B].append([A,T,K])
que = []
point = [10**20]*(N+1)
check_count = [0]*(N+1)
heapq.heapify(que)
# スタート位置の経過時間(ポイントと呼ぶ)、スタートの場所を代入
heapq.heappush(que,[0,X]) # [ポイント、場所]の二次元配列
while len(que) > 0:
    # 1.まずはdequeから最小値を取り出して場所を確定させる。
    confirm_count,confirm_place = heapq.heappop(que)
    if check_count[confirm_place] == 0: # 既に確定している場所の探索は行わない
        check_count[confirm_place] = 1 # 確定したので値を１にする
        if point[confirm_place] > confirm_count:
            point[confirm_place] = confirm_count #heapqueから受け取った最小値がポイント配列の中の値より小さかったら更新
        # 2.値が確定したら確定した値から行ける場所を次のdequeに入れる(探索を開始する)
        for next_place,T,K in route[confirm_place]:
            next_point = ceil(confirm_count/K)*K+T
            heapq.heappush(que,[next_point,next_place])
if point[Y] == 10**20:
    print(-1)
else:
    print (point[Y])
