import pymysql

# 전역변수 선업
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드
conn = pymysql.connect(host="127.0.0.1", user="root", password="TIGER", db="mysqlDB", charset="utf8")
# 커서 생성하기
cur = conn.cursor()
# 조회 하기
cur.execute("SELECT * FROM userTable")
#출력 
print("사용자ID    사용자이름    이메일     출생연도")
print("------------------------------------------------")

while True :
    row = cur.fetchone()
    if row == None : break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(f"{data1:6}{data2:10}{data3:18}{data4:6}")