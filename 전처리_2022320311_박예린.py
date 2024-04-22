import csv
import math

# 먼저 평균을 계산한다.
def calculate_mean(data):
    return sum(data) / len(data)

# 표준편차 계산도 한다. (구글에서 찾은 방법)
def calculate_std_dev(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# 아웃라이어 찾는다
def identify_outliers(data, mean, std_dev):
    outlier_upper_limit = mean + (3 * std_dev)
    outlier_lower_limit = mean - (3 * std_dev)
    outliers = [x[0] for x in data if x[5] > outlier_upper_limit or x[5] < outlier_lower_limit]
    return set(outliers)

# CSV 파일 읽고 저장한다
all_data = []
for num in range(1, 6):
    filename = f"P{num}_LDT.csv"
    with open(filename, encoding="cp949") as f:
        reader = csv.reader(f)
        next(reader)  # 구글
        for row in reader:
            all_data.append(row)

# 필요한 부분 찾는다
extracted_data = []
for row in all_data:
    participant = row[2]
    syllables = row[36]
    lexicality = row[37]
    rt = row[26]
    acc = row[25]
    try:
        syllables = float(syllables)
        lexicality = float(lexicality)
        rt = float(rt)
        acc = float(acc)
        extracted_data.append([participant, syllables, lexicality, rt, acc])
    except ValueError:
        # 안되는 부분은 제외한다
        def error():
            return "Skipping row: {row}"

accuracy_values = [x[4] for x in extracted_data]
accuracy_mean = calculate_mean(accuracy_values)
accuracy_std_dev = calculate_std_dev(accuracy_values, accuracy_mean)

def identify_outliers(data, mean, std_dev):
    outlier_upper_limit = mean + (3 * std_dev)
    outlier_lower_limit = mean - (3 * std_dev)
    outliers = []
    for x in data:
        if len(x) >= 6:
            if x[4] > outlier_upper_limit or x[4] < outlier_lower_limit:
                outliers.append(x[0])
    return set(outliers)

outliers = identify_outliers(extracted_data, accuracy_mean, accuracy_std_dev)

print("acc 평균: ", accuracy_mean)
print("acc 표준편차: ", accuracy_std_dev)
print("acc 아웃라이어(3표준편차 초과): ", accuracy_mean + (3 * accuracy_std_dev))
print("acc 아웃라이어(3표준편차 미만): ", accuracy_mean - (3 * accuracy_std_dev))
print(outliers)
