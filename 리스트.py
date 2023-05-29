# 연속적으로 데이터를 저장하는 자료형, 
#동적으로 크기가 변경 됨. 다른 타입의 데이터를 함께 사용 가능(다른 배열, 다른 크기)

numbers = [1,2,3,4,5]
fruits = ["apple", "banana","orange"]
mixed = [1, "apple", True, 3.14, [1,2,3,4,5]]

# 변수 사용 대비 이점
# 1. 기존
kor, eng, mat = map(int, input("성적 입력 : ").split()) 
tot = kor + eng + mat 
print(f"평균  : {tot/3}")

# 2. 리스트에다가 넣기 
score = list(map(int, input("성적 입력 : ").split()))
print(f"평균 : {sum(score)/len(score)}")

