# Python Object(Ductionary , List, Tuple 등)를 JSON 문자열로 변ㄱ경하는 것을 JSON Encoding
# 인코딩은 json.dumps() 메소드를 이용해서 JSON 문자열로 변환
# 디코딩은 JSON 문자열을 Python 타입(Dictonary, List, Tuple)로 변경 하는 것 json.loads()
# import json
# customer = {
#     "id" : 123456,
#     "name" : "이태석",
#     "history" : [{"date" : "2023-05-05", "제품" : "iPone Pro 14"},
#                  {"date" : "2023-06-02", "제품" : "Galuxy S23 Ultra"}
#                  ]

# }

# jsonString = json.dumps(customer, ensure_ascii=False)
# print(jsonString)

import json

jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
    {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
    {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
]}'''

dict = json.loads(jsonString)

print(dict["name"])
for h in dict["history"]:
    print(h["date"], h["item"])