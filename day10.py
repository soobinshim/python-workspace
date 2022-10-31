
aa = [[1,2,3,4],[5,6,7,8]]

#a = aa[0]
#a = aa[0][:]
#a = aa[0].copy()
import copy
a = copy.deepcopy(aa[0])
a[1] = 2000

print("aa: ", aa)
print("a: ", a)

print("-")

#Q1. 반복문을 이용하여 리스트 출력
ls_1 = []

ls_2 = []
value = 1

for i in range(3):
    for j in range(4):
        ls_1.append(value)
        value += 1
    ls_2.append(ls_1)
    ls_1 = []

for i in ls_2:
    for j in i:
        print(j, end="\t")
    print()
print(f"ls_2: {ls_2}")

for i in range(3):      # range(len(ls_2))
    for j in range(4):  # range(len(ls_2[i])
        print(ls_2[i][j], end="\t")
    print()

print("-")

# map = 리스트 안의 문자열을 정수형으로 변환해 줌 (정수형>문자열도 가능)
be = ['2019','12','31']
#test = (int)(be[0])+100
#print(test)
for i in range(len(be)):
    be[i] = int(be[i])
print(be)
be = list(map(int, be))
print(be)

be = [['100','222'],['200','300']]

#for i in range(len(be)):
#    for j in range(len(be[i])):
#        be[i][j] = int(be[i][j])
for i in range(len(be)):
    be[i] = list(map(int, be[i]))
print(be)

be[0][0] = be[0][0] * 100
print(be)

#for i in range(len(be)):
#    for j in range(len(be[i])):
#        be[i][j] = str(be[i][j])
for i in range(len(be)):
    be[i] = list(map(str, be[i]))
print(be)

print("-")

#Q2. 반복문 이용하여 리스트 출력
ls = [
    [['이름'],['나이'],['주소'],['지울값'],['연봉']],
    [['홍길동'],['20살'],['산골자기'],['지우세요'],['5000']],
    [['김개똥'],['30살'],['지구촌'],['지우세요'],['4500']]
    ]
'''
for i in range(len(ls)):
    for j in range(len(ls[i])):
        print(ls[i][j], end="")
    print()

for i in range(len(ls)):
    del(ls[i][3])
    for j in range(len(ls[i])):
        print(ls[i][j], end="")
    print()
'''
#ls[1][4][0] = str(int(int(ls[1][4][0])*1.1))
#print(ls[1][4])

for i in range(len(ls)):
    for j in range(len(ls[i])):
        if j % 3 == 0 and j != 0:
            del(ls[i][j])
            if i != 0:
               ls[i][j][0] = str(int(int(ls[i][j][0])*1.1))

for i in ls:
    for j in i:
        print(j, end="")
    print()    







    






























