# while 문 : 조건이 참인 동안 반복 수행하며 주로 횟수가 정해지지 않은 경우에 사용,
# 횟수가 정해지지 않은 경우 반드시 탈출 조건이 필요
n = int(input("정수 입력 : "))
sum = 0
while n :
    sum += n
    n -= 1 # n--

print(sum)

while True :
    age = int(input("나이를 입력 하세요 : "))
    if 0 < age < 200 : break; # 정상적인 입력으로 간주
    print("나이를 다시 입력 하세요.")
