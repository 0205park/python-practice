
print("=== 성적 평균 계산기 ===")

subjects = int(input("과목 수를 입력하세요: "))
scores = []

for i in range(subjects):
    score = float(input(f"{i+1}번째 과목 점수: "))
    scores.append(score)

if len(scores) > 0:
    average = sum(scores) / len(scores)

    print("총점:", sum(scores))
    print("평균:", round(average, 2))

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("학점:", grade)
else:
    print("입력된 과목이 없습니다.")
