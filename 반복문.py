# for 요소 in 시퀀스(리스트, 튜플, 문자열) : 요소를 순회
# fruits = ["apple","banana","kiwi"]
# for e in fruits :
#     print(e)

# for 변수 in range(시작값, 종료값, 증감값) : 자바의 기본적인 for 과 동일
# n = int(input("정수 입력 : "))
# sum = 0
# for i in range(1, n+1) :
#     sum += i

# print(sum)

#2중 for문 : 구구단 출력
# for i in range(2,10) : #
#     for j in range(1,10) :
#         print(f"{i} * {j} = {i*j}")
#     print("-"*25)

#2중 for문과 조건문 활용하기
# n = int(input("정수 입력 : "))
# for i in  range(0,n) : #입력받은 개수 만큼 순회
#     for j in range(0,n) :
#         if j % 2 == 0 : print(f"{j}는 짝수")
#         else : print(f"{j}는 홀수")

#별찍기 : 입력 받은 수 만큼 별 찍기
n = int(input())
for i in range(n) :
    for j in range(i+1) :
        print("*", end="")
    print("\t")


for i in range(n):
    for j in range(n-i) :
        print("*",end="")
    print()

#for문에서 continue 사용하기 : continue를 만나면 아래의 문장을 수행하지 않고
# 반복문의 조건문으로 이동

n = int(input())
for i in range(n) : 
    if i % 2 == 0 : continue
    print(i)

#for 문을 역순으로 순회하기
n = int(input())
for i in range(n, 0-1 ,-1) :
    print(f"값 : {i}")