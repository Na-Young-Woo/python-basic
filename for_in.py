

for i in range(3):
    print('Hi')


for i in range(5):
    print('Hi')

for i in range(1, 10):
    print('Hello', i)

# Hello 1
# Hello 2
# Hello 3
# Hello 4
# Hello 5
# Hello 6
# Hello 7
# Hello 8
# Hello 9

for i in range(10, 0, -1):
    print(i)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# ===================

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    print(num)

fruits = ('apple', 'orange', 'grape')
for i in fruits:
    print(i)

tuple1 = (2, 4, 5, 6, 7, 8, 3, 6)
for num in tuple1:
    print(num)

# ===================

# count = int(input('반복할 횟수를 입력하시오'))

# for i in range(count):
#     print('Hello, world!')

for i in range(10):
    for fruit in fruits:
        print(i, fruit)


dan = int(input('반복할 단을 입력하시오 (ex.2) '))

for i in range(1, 11):
    print("{}X{}={}".format(dan, i, i*dan))

for i in range(2, 11):
    for j in range(2, 10):
        print('{}X{}={}'.format(i, j, i*j))
