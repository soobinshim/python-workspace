num1 = 9
num2 = 2

print( f"{num1} / {num2} = {num1 / num2}" )
print( f"{num1} // {num2} = {num1 // num2}" )
print( f"{num1} % {num2} = {num1 % num2}" )
print( f"{num1} ** {num2} = {num1 ** num2}" )

'''
* 관계 연산자
 - >, <, <=, ....
 - 참(True) 또는 거짓(False)을 표
'''
su1 = 3.1
su2 = 3

print( "su1 >= su2 :", su1 >= su2 )
print( "su1 < su2 :", su1 < su2 )
print( "su1 == su2 :", su1 == su2 )
print( "su1 != su2 :", su1 != su2 )

print( "-" )

'''
* 복합 대입 연산자
 - +=, -=, *=, ...
 ex.
 a = 10
 a = a + 100 -> a += 100
 a = a * 100 -> a *= 100
'''
su1 = su2 = 5

su1 += 1; print( "su1 += 1 ->", su1 )
su1 -= 1; print( "su1 -= 1 ->", su1 )
su1 *= su2; print( "su1 *= su2 ->", su1 )
su1 //= su2; print( "su1 // su2 ->", su1 )
su1 %= su2; print( "su1 %= su2 ->", su1 )

print( "-" )

su1 = 5
su2 = 3

su1 **= su2 #su1 = 125
su1 -= 2 #su1 = 123

print( "su1 / 4 :", su1 / 4 )   # 30.7...
print( "su1 // 4 :", su1 // 4 ) # 30
print( "su1 % 4 :", su1 % 4 )   # 3

print( "-" )

'''
* 논리 연산자
 - 참 또는 거짓 표현
 - and , or, not
 - or ; 값 or 값 -> 하나라도 참이면 결과는 참
 - and : 값 and 값 -> 하나라도 거짓이면 거짓, 모두가 참일 때 참
 - not : not 값 -> 결과값을 반전시켜 준다
'''
print( False or False )
print( (10 > 20) or (10 % 2 == 0) )

print( False and True )
print( True and True )
print( False and False )

a = 100
print( a > 10 and a % 2 == 0 )

print( not True )
print( not False )

print( "-" )

'''
* 제어문
 - if, 반복문, break, continue
 ex.
 if 조건식:
     종속 문장
'''
print( "1. 쉬운 게임" )
print( "2. 어려운 게임" )
print( "3. 게임 종료" )
#num = int(input(">>> "))
num = 1
if num == 1:
    print( "쉬운 게임이 실행됩니다" )
if num == 2:
    print( "어려운 게임이 실행됩니다" )
if num == 3:
    print( "게임을 종료합니다" )
print( "다음 문장" )

print( "-" )

num1 = 10
num2 = 5

if num1 > num2:
    print( "참인 경우 실행" )
print( "다음 문장 실행" )

print( "-" )

num = int(input("수 입력: "))

if num % 3 == 0:
    print( f"{num}은(는) 3의 배수" )

print( "-" )

num = int(input("수 입력: "))

if num % 2 == 0:
    print(f"{num}은(는) 짝수")
if num % 2 == 1:
    print(f"{num}은(는) 홀수")

print( "-" )

num1 = int(input("수 입력: "))
num2 = int(input("수 입력: "))

if num1 > num2:
    print(f"{num1}이(가) 더 큰 수")
if num1 < num2:
    print(f"{num2}이(가) 더 큰 수")

print( "-" )

num = int(input("수 입력: "))
print(f"{num}의 절대값은 {-num}")













