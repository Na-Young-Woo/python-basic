# Set

# 중복되지 않은 데이터들이 모인 집합 형태의 자료형
# 순서가 없음
# { } 를 사용하고 아이템들은 ‘,’(쉼표)로 구분

set1 = {1, 2, 3}
set1.add(4)
print(set1)

set1.update([4, 5, 6])
print(set1)
set1.remove(5)
print(set1)
