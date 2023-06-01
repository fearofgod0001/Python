import requests # HTTP 요청을 보내고 응답을 받는데 사용하는 라이브러리(get, post, put, delete)
from bs4 import BeautifulSoup #HTML 및 XML 파일에서 데이터를 추출할 떄 사용
from flask import Flask

# url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
# html = requests.get(url).text
# soup = BeautifulSoup(html,"html.parser")
# print(soup)

app = Flask(__name__) #__name__은 현재 모듈 이름을 의미
@app.route()

#오류
url ="https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

#HTTP Get요청
response = requests.get(url).text
#HTML 파싱
soup = BeautifulSoup(response,"html.parser")
# print(soup)

for loc in soup.select("location") :
    print("도시 : ",loc.select_one("city").string)
    print("날씨 : ",loc.select_one("wf").string)
    print("최저기온 : ",loc.select_one("tmn").string)
    print("최고기온 : ",loc.select_one("tmx").string)
    print("-"*25)