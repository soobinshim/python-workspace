
st = '  파이썬 '
print(f"*{st}*")    # 공백 구분

st = st.strip() # .strip() 양쪽에 있는 공백 제거
print(f"*{st}*")

if st == '파이썬':
    print("참")
else:
    print("거짓")

st = "----파이썬----"
print(st)
print(st.strip("-"))
print(st.rstrip("-"))   # .rstrip() 오른쪽 제거
print(st.lstrip("-"))   # .lstrip() 왼쪽 제거

print("-")

st = "Never ever give up"
print(st)
li = st.split() # .split() 괄호 안의 특정 값을 기준으로 분리시켜 줌
print(li)

st = "Never:ever:give:up"
li = st.split(":")
print(li)

print("-")

#Q1. 아래의 내용을 다음과 같이 변경 후 st에 저장하여 st를 출력하시오
st = "안녕하세요 오늘 2020/2/23 날씨는 error 춥다"

#[안녕하세요,오늘,2020/2/23,날씨는,error,춥다]
sp_li = st.split()
#year=[2020, 2, 23]
year = sp_li[2].split("/")
#sp_li = [안녕하세요,오늘,날씨는,춥다]
del(sp_li[4])
del(sp_li[2])
#[안녕하세요,오늘,2020년2월23일,날씨는,춥다]
sp_li.insert(2,
        year[0]+"년"+year[1]+"월"+year[2]+"일")
print( sp_li )

st = ""
for i in sp_li:
    st += i+" "
print( st )

print("-")

st = """
안녕 하세요
반갑 습니다
추워요
"""
print(st.split("\n"))
print(st.splitlines())  # .splitlines() 엔터를 기준으로 분리시켜 줌

print("-")

#Q2. url 확장자에서 .gif .jpg .png 파일만 뽑으세요
st = """ url~~~ """

for i in st.split("src"):
    for k in i.split():
        if k.endswith('.gif"') or k.endswith('.jpg"') or k.endswith('.png"'):
            print(k.strip('"').split("/")[-1])

print("-")

st = '123'
re = "%"
print(re.join(st))  # .join() 앞쪽의 값을 뒤쪽 값의 사이사이에 끼워넣음
print("안녕".join(st))

li = ["123","안녕","하세요"]
print("♡".join(li))

print("-")

st = "python"
print(st)
print(st.center(10))    # .center() 가운데 정렬
print(st.center(10,'-'))
print(st.ljust(10))     # .ljust() 왼쪽 정렬
print(st.rjust(10))     # .rjust() 오른쪽 정렬
print(st.zfill(10))     # .zfill() 비어 있는 공간은 0으로 채우고 정렬

print("-")

#Q3. 아래의 값을 변경하여 출력하시오
accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"

replaceAB = accountBook.split(',') #,기준으로 리스트로 저장

k = 0
for i in replaceAB:
    replaceAB[k] = i.lstrip() #각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
    k += 1

print('item'.ljust(10),end='')
print('date'.ljust(10),end='')
print('$(price)'.ljust(10))
print('-'*30)

kk = '$ '
for i in range(len(replaceAB)):
    z = replaceAB[i].split() #공백을 기준으로 리스트로 저장

    for k in range(len(z)):
        if k == 0 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k ==1 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k == 2 : 
            print("{:,}".format(int(z[k])).join(kk).ljust(10))
























