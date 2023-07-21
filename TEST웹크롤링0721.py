from bs4 import BeautifulSoup
import json

import requests
res = requests.get("https://www.iei.or.kr/intro/teacher.kh")

soup = BeautifulSoup(res.text, "lxml")



#강사 선생님 성함 이미지 URL 출력
# intro_names = soup.find_all("p", {"class": "intro_name"})
# for intro_name in intro_names:
#     print(intro_name.text.strip())

# intro_thumbs = soup.find_all("div", {"class": "intro_thum"})
# for intro_thumb in intro_thumbs:
#     img_tag = intro_thumb.find("img")
#     if img_tag:
#         img_src = img_tag.get("src")
#         print(img_src)


intro_data = []

intro_names = soup.find_all("p", {"class": "intro_name"})
intro_thumbs = soup.find_all("div", {"class": "intro_thum"})

#JSON 양식으로 코드 변환
for intro_name, intro_thumb in zip(intro_names, intro_thumbs):
    name = intro_name.text.strip()
    img_tag = intro_thumb.find("img")
    if img_tag:
        img_src = img_tag.get("src")
        intro_data.append({"name": name, "img_src": img_src})

# JSON 형식으로 저장
with open("teacher.json", "w", encoding="utf-8") as json_file:
    json.dump(intro_data, json_file, ensure_ascii=False, indent=4)

print("크롤링한 정보를 JSON 파일로 저장하였습니다.")