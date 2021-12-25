A,B,C,D = map(int,input().split())
ans = 0
if C >= A:
    if D >= B:
        ans = B-C
    else:
        ans = D-C
else:
    if D >= B:
        ans = B-A
    else:
        ans = D-A
if ans < 0:
    ans = 0
print(ans)
