
ls = []
for i in range(3):
    value = input(f"{i+1}번째 입력: ")
    ls.append(value)
print(ls)

for i in range(len(ls)):
    print(ls[i])

for i in ls:    #ls = [입력한 값 저장되어 있음]
    print(i)

arr = ls

#ls = []    # ls 초기화
ls.clear()  # ls 초기화
print(arr)

ls = [30,20,10]
print(type(ls))     # type() 자료형 알려 줌
print("기본값: ", ls)

ls.append(111)      # .append() 리스트 안에 데이터를 추가하는 용도
print("append: ", ls)

ls.pop()            # .pop() 리스트의 제일 마지막에 있는 값을 제외함
print("pop: ", ls)

ls.reverse()
print("reverse: ", ls)  # .reverse() 리스트 안의 값을 뒤집어 줌

ls.sort()
print("sort: ", ls) # .sort() 리스트 안의 값을 오름차순 정렬

del(ls[2])
print("del: ", ls)  # del() 2번째 값을 제외

#result = ls.index(10)   # .index() 리스트에서 해당 값이 몇 번째에 있는지 알려 줌
result = ls.count(20)    # .count() 리스트에서 해당 값의 개수를 알려 줌
print("count: ", result)

ls.insert(2,200)    # .insert() 리스트의 해당 번째 위치에 값을 넣음
print("insert: ", ls)

ls.remove(200) # 리스트 안의 값을 삭제
print("remove: ", ls)

ls01 = [10,20,30]
ls02 = [40,50,60]
ls = ls01 + ls02
print(ls)
ls02.extend(ls01)     # .extend() 리스트의 값을 더해 줌
print("extend: ", ls02)


print ("-")

#Q1.
ls = []
while True:
    print("1.이름 저장 2.모든 이름 출력 3.특정 이름 삭제 4.종료")
    num = int(input(">>>"))

    if num == 1:
        save_ = input("이름 저장: ")
        if ls.count(save_) != 0:
            print("존재하는 이름입니다")
        else:
            ls.append(save_)
            print("저장 완료")
            
    if num == 2:
        print(ls)
        
    if num == 3:
        remove_ = input("삭제할 이름: ")
        if ls.count(remove_) != 0:
            ls.remove(remove_)
            print("삭제 완료")
        else:
            print("존재하지 않는 이름입니다")

    if num == 4:
        print("종료")
        break
      
#Q2. 
List = ['김개똥',"2002년입사",'잘못된 사항','등급B']
#removeName = input("삭제 입력 : ")
#List.remove( removeName )
del(List[2])
ls = List.copy()
for i in range(3):
    changeName = input("추가할 이름 입력 : ")
    ls[0] = changeName
    #removeName = ls[0]
    #ls.insert(0, changeName )
    #ls.remove(removeName)
    #print(ls)
    List.extend(ls)

for i in range(len(List)):
    if i % 3 == 0 and i != 0:
        print()
    print(List[i], end="/")

# 이차원 리스트
ls = [[1,2,3],[4,5,6],[7,8,9]]
print(ls[0][0])
print(ls[1])
print(ls[2])


#Q3.
ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in ls:
    for j in i:
        print(j, end="\t")
    print()























