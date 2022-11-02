'''
Tuple
 - 중복된 데이터를 가질 수 없다
 - 데이터 변경이 불가
 - index로 접근 가능하다
 - 소괄호가 있으면 튜플로 보면 된다
'''

tp = (10,20,30)
print('tp:', tp)
print('tp[0]:', tp[0])
print('type(tp):', type(tp))
print('len(tp):', len(tp))

#tp[0] = 1000   # 변경 불가
tp = (111,222,333,444)
print('tp:', tp)

print("-")

tp = (10)
print(type(tp)) # int

tp = (10,)
print(type(tp)) # tuple

tp = 10,
print(type(tp)) # tuple

'''
packing : 압축 (여러 개의 값을 가지고 있다)
umpacking : 하나의 값을 여러 개로 나누는 것
'''
pack = 1, 2, "패킹"
print("패킹:", pack)
print(type(pack))

a,b,c = pack
print(a,b,c)

a, *b = pack
print(a,b)
print(type(a), type(b))

pack = 10,20,10,10,30
print(pack.count(10))
print(pack.index(20))

print("-")

str_ = "Have a nice day"
print(str_[0])
print(str_[1])

li = [1,2,3,4]
print(li[-1])
print(str_[-1])

for i in range(len(str_)):
    print(str_[i], end="")
print()

for i in str_:
    print(i, end="")
print()

print(str_[7:11])

print("-")

str_ = "Python test, 그리고 programming 할 만하다^^"
print(str_)
print("upper:", str_.upper())   # .upper() 대문자로 변환
print("lower:", str_.lower())   # .lower() 소문자로 변환
print("swapcase:", str_.swapcase()) # .swapcase() 대소문자 변환
print("title:", str_.title())   # .title() 첫 글자 대문자로 변환

print("-")

#Q1. 대소문자 변환
st = "NevEr -eVer 110gIVe up"
st1 = st.title()
print(f"변경 전: {st}")
print(f"변경 후: {st1}")

print("-")

st = "Have a nice day"
print(st.count("a"))        # .count() 해당 단어가 몇 개인지
print(st.count("day"))
print(st.count("dak"))

print(st.startswith("Ha"))  # .startswith() 해당 단어로 시작는지
print(st.startswith("ha"))

print(st.endswith("ay"))    # .endswith() 해당 단어로 끝나는지
print(st.endswith("dday"))

print("-")

#Q2. 공백 포함 문자열의 총 개수, 'a'개수, 's'개수 출력
st = "It is a fun Python class"

st1 = len(st)
st2 = st.count("a")
st3 = st.count("s")

print(f"(총 개수: {st1}, a 개수: {st2}, s 개수: {st3}")

print("-")

st = "Have a nice day"
print(st)

print(st.find("day"))
print(st.index("day"))

print(st.find("kkk"))

print(st.find("a")) # 첫 번째에 있는 위치만 가져옴
print(st.find("a",2))   # 두 번째 다음부터 있는 위치만 가져옴

c = st.find("a",2)
print(c)
c = st.find("a",c+1)    # 5 번째(이전 c에서 5 번째에 있다고 함) 다음부터 있는 위치만 가져옴

print("-")

#Q3. a의 총 개수와 index의 위치를 list에 저장 후 출력
st = "Have a nice day Have a nice day Have a nice day"
cnt = 0
li = list()

while True:
    cnt = st.find("a", cnt)
    if cnt != -1:
        li.append(cnt)
    else:
        break
    cnt += 1
print("a 개수:", st.count("a"))
print("a 위치:", li)


#Q4. 다음 문자열에서 대소문자 구분 없이 ab로 시작하는 문자열과 test로 끝나는 문자열들을 출력하시오
li = ['AbCe test123', '.acd efg', 'a123 TEST 123', '123 TEst']

for i in li:
    lo = i.lower()

    if lo.startswith("ab") or lo.endswith("test"):
        print(i)

print("-")

st = "2015/04/02"
print(st)

st1 = st.replace("/",".")   # .replace 변환
print(st1)
print(st.replace(st[0:4],"2022"))

print("-")

#Q5. 아래의 내용을 다음과 같이 변경하시오
    # -(바): (콜론으로 변경), 년도를 1999년으로 모두 변경

st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일"""
st = st.replace("-",":")
i = 0

for j in range(st.count(":")):
    i = st.find(":",i+1)
    st = st.replace(st[i+1:i+5],"1999")
print(st)
    




















