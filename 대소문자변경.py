#영어 소문자와 대문자로 이루어진 단어를 입력 받은 뒤 대문자는 소문자로 소문자는 대문자로 

# result = ""
# for e in input():
#     if e.islower() :
#         result += e.upper()
#     else :
#         result += e.lower()
# print(result)

#세개의 자연수를 입력 받아서 모두 곱함
#곱한 값의 결과에서 나오는 숫자의 횟수를 출력하기

A,B,C = map(int, input("정수 3개 입력 : ").split())
ls = list(str(A*B*C))
for i in range(10):
    print(ls.count(str(i)))

