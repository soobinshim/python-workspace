'''
list
 - 하나의 자료형으로 여러 개의 값을 저장할 수 있다
 - [](대괄호)로 표현되면 리스트로 생각하면 어느 정도 맞다
 - 각각의 값에 접근하고자 할 경우 index를 이용한다
 - index는 0부터 시작한다

ls = [500, 200, 300, 400]
print(ls)
print(ls[0])
print(ls[3])

print("-")

ls = [0,0,0]
ls[0] = int(input("값 입력: "))
ls[1] = int(input("값 입력: "))
ls[2] = int(input("값 입력: "))
sum = ls[0] + ls[1] + ls[2]
print(ls)
print(sum)

print("-")

ls = [0,0,0]
sum = 0
print("len: ", len(ls)) # len = 길이

for i in range (len(ls)):   # i에는 0, 1, 2번째가 들어오게 된다
    ls[i] = int(input(str(i)+"값 입력: ")) # = (f"{i}값 입력:")
    sum += ls[i]
print(ls)
print("합: ", sum)

print("-")

ls = [10,20,30,40]
print("ls: ", ls)
print(ls[1:3])  # 1번째부터 3번째 전까지
print(ls[:2])   # 처음부터 2번째 전까지
print(ls[1:])   # 1번째부터 끝까지
print(ls[:])    # 처음부터 끝까지

print("-")

import copy # import = 다른 파일에 있는 것을 현재 페이지로 불러와서 사용할 때
import day01

n = 100
print(id(n))

ls = [10,20,30]
#arr = ls    # [:]를 붙이면 arr과 ls의 값이 달라진다
#arr = copy.deepcopy(ls)
arr = ls.copy()
print(id(ls))
print(id(arr))

ls[1] = 12345
print(ls)
print(arr)

print("-")

ls = [10,20,30]
arr = [40,50,60]
print(ls)
print(arr)
str = ls + arr  # [10,20,30,40,50,60]
print(str)
str = ls * 3    # [10,20,30,10,20,30,10,20,30]
print(str)

sum = [0,0,0]
mul = [0,0,0]
for i in range( len(ls) ):
    sum[i] = ls[i]+arr[i]
    mul[i] = ls[i]*3
print(sum)
print(mul)

print("-")

a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

print("-")
'''
#Q1. 정렬
ls = [4,8,2,7,6]
for i in range(4):
    for j in range(i+1, 5):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)

for i in range(len(ls)):
    for j in range(len(ls)):
        if ls[i] < ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)


#Q2. 등수 배열
ls = [82,85,76,79,96]
rank = [1,1,1,1,1]

for i in range (len(ls)):
    for j in range(len(ls)):
        if ls[i] < ls[j]:
            rank[i] += 1
            
for i in range(len(rank)):
    print(f"{ls[i]}점, {rank[i]}등")
















