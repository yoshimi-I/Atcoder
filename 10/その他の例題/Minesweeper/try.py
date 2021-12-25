H ,W = map(int,input().split())
S = list(list(input()) for _ in range(H))

#ここが配列の外枠を覆う配列を追加するコード
for i in range(H):
    S[i].append(".")
    S[i].insert(0,".")
S.insert(0,list("."*(W+2)))
S.append(list("."*(W+2)))

#ここから配列内をループさせて実行結果を得るコード
for j in range(1,1+H):
    for k in range(1,W+1):
        if S[j][k] == "#":
            continue
        else:
            check = [S[j-1][k-1],S[j][k-1],S[j+1][k-1],S[j-1][k],S[j+1][k],S[j-1][k+1],S[j][k+1],S[j+1][k+1]]
            S[j][k] = check.count("#")

#ここからが配列を出力すコード
for a in range(1,1+H):
    for b in range(1,W+1):
        print(S[a][b],end = "")
    print("")