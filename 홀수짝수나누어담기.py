#응용 문제 : 홀수, 짝수 나누어 담기
# 무작위 수를 공백으로 입력받아 홀수와 짝수 리스트에 나누어 담기
number = list(map(int,input("입력 : ").split()))
even=[] # 짝수 저장
odd=[] # 홀수 저장

for e in number : #number 리스트 요소로 자동 순회
    if e%2 ==0 :
        even.append(e)
    else :
        odd.append(e)

even.sort()
odd.sort()
print(even)
print(odd)

# 람다를 이용하는 방법으로 풀기
number = list(map(int,input("입력 : ").split()))
odd = list(filter(lambda x: x % 2 == 1, number)) # (x) => x % 2 == 1 [리액트 문법]
even = list(filter(lambda x: x % 2 == 0, number))
print(even)
print(odd)
