N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
answer = []
score = 0
def match(pon,count_num,answer):
    if pon == "r":
        if answer[count_num-K] == "p":
            answer.append("a")
            return 0
        else:
            answer.append("p")
            return P
    if pon == "s":
        if answer[count_num-K] == "r":
            answer.append("a")
            return 0
        else:
            answer.append("r")
            return R
    if pon == "p":
        if answer[count_num-K] == "s":
            answer.append("a")
            return 0
        else:
            answer.append("s")
            return S

for j in range(K):
    if T[j] == "r":
        answer.append("p")
        score += P
    if T[j] == "s":
        answer.append("r")
        score += R
    if T[j] == "p":
        answer.append("s")
        score += S


for i in range(K,len(T)):
    score += match(T[i],i,answer)

print(score)