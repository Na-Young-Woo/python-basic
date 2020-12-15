# dictionary

# 키(key)-값(value)로 연관된 데이터들이 순서 없이 모인 자료형
# 키를 통해서 데이터에 접근 가능
# { } 를 사용하고 키:값 형식으로 저장하고 ‘,’(쉼표)로 구분한다.
# 키는 중복될 수 없다.

student = {'name': '홍길동', 'major': '정보통신학과', 'score': 4.2}
print(student)
scores = {1: 3.5, 2: 4.0, 3: 4.3, 4: 4.2}
print(scores)

# 생성
dic1 = {}  # 빈 딕셔너리 생성
print(dic1)

dic2 = dict()  # 생성자로 생성
print(dic2)
dic3 = {'name': 'item', 1: 3.5, False: [1, 2, 3]}
print(dic3)

dic4 = dict(name='길동', height=180, age=20)
print(dic4)  # 생성자로 생성해서 넣어주기

# 키 값 가져오기
students = {'name': '홍길', 1: 3.5, False: [1, 2, 3]}
print(students['name'])
print(students[False])
print(scores[1])
print(scores[2])

# 키 값 수정 및 추가

students['major'] = '정보통신'
print(students)

dic4['major'] = '사학과'
print(dic4)

del students[1]
print(students)

del scores[1]
print(scores)


student01 = dict(name='길동', major='정통과', scores=3.5)

print(student01.items())
print(student01.keys())
print(student01.values())

student02 = {'name': '길동', 'major': "정통과", "scores": 3.5}

print(student02.items())
# dict_items([('name','홍길동'), ('major','정통과'), ('score', 3.5)])
print(student02.keys())
# dict_keys(['name', 'major', 'score'])
print(student02.values())
# dict_values(['홍길동','정통과', 3.5])


# 실제로 사용할 때
student01 = dict(name='길동', major='정통과', scores=3.5)

# [('name', '길동'), ('major', '정통과'), ('scores', 3.5)]
print(list(student01.items()))
print(list(student01.keys()))
print(list(student01.values()))
