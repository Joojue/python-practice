weeks = range(1, 51)
for week in weeks:
    with open("{0}주차.txt".format(week), "w", encoding="utf8") as file:
        file.write("- {0}주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :".format(week))