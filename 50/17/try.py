N = int(input())
ans_list = set()
for i in range(2,10**5):
    for j in range(2,40):
        if i**j <= N:
            ans_list.add(i**j)
        else:
            break
print(N-len(ans_list))
