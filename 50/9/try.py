N = int(input())
#value = 元の数字
# base = n進法
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)
count = []
for i in range(1,N+1):
    N_list =list(str(i))
    N_8 = base10int(i,8)
    N_8_list = list(str(N_8))
    if "7" in N_list or "7" in N_8_list:
        count.append(i)
print(N-len(count))
