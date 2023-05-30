# 함수란 ?  특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램을 의미
# 함수의 사용 목적은 재사용성 모듈화를 위해 사용
# 업무 분장의 기준으로 삼을 수 있으며 , 단위 테스트의 기준이 됨
# 일반적으로 함수는 직별자 뒤에 () 있음
# ex) print() sum()...
# 매개변수와 함수를 호출하는 인자의 개수는 일치해야 함

#은행 계좌 개설하고 입금과 출금 예제
def open_account(name) : 
    pritnt(f"{name}님의 계좌가 개설 되었습니다.")
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