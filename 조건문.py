# 조건문 :  if ~ else

# num = int(input("정수를 입력하세요 : "))
# if num % 2 == 0 :
#     print("짝수")
# else :
#     print("홀수")

#조건문 : if ~elif ~else
# n = int(input("정수입력 : "))
# if n>100 : 
#     print("100보다 큼")
# elif n<100 : 
#     print("100보다 작음")
# else :
#     print("100과 같음!")

age=int(input("나이를 입력하세요 :"))

# if(age > 0 and age <200) :
if(0< age < 200) :
    print("정상입력 입니다.")
else : 
    print("잘못 입력하셧습니다.")


#회원 가입을 위한 id pw를 입력받는
#string.find(찾을문자)
#string.find(찾을 문자, 시작index)
#string.find(찾을 문자, 시작index, 끝index)
user=input("아이디 입력 : ")
if len(user) >= 10 :
    pw =input("비밀번호 입력 :")
    if pw.__len__() < 8 or pw.__len__() > 16 :
        print("비밀번호는 8자에서 16자 사이여야 합니다.")
    else :
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else : 
    print("아이디는 반드시 10자리 이상이어야 합니다.")