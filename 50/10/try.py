N = int(input())
def divisor(num):
    i = 1
    ans_list = []
    while i**2 <= num:
        if num %i == 0:
            ans_list.append(i)
            if num//i != i:
                ans_list.append(num//i)
        i += 1
    ans_list.sort()
    return(ans_list)
ans = divisor(N)
for i in ans:
    print(i)

