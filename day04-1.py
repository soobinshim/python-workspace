'''
if 조건식:
    종속 문장
elif 조건식:
    종속 문장
elif ...
else:
    종속 문장
'''
'''
num = int(input("수 입력: "))
if num > 100:
    print("100보다 크다")
elif num > 50:
    print("50보다 크다")
elif num > 0:
    print("0보다 크다")
else:
    print("그 외의 값 입력")
print("다음 문장 실행")
'''

print("-")

'''
#Q1. 이름, 학번, 3과목의 성적을 입력받아 합계와 평균을 구하고, 평균이 90 이상이면 'A', 80 이상 'B', 70 이상 'C', 60 이상 'D', 60 미만이면 'F' 출력하시오.
name = input("이름 입력: ")
num = input("학번 입력: ")
kor = int(input("국어 점수: "))
mat = int(input("수학 점수: "))
eng = int(input("영어 점수; "))
sum = kor+mat+eng
avr = (kor+mat+eng) / 3

if avr >= 90:
    print("A")
elif avr >= 80:
    print("B")
elif avr >= 70:
    print("C")
elif avr >= 60:
    print("D")
else:
    print("F")
'''

'''
#Q2. 커피의 개당 가격은 2000원이다. 10개 초과하는 양에 대해서만 개당 1500원씩 받는다. 커피의 개수를 입력받아 금액을 출력하시오.
num = int(input("커피 개수 입력: "))

#Q2-1.
if num > 10:
    print(f"{2000*10+1500*(num-10)}원")
else:
    print(f"{2000*num}원")

#Q2-2.
money=0
num = int(input('주문할 커피 개수 : '))
if num>10:
    money += 20000 + (num-10)*1500;
elif num>0 and num<=10:
    money = num*2000;
print(f"{money} 원입니다.\n");
'''

'''
#Q3. 정수를 입력받아 아래와 같이 출력하시오.
num = int(input("정수 입력: "))

if num == 0:
    print("0은 3의 배수도 4의 배수도 아닙니다")
elif num % 3 == 0 and num % 4 == 0:
    print("3의 배수이면서 4의 배수입니다")
elif num % 3 == 0:
    print("3의 배수입니다")
elif num % 4 == 0:
    print("4의 배수입니다")
else:
    print("3의 배수도 4의 배수도 아닙니다")
'''

#Q4. 비행기를 타는 데 30분 거리까지의 기본 요금은 30000원이며, 10분 단위로 추가 요금 5000원씩 부과된다.
# 1~30: 30000 / 31~40: 35000 / 41~50: 40000
money = 30000
time = int(input("비행기 탄 시간(분): "))
time = time - 30
if time > 0:
   # money += (5000+((time-1)//10)*5000)
    if (time%10) == 0:
        money=money+time//10*5000
    else:
        money=money+time//10*5000+5000
print(money,"원입니다.")























