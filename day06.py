for i in range(0,3,1):
    print('상위for문 실행')
    for k in range(0,5,1):
        print(f"이중 for문 i:{i}, k:{k}")
    print('상위for문 종료')

# 구구단. 2*1=2
for i in range(2,10,1):
    for k in range(1,10,1):
        print(f"{i} * {k} = { i*k }")


for i in range(0,5,1):
    print(f'상위포문 {i} 일때 하위 포문 : ', end=" ")
    for k in range(0,5,1):
        print(f"{ i*k }", end=" ")
    print()

for i in range(0,5):
    for j in range(1,6):
        print(j + (5*i) ,end = '\t')
    print()







        
