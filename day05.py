'''
for(초기값, 비교값, 증감값):
    종속문장
반복문
- 동일한 반복할 경우 사용
- 규칙적으로 값이 변하는 경우
- 여러개의 값을 하나씩 표현하고자 하는 경우
'''
for i in range(1, 11, 1):#i=1, i<11, i+=1
    print( i )
    
print('다음 문장들 실행')

for i in range(1 ,  11 ,  1):
    print("for 시작")
    if i % 2 == 0 :
        print('i = ', i)
    print("for 끝")

    
print('다음 문장들 실행')

print("="*10)
for i in range(0, 11, 2):
    print( i )
    
print("="*10)
for i in range(10, 0, -2):
    print( i )

print("-"*10)

print( 1 , end="\t")
print( 2 )
print( 3 )
print("-"*10)

sum_ = 0
num = 1

sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num
num += 1
sum_ = sum_ + num

print('sum_ = ', sum_)

sum_ = 0
for num in range(1,11,1):
    sum_ = sum_ + num
print('반복 sum : ',sum_)

for n in range(1, 31, 1):
    print(n , end="\t")
    if n%5 == 0:
        print()


sum_ = 0
num = int( input('수 입력 : '))
for i in range(1, num+1 , 1):
    sum_ += i
print(f"1~{num}까지의 합 : {sum_}")


oddSum = 0; evenSum = 0
for i in range(1, num+1 , 1):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print(f"1~{num}까지의")
print("짝수 합 : ",evenSum)
print("홀수 합 : ",oddSum)









