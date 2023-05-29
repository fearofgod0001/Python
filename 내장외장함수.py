#내장 함수 :  파이썬 기본적으로 제공하며, import 없이 사용
ls = [1,2,3,4,5,6,7,8,9]
print(sum(ls) / len(ls)) #평균을 구하기 
print(sorted(ls)) #정렬
# 몫과 나머지 반환
print(divmod(sum(ls),5)) # 몫과 나머지

# 외장함수 (import 해서 사용): 랜덤
import random

#지정한 범위 내의 임의의 수를 구하는 함수 
rand = random.randrange(0,4) # 0~4 미만의 임의의 값이 생성
print(rand)
rand = random.randint(0,4) # 0~4 사이의 임의의 값이 생성
print(rand)

#현재 시간 가져오기
from datetime import datetime #리액트에서 import datetime from datetime 과 똑같은 양식

datetime.today()
datetime.today().year
datetime.today().month
datetime.today().day
datetime.today().hour

# 중복 값이 없는 로또 번호 생성
import random
print("로또 번호 자동 생성 : ",end="")
ls=[]
while True :
    rand = random.randrange(1,46)
    if rand not in ls : 
        ls.append(rand)
    if len(ls) == 6 : break
print(ls)

