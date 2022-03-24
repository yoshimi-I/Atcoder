N = int(input())
S = []
T = []
for i in range(N):
    s,t = input().split()
    S.append(s)
    T.append([int(t),i])
T.sort(reverse=True)
print(S[T[1][1]])