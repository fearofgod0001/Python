# 함수란 ?  특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램을 의미
# 함수의 사용 목적은 재사용성 모듈화를 위해 사용
# 업무 분장의 기준으로 삼을 수 있으며 , 단위 테스트의 기준이 됨
# 일반적으로 함수는 직별자 뒤에 () 있음
# ex) print() sum()...
# 매개변수와 함수를 호출하는 인자의 개수는 일치해야 함

#은행 계좌 개설하고 입금과 출금 예제
def open_account(name) : 
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name
# 입금
def desposit(balance,input) : # 잔액과 입금 금액을 입력 받음
    print(f"{input}이 입금되었습니다. 잔액은 {balance + input}입니다.")
    return balance+input

# 출금
def withdraw(balance,input) :
    if balance >= input :
        print(f"{input}이 출금 되었습니다. 잔액은 {balance-input}입니다.")
        return balance-input   
    else :
        print(f"잔액이 부족해 출금이 실패 했습니다. 현재 잔액은 {balance}입니다.")
        return balance
    
balance = 0 #외부에서 선언하지만 매개변수로 전달 함
name = open_account("이태석")
balance=desposit(balance, 1000)
balance-withdraw(balance, 500)
print(f"{name}의 잔액은 {balance} 입니다.")


# 기본값 인자 : 함수 선언 시 매개변수에 대한 기본 값을 정의 할 수 있습니다.
def profile(name, year =2, age=18, school="휘문고") :
    print(f"이름 : {name}, 학교 : {school}, 학번 : {year}, 나이 : {age}")

profile("이석태")
profile("이태석")
profile("이태석",None,22)

# 가변 매개 변수 : 함수의 매개변수 앞에 (*) 붙여주면 함수의 매개변수를 몇 개를 입력 하던 함수 내에서 튜플로 인식
def profile(name,age,*lang) :
    print(f"이름 : {name}, 나이 : {age}",end=" ")
    for e in lang :
        print(e,end=" ")
    print("\n")

profile("이태석", 18,"Python","java","C","C++","React","Kotiln")
profile("이태석2", 22,"Python","java")
profile("이태석3", 18,"Python","java","C","C++")

# 지역 변수와 전역 변수 
# 전역변수 : 함수보다 변수의 생존 범위가 더 넓어서 리턴 값이 필요 없음
# global 키워드를 사용하면 전여긍로 선언한 변수를 함수 내에서 사용 할 수 있음.
knife = 10 # 칼을 10자루 준비함 
def game(player) : 
    global knife
    knife -= player #게임에서 참가한 선수가 사용한 개수만큼 차감

def game(player,knife) : 
    knife -= player #게임에서 참가한 선수가 사용한 개수만큼 차감
    print(f"남아있는 칼은 {knife} 자루 입니다.")

player = int(input("경기에 참여하는 선수가 몇명 입니까? : "))
game(player,knife)

# 람다와 함수
# 람다란? 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현, 이름 없는 함수를 의미