
for row in range(10):
    if row == 2:
        break
    print('{}번째 row'.format(row))

for row in range(10):
    if row == 2:
        continue
    print('{}번째 row'.format(row))


# 홀수만 출력
for i in range(12):
    if i % 2 == 0:
        continue
    print(i)

# 아래와 비슷
for i in range(1, 10, 2):
    print(i)


# while

age = 0
while age < 5:
    print('{}살입니다.'.format(age))
    age += 1


age = 0
num = 0
while age < 5:
    while num < 10:
        print('{}살입니다.'.format(age))  # 10번 반복
        num += 1
    num = 0
    age += 1
