i=0
#while i<5:
for i in range(5):
    print(i, "종속문장실행")
    #i += 1
print('다음 문장들 실행')
# for문으로 변경하세요

i=1
odd,even=0,0
#while i<=10:
for i in range(11):
    if i % 2 == 0:
        even += i
    else:
        odd += i
    #i+=1
print("1~10까지의 짝수 합 : ",even)
print("1~10까지의 홀수 합 : ",odd)
# for문으로 변경

i = 0
while i < 5:
    if i == 3:
        print('3333333')
        break
        
    print('i : ',i)
    i += 1
print('다음 문장들 실행')

print("-"*10)
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
        print('3333333')
        
    print('i : ',i)
    
print('다음 문장들 실행')

rice = 100000; mouse = 2; day=1
while True:
    rice = rice - mouse*20
    if day % 10 == 0:
        mouse *= 2
    #print(f"{day}일 {mouse}마리 {rice}g")
    if rice <= 0:
        break
    day += 1
print( f"{day}일 {mouse}마리")

money, j = 0,0
money = int(input("요금 투입 : "))
while True:
    print("==== 커피 자판기 ====")
    print("1.커피(200) 2.코코아(250) 3.반환 4.종료")
    j = int( input("메뉴 선택 : "))
    if j == 4:
        print("종료")
        break
    elif (j==1 and money >= 200) or (j==2 and money >= 250):
        print("맛있게 드세요")
        if j == 1:
            money -= 200
        else:
            money -= 250
    elif j == 3:
        print(money, "원 반환 금액")
        money = 0
    else:
        print("요금이 부족합니다")
















