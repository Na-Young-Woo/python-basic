# 제어문 (if, if-else)

adult = 8
gender = "녀"

if 7 < adult < 19:

    print('당신은 미성년자입니다')
    if gender == "여" or "녀":
        print('그리고 여자군요')
    elif gender == "남":
        print('그리고 남자군요')
    else:
        print('아직 성별을 정확히 입력하지 않았군요')

elif adult > 19:
    print('당신은 성인입니다')

elif adult <= 7:
    print('세상에 당신은 아기군요!')

else:
    print('나이를 정확히 입력해주세요')


# ==========================


score = 90

if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'F'

print(result)
