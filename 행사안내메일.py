# 고객의 이름 입력 받기
# 행사 내용 입력 받기
# 행사 날짜 입력 받기
# 행사 시간 입력 받기
name = input("고객이름 : ")
event_name = input("행사제목 : ")
event_date = input("날짜(ex:20230514) : ")
event_time = input("시간 : ")

month = event_date[4:6]

greeting = "한파의 연속인 1월 입니다."
if month == "01":
    greeting = "한파의 연속인 1월 입니다."
elif month == "02":
    greeting = "봄을 기다리는 2월 입니다."
elif month == "03":
    greeting = "봄의 기운이 느껴지는 3월 입니다."
elif month == "04":
    greeting = "새싹이 피어나는 4월 입니다."
elif month == "05":
    greeting = "계절의 여왕 5월 입니다."
elif month == "06":
    greeting = "활동하기 좋은 6월 입니다."
elif month == "07":
    greeting = "휴가가 기다려지는 7월 입니다."
elif month == "08":
    greeting = "무더운 8월 입니다."
elif month == "09":
    greeting = "무더운 8월 입니다."
elif month == "10":
    greeting = "천고마비의 계절 10월 입니다."
elif month == "11":
    greeting = "쓸쓸한 늦가을 11월 입니다."
else :
    greeting = "올 한해의 마무리 12월 입니다."

trans_time = int(event_time)
if trans_time > 12 :
    trans_time = trans_time - 12
    time ="오후" + str(trans_time)
else :
    time ="오전" + str(trans_time)

e_name = greeting.replace("입니다.","이다 ㅋ")
print(f"오 {name} 야!!!")
print(e_name)
print(f"반가운 {event_name}이 돌아왔다")
print(f"날짜는 {event_date[4:8]}이고 시간은 {time}에 한다 참석해라")

