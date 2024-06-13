import pandas as pd

# 사용자로부터 피험자 수 입력 받기
num_participants = int(input("피험자 수를 입력하세요: "))

data = {
    "참가자": [],
    "Hit Rate": [],
    "Miss Rate": [],
    "False Alarm Rate": [],
    "Correct Rejection Rate": []
}

#리스트에 저장
for i in range(num_participants):
    participant = input(f"피험자 {i+1}의 이름을 입력하세요: ")
    hit_rate = float(input(f"{participant}의 Hit Rate을 입력하세요: "))
    miss_rate = float(input(f"{participant}의 Miss Rate을 입력하세요: "))
    false_alarm_rate = float(input(f"{participant}의 False Alarm Rate을 입력하세요: "))
    correct_rejection_rate = float(input(f"{participant}의 Correct Rejection Rate을 입력하세요: "))

    data["참가자"].append(participant)
    data["Hit Rate"].append(hit_rate)
    data["Miss Rate"].append(miss_rate)
    data["False Alarm Rate"].append(false_alarm_rate)
    data["Correct Rejection Rate"].append(correct_rejection_rate)

df = pd.DataFrame(data)
print(df)

#엑셀 파일로 저장
df.to_excel("GPC_data.xlsx", index=False)


