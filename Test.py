
# # 람다식
# mysum = lambda x,y: 2*x + y
# print(mysum(2,4))

# #문자열 거꾸로 
# kh = "kh 정보교육원"
# reversed_kh=kh[::-1]
# print(reversed_kh)

# #for문과 range()함수를 사ㅣ용 1 - 1까지 만들고 한줄로 출력
# for i in range (1,11) :
#     print(i,end="")

# #수치해석과 관련된 모듈을 사용하기 위한 임포트 명령어를 작성하시오.
# # import numpy as np


# question = list(range(100))
# print(question[2])

# #출력 거꾸로
# nums = [1, 5, 7, 2, 4, 3, 6]
# nums.sort(reverse=True)
# print(nums)

# #변경한 lambda 식에 x에 10 y에 20을 입력하여 실행하는 코드를 서술하시오. 
# def test(x, y):
#     return x * y

# test = lambda x,y : x*y
# print(test(10,20))

# #입력받은 수의 팩토리얼을 계산하여 리턴하는 함수를 작성하시오.


def facto(n):
    res=1
    for i in range(1,int(n)+1) :
        res *= i 
    return res
print(facto(input("입력하세요 : ")))
    
