# 연속적으로 데이터를 저장하는 자료형, 
#동적으로 크기가 변경 됨. 다른 타입의 데이터를 함께 사용 가능(다른 배열, 다른 크기)

# numbers = [1,2,3,4,5]
# fruits = ["apple", "banana","orange"]
# mixed = [1, "apple", True, 3.14, [1,2,3,4,5]]

# # 변수 사용 대비 이점
# # 1. 기존
# kor, eng, mat = map(int, input("성적 입력 : ").split()) 
# tot = kor + eng + mat 
# print(f"평균  : {tot/3}")

# # 2. 리스트에다가 넣기 
# score = list(map(int, input("성적 입력 : ").split()))
# print(f"평균 : {sum(score)/len(score)}")

# print(mixed[1:3])

s = ["korea","seoul","inchun",[1,2,3,4,5],["한국","일본","중국"]]
print(s[0][1])
print(s[4][0][0], s[4][1][0], s[4][2][0])

# 리스트 연산자 : 연결(+), 반복(*)
list_a=[1,2,3]
list_b=[4,5,6]
print(list_a*3)
print(list_a+list_b)

# 리스트 요소 추가 : 
# append : 리스트의 끝에 값을 추가하는 함수 
# insert : 특정 위치에 값을 추가하는 함수
list_aa = [1,2,3]
list_aa.append(4)
list_aa.append(10)
list_aa.insert(1,22) # 1번 인덱스에 22를 삽입.
print(list_aa)

# 리스트 제거하기
# pop : 인덱스가 없으면 마지막 요소 반환하고 삭제, 
# 인덱스가 있으면 인덱스의 위치 데이터 삭제
# 인덱스 범위를 벗어나면 error
# remove : 값으로 제거, 동일한 값이 여러개 있는 경우 낮은 인덱스부터 제거 
# clear : 모든 값을 지우고 빈 리스트만 남김
# del 리스트명[인덱스] : 해당 값 제거
list_all=[0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","korea"]
print(list_all)
list_all.pop() # 인덱스가 없으므로 마지막 요소 제거
print(list_all)
list_all.pop(8)
print(list_all)
list_all.insert(8,8)
print(list_all)
del list_all[10]
print(list_all)
list_all.insert(10,"a")
print(list_all)
list_all.clear()
print(list_all)



