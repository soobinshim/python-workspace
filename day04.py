'''
if 조건식:
    종속 문장
else:
    종속 문장
다음 문장
'''
num = int(input("수 입력: "))
if num == 1:
    print("1 입력")
else:
    print("그 외의 값 입력")
print("다음 문장 실행")

print("-")

save_id = input("저장할 id 입력: ")
print("인증 프로그램")
input_id = input("비교할 id 입력: ")
if save_id == input_id:
    print("인증 통과")
else:
    print("인증 실패")

print("-")

num = 15
if num % 3 == 0:
    if num % 2 == 0:
        print(f"{num} 2,3의 배수입니다.")
        print(f"{num} 짝수이며 3의 배수입니다")
    else:
        print(f"{num}은 3의 배수이며 짝수는 아니다")
else:
    print(f"{num}은 3의 배수가 아닙니다")

print("-")

'''
bit    : 8 -> 1byte
byte   : 1024 -> 1KB
Kbyte   : 1024 -> 1MB
Mbyte   : 1024 -> 1GB
Gyte   : 1024 -> 1TB

'''
#Q1. 사용자로부터 GByte의 값을 입력받아 Byte, Kbyte, Mbyte로 각각 출력되게 만드시오.
Gbyte = int(input("Gbyte 입력: "))
num = int(input("1.byte 2.Kbyte 3.Mbyte: "))

if num == 1:
    print(f"{Gbyte} : {1024**3*Gbyte} byte")
if num == 2:
    print(f"{Gbyte} : {1024**2*Gbyte} Kbyte")
if num == 3:
    print(f"{Gbyte} : {1024*Gbyte} Mbyte")

print("-")

#Q2. 인증 프로그램을 만드시오.
save_id = input("저장할 ID 입력: ")
save_pw = input("저장할 PW 입력: ")
print("인증 프로그램입니다\nID와 PW를 입력하세요")
input_id = input("ID 입력: ")
input_pw = input("PW 입력: ")

if save_id == input_id:
    if save_pw == input_pw:
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다")
else:
    print("등록되지 않은 아이디입니다")
































