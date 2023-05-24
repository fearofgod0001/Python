print(39) #정수형
print("문자열")
print([1,2,3,4,5]) #리스트형
print(1+2)
print("파"+"이"+"썬")
print("파""이""썬")
print("파","이","썬") #콤마는 기본적으로 띄어쓰기가 포함되어 있음
print("파\n\n\n이\n\n썬")
print("\"안녕하세요\"라고 말했습니다.")

# end와 sep옵션
print("Hello", end="\n")
print("파이썬...")

print(1,2,3,4,5, sep="\t")
print("파이썬...")
print("010","5006","4146", sep="-")

year = 2023
month = 5
day = 24
print(year, month, day)

# 다양한 출력 스타일
name = "이태석"
age = 32
gender = "남성"
job = "소프트웨어 개발자"
addr = "경기도 수원시"
#c언어 스타일, %로 서식으 ㄹ지정하는 형식
print("="*5, "C 스타일", "="*5)
print("이름 : %s"%(name))
print("나이 : %d"%(age))
print("성별 : %s"%(gender))
print("직업 : %s"%(job))
print("주소 : %s"%(addr))

#파이썬 스타일 3.6 이전 버전에서 주로 사용
print("="*5, "파이썬 old 스타일", "="*5)
print("이름 : {}".format(name))
print("이름 : {}, 주소: {}".format(name,addr))
print("나이 : {}".format(age))

#파이썬 스타일 3.6이후 버전에서 주로 사용
print("="*5, "파이썬 new 스타일", "="*5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"주소 : {addr}")

#자바스타일
print("="*5, "자바 스타일", "="*5)
print("이름 : "+ name)
print("나이 : "+ str(age))
print("성별 : " + gender)

#출력 포맷 정렬
# < : 좌측 정렬
# > : 우측 정렬
# ^ : 중앙정렬
print("|{:5}|".format(10))
print("|{:<5}|".format(10))
print("|{:>5}|".format(10))
print("|{:^6}|".format(10))

num=10
print(f"|{num:5}|")

# 소수점 이하 
print(f"{3.141592:.2f}")


