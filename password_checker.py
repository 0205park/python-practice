
import string

print("=== 비밀번호 안전도 검사 ===")

password = input("비밀번호 입력: ")
score = 0

if len(password) >= 8:
    score += 1

if len(password) >= 12:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in string.punctuation for c in password):
    score += 1

print("안전도 점수:", score, "/ 6")

if score >= 5:
    print("안전한 비밀번호입니다.")
elif score >= 3:
    print("보통 수준의 비밀번호입니다.")
else:
    print("취약한 비밀번호입니다.")

print("※ 이 결과만으로 실제 보안을 보장할 수 없습니다.")
