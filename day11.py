'''
set
 - 중복을 허용하지 않는다
 - 순서가 없다
 - list처럼 index로 접근이 불가
 - {} 대괄호로 표현됨
'''
'''
s = set("안녕녕녕하세요")
print(s)
print(type(s))

s = set([1,2,3,3,3,'안','안','녕'])
print(s)
#print(s[0]) # index로 접근 불가

li = list(s) # list로 형변환을 하면 index 접근 가능
print(li)
print(li[1])
print(type(li))

s = {1,2,3,4}
print(s)

s.add(555)  # .add 값 추가
print(s)

s.update([7,8,9])   # .update 값 뭉탱이로 추가
print(s)

s.remove(555)   # .remove 값 삭제
print(s)

import random

for i in range(5):
    print(random.random(), end=", ")    # random.random() = 0.0000... ~ 0.9999... 사이에 있는 값

print()

for i in range(5):
    print(int(random.random()*3), end=", ")

print()

for i in range(5):
    print(random.randrange(0,3), end=", ")  # random.randrange() = 범위 내의 숫자(해당 코드는 0부터 2) 랜덤으로 표현

print("-")





#Q1. 1부터 45까지 랜덤한 숫자 6 개. 중복 X
import random

# list
ls = []

while len(ls) < 6:
    ran = random.randrange(1,46)
    if ls.count(ran) == 0:
        ls.append(ran)
print(ls)


ls = []

for i in range(6):
    if ls.count(i) < 6:
        i = random.randrange(1,7)

        if ls.count(i) == 0:
            ls.append(i)
    else:
        pass
print(ls)

# set
s = set()

while len(s) < 6 :
    s.add(random.randrange(1,46))
print(s)

s = set()

for i in range(6):
    if len(s) < 6:
        i = random.randrange(1,7)
        s.add(i)
    
print(s)



print("-")



#Q2. 업다운 게임
import random

best = 100

while True:
    print("1.게임시작 2.최고기록 확인 3.종료")

    num = int(input(">>> "))
    cnt = 0
    
    if num == 1:
        com = random.randrange(1,100)
        print("com:", com)

        while True:
            user = int(input("수 입력: "))
            cnt += 1

            if com < user:
                print("down")
            elif com > user:
                print("up")
            elif com == user:
                print("정답")
                if cnt < best:
                    print("최고기록 갱신")
                    best = cnt
                break
                 
    elif num == 2:
        if best == 100:
            print("게임 먼저 진행하세요")
        else:
            print("최고 기록: ", best)
        
    elif num == 3:
        print("게임 종료")
        break
'''


print("-")


#Q3. 야구 게임
import random
best = 100

while True:
    print("\n1.게임시작 2.최고기록 확인 3.종료")

    num = int(input(">>> "))
    cnt = 0

    if num == 1:
        cnt = 0
        com_set = set()

        while True:
            com_set.add(random.randrange(1,10))
            
            if len(com_set) == 3:
                break
            
        com = list(com_set)
        print("com:", com)
        result = [0,0,0]
        
        while True:
            cnt += 1
            for i in range(3):
                user = int(input("수 입력: "))

                if user == com[i]:
                    result[0] += 1
                elif com.count(user) != 0:
                    result[1] += 1
                else:
                    result[2] += 1
            print(f"{result[0]}스트라이크, {result[1]}볼, {result[2]}아웃")

            if result[0] == 3:
                break
            result = [0,0,0]
            
        if cnt < best:
            print(cnt, "회. 최고 기록 갱신")
            best = cnt
        else:
            print(cnt, "회 만에 맞혔습니다")

    elif num == 2:
        if best == 100:
            print("게임 먼저 진행하세요")
        else:
            print("최고 기록: ", best)

    elif num == 3:
        print("게임 종료")
        break
        
            
    


























