import csv
import math

<<<<<<< HEAD
# 먼저 평균을 계산한다.
def calculate_mean(data):
    return sum(data) / len(data)

# 표준편차 계산도 한다. (구글에서 찾은 방법)
=======
# Function to calculate mean
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate standard deviation
>>>>>>> refs/remotes/origin/main
def calculate_std_dev(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

<<<<<<< HEAD
# 아웃라이어 찾는다
=======
# Function to identify outliers
>>>>>>> refs/remotes/origin/main
def identify_outliers(data, mean, std_dev):
    outlier_upper_limit = mean + (3 * std_dev)
    outlier_lower_limit = mean - (3 * std_dev)
    outliers = [x[0] for x in data if x[5] > outlier_upper_limit or x[5] < outlier_lower_limit]
    return set(outliers)

<<<<<<< HEAD
# CSV 파일 읽고 저장한다
=======
# Read data from CSV files and store in a list of lists
>>>>>>> refs/remotes/origin/main
all_data = []
for num in range(1, 6):
    filename = f"P{num}_LDT.csv"
    with open(filename, encoding="cp949") as f:
        reader = csv.reader(f)
<<<<<<< HEAD
        next(reader)  # 구글
        for row in reader:
            all_data.append(row)

# 필요한 부분 찾는다
=======
        next(reader)  # Skip header row
        for row in reader:
            all_data.append(row)

# Extract relevant columns and convert data types
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
        # 안되는 부분은 제외한다
        def error():
            return "Skipping row: {row}"

=======
        # Handle the case where the value cannot be converted to float
        print(f"Skipping row: {row}")

# Calculate mean and standard deviation for accuracy
>>>>>>> refs/remotes/origin/main
accuracy_values = [x[4] for x in extracted_data]
accuracy_mean = calculate_mean(accuracy_values)
accuracy_std_dev = calculate_std_dev(accuracy_values, accuracy_mean)

<<<<<<< HEAD
=======
# Identify outliers
>>>>>>> refs/remotes/origin/main
def identify_outliers(data, mean, std_dev):
    outlier_upper_limit = mean + (3 * std_dev)
    outlier_lower_limit = mean - (3 * std_dev)
    outliers = []
    for x in data:
<<<<<<< HEAD
        if len(x) >= 6:
=======
        if len(x) >= 6:  # Ensure the row has at least 6 elements
>>>>>>> refs/remotes/origin/main
            if x[4] > outlier_upper_limit or x[4] < outlier_lower_limit:
                outliers.append(x[0])
    return set(outliers)

outliers = identify_outliers(extracted_data, accuracy_mean, accuracy_std_dev)

<<<<<<< HEAD
print("acc 평균: ", accuracy_mean)
print("acc 표준편차: ", accuracy_std_dev)
print("acc 아웃라이어(3표준편차 초과): ", accuracy_mean + (3 * accuracy_std_dev))
print("acc 아웃라이어(3표준편차 미만): ", accuracy_mean - (3 * accuracy_std_dev))
print(outliers)
=======
print("Outliers:", outliers)
>>>>>>> refs/remotes/origin/main
