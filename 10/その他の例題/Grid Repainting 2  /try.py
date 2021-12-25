H,W = map(int,input().split())
S = list(list(input()) for _ in range(H))
ans = "Yes"

for i in range(H):
    S[i].append(".")
    S[i].insert(0,".")
S.append(list("."*(W+2)))
S.insert(0,list("."*(W+2)))
for j in range(1,H+1):
    for k in range(1,W+1):
        if S[j][k] == "#":
            search = [S[j-1][k],S[j+1][k],S[j][k-1],S[j][k+1]]
            if search.count("#") == 0:
                ans = "No"
print(ans)