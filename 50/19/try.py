N = int(input())
S = list(input())
Q = int(input())
check = 0
for i in range(Q):
    T,A,B = map(int,input().split())
    A-=1
    B-=1
    if T == 1:
        if check == 0:
            S[A],S[B] = S[B],S[A]
        if check == 1:
            if A<= N-1:
                A = A+N
            else:
                A = A-N
            if B<=N-1:
                B = B+N
            else:
                B = B-N
            S[A],S[B] = S[B],S[A]
    else:
        if check == 0:
            check = 1
        else:
            check = 0
if check == 0:
    print("".join(S))
else:
    left = S[:N]
    right = S[N:]
    ans = right+left
    print("".join(ans))
