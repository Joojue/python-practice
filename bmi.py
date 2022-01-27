def std_weight(height, gender):
    gender = gender
    if gender == "남자":
        std_weight = pow((height/100), 2)*22
    elif gender == "여자":
        std_weight =  pow((height/100), 2)*21
    print("키 %dcm %s의 표준 체중은 %.2fkg입니다." % (height, gender, std_weight))
    return height, gender, std_weight

홍길동 = std_weight(175, "남자")
