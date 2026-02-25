print("시작했다")


print("코딩 1일차 시작")


name = "지안"
age = "17"


print("이름",name)
print("나이",age)


A = "나는개쩔어"
print(A)


name = input("이름을 입력하세요: ")
print("안녕,",name)


age = int(input("나이 입력: "))
print("5년 후의 나이", age+5)


A = int(input("니가 원하는 수: "))
print("니가 원하는 수에 911을 더한 값:", A+911)


A = int(input("니가 원하는 수:"))
if A % 2 ==0 :
    print("짝수")
else:
    print("홀수")


print(10 % 3)


A = int(input("수:"))
if A % 3 ==0 :
    print("3의배수")
else :
    print("3의배수 아님")


for i in range(1, 51):
    if i % 3 ==0 :
        print(i)


for i in range(1, 51):
    if i % 3 ==0 and i % 2 ==0 :
        print(i)


for i in range(1,100 ):
    if i % 3 ==0 or i % 5 ==0 :
        print(i)