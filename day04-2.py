'''
* while
 반복문
'''
'''
data = "저장값 없음"

while True:
    print("=" * 20)
    print("1. 데이터 입력")
    print("2. 데이터 출력")
    print("3. 종료")
    print("=" * 20)
    
    num = int(input(">>> "))

    if num == 1:
        data = input("데이터 입력: ")
    elif num == 2:
        print("입력 데이터: ", data)
    else:
        print("종료합니다")
        break
'''

while True:
    print("="*40)
    print("\t\tM E N U")
    print("="*40)
    print("1. 학생 이름 입력")
    print("2. 성적 3과목(국,영,수) 입력")
    print("3. 학생 이름 출력")
    print("4. 합계 출력")
    print("5. 평균 출력")
    print("6. 종료")
    print("="*40)

    num = int(input(">>> "))
    
    if num == 1:
        name = input("학생 이름 입력: ")
    elif num == 2:       
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        mat = int(input("수학 점수 입력: "))
    elif num == 3:
        print(f"학생 이름: {name}")
    elif num == 4:
        sum = kor + eng + mat
        print(f"성적 합계: {sum}")
    elif num == 5:
        evr = (kor + eng + mat ) / 3
        print(f"성적 평균: {round(evr,1)}")
    else:
        print("종료합니다")
        break


        















    
    
