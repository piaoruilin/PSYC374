month = int(input("월(1-12)을 입력해 주세요: "))
day = int(input("일(1-31)을 입력해 주세요: "))

new_month = month + 1
if new_month > 12:
  new_month = 1

new_day = day + 1
if new_day > 31:
  new_day = 1
elif new_day > 28 and new_month == 2:
  new_month = 3
  new_day = 1

print("입력하긴 날짜의 다음날은",new_month,"월",new_day,"일입니다.")