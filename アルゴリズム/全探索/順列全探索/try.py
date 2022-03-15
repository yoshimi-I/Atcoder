import itertools
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
ls = list(itertools.permutations(range(1,N+1)))
print(abs(ls.index(P)-ls.index(Q)))