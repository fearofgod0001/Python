# 배수 찾기 
# 문제 : 정수 n(0 < n < 1000)과 수 목록 주어졌을 때, 목록에 들어가는 수가 n의 배수인지 아닌지 구하는 프로그램
# --------------------------
# 예제 입력
# 3 << n
# 1 7 99 321 777 0
# --------------------------
n = int(input("n을 입력하세요 : "))
list = []
while True:
    x = int(input())
    if x == 0 : break
    list.append(x)
for e in list :
    if e % n == 0 :
        print(f"{e} is a multiple of {n}")
    else :
        print(f"{e} is NOT a multiple of {n}")

