#산술 연산자 : 더하기, 빼기 , 곱하기, 나누기 , 나머지 , 몫
i,j = 10,3

print("%d + %d = %d"%(i,j,i+j))
print("%d - %d = %d"%(i,j,i-j))
print("%d * %d = %d"%(i,j,i*j))
print("%d / %d = %.2f"%(i,j,i/j))

print(i/j) # 나누기 연산자
print(i//j) # 몫 
print(i**j) # 제곱
print(i%j) # 나머지 

# tax_rate=0.10
# income = int(input("당신의 수입을 입력하세요 : "))
# print(f"당신이 내야 할 세금은 {int(income * tax_rate)}원 입니다.")

# mon_pay = float(input("당신의 월 실수령을 입력하세요 : "))
# print(f"당신의 연봉은 {mon_pay * 12} 입니다.")



# 관계연산자 (and, or, not)
# and : 둘다 참이면 참
# or : 둘중 하나만 참
# not : 현재 결과 부정

x,y,z=10,20,30
rst1=(x>0) and (x>y)
rst2=(x>0) or (x>y)
rst3=not((x>0) and (x>y))
print(rst1,rst2,rst3)

#나머지 연산자와 다항연산자
#(조건) and 참인 경우 or 거짓인 경우
num = int(input("정수값을 입력하세요 : "))
flag = (num % 2==0) and "짝수" or "홀수"
print(flag)

age=23
is_adult = (age>=20) and "성인" or "카기네"
print(is_adult)