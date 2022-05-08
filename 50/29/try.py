N  = int(input())
mod=10**9+7
E = 10**N
# AはA i=0 なる i が存在する。の余事象
# BはB i=9 なる i が存在する。の余事象
# A_BはA且つB
# Eは全事象
A = 9**N
B = 9**N
A_B = 8**N
ans = E-(A+B)+A_B
print(ans%mod)