#입력 받은 n개의 원소에 대한 평균 구하기
n = input("갯수를 입력하세요 : ")
list=[0]*int(n)
print(list)
for_n = 0

for i in range(0,int(n)):
    list[i] = int(input(f"숫자를 입력하세요"))
    for_n+=list[i]

print(for_n)


# 정수  n을 입력 받아  n*n 출력하기
n = input("숫자를 입력하세요 : ")
print(int(n)*int(n))


#n개에 대한 숫자를 입력 받아 최소값 및 최대값 구하기
n = input("숫자를 입력하세요")
list = [0] *int(n)
for i in range(0,int(n)):
    list[i] = int(input(f"숫자를 입력하세요"))

print(min(list))
print(max(list))


#주민등록번호를 입력받아 생년 월일, 성별, 나이 출력하기
id_num=input("주민번호를 입력하세요 : ")
year = id_num[:2]
mon_dat = id_num[2:6]

if int(id_num[6]) == 1 :
    gender = "남성"
else :
    gender = "여성"

age = 2023-1900-int(id_num[:2])
print(year)
print(mon_dat)
print(gender)
print(age)
