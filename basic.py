# 연산자

print("python hi")

print(1+3)
print(5-2)
print(6*7)
print(6/4)
print(6//3)
print(5**2)  # 25
print(5**3)  # 125
print(20 % 3)

print(("Hello "*3)+"hi")


hi = "hello"
print(hi)  # hello

type(hi)  # str

num = 20 % 3
print(num)  # 2

# true
print("나영" != "가영")
# true
print(5 < 7)
# true
result = 11 >= 11
print(result)

result1 = True == 1
print(result1)

result1 = False == 0
print(result1)

# true
print(not(True and False))

age = 5

if age == 5:
    print("5살")
    print("입니다")


l_name = "홍"
f_name = "길동"
age = 20

print(l_name, f_name, age)  # 홍 길동 20
print(l_name+f_name)  # 홍길동

# print 함수

print('이름은', f_name, "나이는", age)
print('이름은' + f_name + "나이는" + str(age))

print('이름은 {} 나이는 {}'.format(f_name, age))

print('이름은 {0} 나이는 {1}'.format(f_name, age))
print('이름은 {1} 나이는 {0}'.format(age, f_name))

print('이름은 %s 나이는 %d' % (f_name, age))
print('p1 = %f' % 3.14)

# List
# list는 일련번호로 구분되는 순서에 따라 데이터가 정렬된 목록 형태의 자료형
# 리스트는 문자열, 정수, 실수 등 모든 자료형을 섞어서 저장할 수 있음


scores = [30, 50, 90, 87, 65, 43]
print(scores)

items = [1, 3, 'hi', 5.6, False, 77, 'World']
print(items)

score0 = scores[0]
print(score0)
print(scores[5])  # 43
print(scores[-1])  # 43, 역순으로 진행
print(scores[-5])  # 50
print(scores[-6])  # 30

scores[1] = 100  # 50이 100으로 변함
print(scores)

print(scores[-7])  # 리스트 범위를 벗어나는 오류

# .append => 추가
scores.append(99)
print(scores[6])
scores.append("안녕?")
print(scores)

# .insert => 삽입
scores.insert(1, "37")  # 들어갈 배열 위치, 들어갈 데이터
scores.insert(2, "hi2")
print(scores)
# [30, '37', 'hi2', 100, 90, 87, 65, 43, 99, 99, '안녕?']

length = len(scores)
print(length)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list1+list2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1*3)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# list 분할

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[0:4])  # [0, 10, 20, 30]
print(numbers[:4])  # [0, 10, 20, 30]
print(numbers[7:11])  # [70, 80, 90, 100]
print(numbers[3:])  # [30, 40, 50, 60, 70, 80, 90, 100]

# range

range(10)  # 0~9
range(1, 10)  # 1~9
range(1, 11)  # 1~10
range(1, 11, 2)  # [1, 3, 5, 7, 9]

list1 = list(range(11))  # 0~10
print(list1)

list2 = list(range(1, 11))  # 1~10
print(list2)

list3 = list(range(1, 11, 2))
print(list3)  # [1, 3, 5, 7, 9]

list3 = list(range(0, 11, 2))
print(list3)  # [0, 2, 4, 6, 8, 10]

list3 = list(range(0, 10, 3))
print(list3)  # [0, 3, 6, 9]

list4 = list(range(10, 0, -1))  # 10~1까지 범위를 가지며 1씩 감소 중
print(list4)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

list4 = list(range(10, 1, -1))  # 10~2까지 범위를 가지며 1씩 감소 중
print(list4)  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

list4 = list(range(10, -1, -1))  # 10~0까지 범위를 가지며 1씩 감소 중
print(list4)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

list4 = list(range(10, 0, -2))  # 10~1까지 범위를 가지며 2씩 감소 중
print(list4)  # [10, 8, 6, 4, 2]

list4 = list(range(10, -1, -2))  # 10~0까지 범위를 가지며 2씩 감소 중
print(list4)  # [10, 8, 6, 4, 2, 0]

# Tuple

# 일련번호로 구분되는 순서에 따라 데이터가 정렬된 목록 형태의 자료형
# tuple은 문자열, 정수, 실수 등 모든 자료형을 섞어서 저장할 수 있음
# list와 달리 내용을 변경 할수 없음
# ()를 사용함

student = ("길동", 'bell', 3, 1.5, True)
print(student)
print(student[0])
student[0] = '허균'  # error

print(tuple(range(10)))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple(range(-5, 16, 2)))  # (-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15)
