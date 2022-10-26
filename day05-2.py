for i in range(0,10): # i=0,i<10,i+=1
    print(i, end=", ")
    
print("-"*10)
for i in range( 10 ): # i=0, i<10, i+=1
    print(i, end=", ")
print("-"*10)
sum_=0; sum2 = 0;
for i in range(1, 101 ):
    sum_ += i
    if i % 3 == 0 and i%5 != 0:
        sum2 += i
print( sum_ - sum2 )

print("-"*10)
num1 = int( input("수 입력 : "))
num2 = int( input("수 입력 : "))

sum_ = 0
if num1 > num2:
    max_ = num1
    min_ = num2
    #n = -1
else:
    max_, min_ = num2, num1
    #n = 1
    
for i in range(min_, max_ + 1 ):
    sum_ += i
print(sum_)


for day in range(1, 31):
    if day == 1:
        won = 10
    else:
        won = won * 2
print(f"30날 입금할 금액 : {won}")











        








