s1 = input()
s2 = input()
s1_num = len(s1)
s2_num = len(s2)

DP = list(([100] * (s1_num + 1)) for _ in range(s2_num + 1) )
for a in range(s1_num + 1):
    DP[0][a] = a
for b in range(s2_num + 1) :
    DP[b][0] = b
for i in range(1,s2_num + 1):
    for j in range(1,s1_num + 1):
        if s1[j-1] == s2[i-1]:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1]) + 1
print(DP[s2_num][s1_num])
