# 이름
# 나이
# 성별
# 직업

name = input("이름을 입력하세요 : ")

while True :
    age = int(input("나이를 입력하세요 : "))
    if 0 < age < 200 : break
    print("나이를 잘 못 입력 하셨습니다.")

while True :
    gender = input("성별을 입력하세요 : ")
    if gender == "M" or gender =="m" or gender =="f" or gender =="F" : break
    print("성별을 잘못 입력 하셨습니다")

while True :
    job = input("직업을 입력하세요 : ")
    if job == "1" :
        job = "학생"
        break    
    elif job =="2" :
        job = "회사원"
        break  
    elif job =="3" :
        job = "회사원"
        break 
    elif job =="4" :
        job = "회사원"
        break
    print("직업을 잘못 입력하셨습니다.")

print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {job}")
     

