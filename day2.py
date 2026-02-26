#1일차 복습
print("나는빡빡이다")

A = ("김근육")
print("빡빡이", A)

A = input("나는")
print("나는", A)

A = int(input("너가 원하는 수:"))
print("너가 원하는 수에  50을 곱한 값:", A*50)

A = int(input("너가 좋아하는 수:"))
if A % 2 ==0:
    print("너가 좋아하는 수는 짝수이다")
else:
    print("너가 좋아하는 수는 홀수이다")

print("3의 배수이며 2의  배수인 1부터 100까지의 수")
for i in range (1,101):
    if i % 3 ==0 and i % 2 ==0:
        print(i) 

#2일차

#함수
def greet(name):
    print(name+"안녕")
greet(input("당신의 이름"))
greet(input("당신의 이름"))

def hi():
    print("A")
    return "B"
print(hi())

#랜덤숫자출력
import random

num = random.randint(1,10)
print(num)

#동전던지기
import random

coin = random.randint(0,1)
if coin ==0:
    print("뒷면")
else:
    print("앞면")

#while문
count = 1

while count <= 5:
    print(count)
    count += 1

#게임 체력 기능
hp= 20

while hp > 0:
    print("현재 체력:", hp)
    hp -= 5
print("게임오버")