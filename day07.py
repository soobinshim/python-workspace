
for i in range(1, 1001):
    sum = 0
    j = 1
    while j < i:
        #print(f"{i} % {j} = {i % j}")
        if i % j == 0:
            sum += j
        j += 1
    if sum == i:
        print(f"{sum}은 완전수다")



N = int(input("수 입력: "))
li = []
for i in range(2, N+1):
    if N % i == 0:
        li.append(i)
    if li == [1,N]:
        print(f"{N}은 소수. {li}")



N = int(input("수 입력: "))
for i in range(2, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:       
            cnt += 1
    if cnt == 2:
        print(f"{i}는 소수")


N = int(input("줄 수를 홀수로 입력하세요: "))
x = int(N/2) + 1
for i in range(1, 2*x):
    if (i <= x):
        for j in range(x-i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        print()
    else:
        for j in range(i-x):
            print(" ", end="")
        for j in range((2*x-i)*2-1):
            print("*", end="")
        print()
    
    























    
    
        


