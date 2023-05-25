#규칙 1: http://naver.com에서 앞의 http://잘라내기
#규칙 2: 처음 만나는 점(.) 이후는 제외
#규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 "o" 갯수 + 
#        글자에 호팜 된 'k'갯수 + '!' + 자신의 이니셜
file_name="password.txt"
f = open(file_name,"wt")
while True : 
    url = input("사이트 : ")
    if url =="exit" : break
    my_str = url.replace("http://","")
    my_str = my_str[:my_str.index(".")]   
    password = my_str[0:3]+str(len(my_str)) + str(my_str.count("n")) +"!"+"lts"
    f.write(password + "\n")
f.close()



