# 입력 받은 수가 소수인지 아닌지 판별하기(함수이용)

def prime(num) :
    for i in range(2,num) :
        if num % i == 0 : return False
    return True

n = int(input("정수 : "))
if (prime(n)) : print(f"{n}은 소수 입니다.")
else : print(f"{n}은 소수가 아닙니다.")