# for 요소 in 시퀀스(리스트, 튜플, 문자열) : 요소를 순회
fruits = ["apple","banana","kiwi"]
for e in fruits :
    print(e)

# for 변수 in range(시작값, 종료값, 증감값) : 자바의 기본적인 for 과 동일
n = int(input("정수 입력 : "))
sum = 0
for i in range(1, n+1) :
    sum += i

print(sum)

#2중 for문 : 구구단 출력
for i in range(2,10) : #
    for j in range(1,10) :
        print(f"{i} * {j} = {i*j}")
    print("-"*25)
