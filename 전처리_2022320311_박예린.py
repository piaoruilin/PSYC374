import csv
import math

# Function to calculate mean
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate standard deviation
def calculate_std_dev(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Function to identify outliers
def identify_outliers(data, mean, std_dev):
    outlier_upper_limit = mean + (3 * std_dev)
    outlier_lower_limit = mean - (3 * std_dev)
    outliers = [x[0] for x in data if x[5] > outlier_upper_limit or x[5] < outlier_lower_limit]
    return set(outliers)

# Read data from CSV files and store in a list of lists
all_data = []
for num in range(1, 6):
    filename = f"P{num}_LDT.csv"
    with open(filename, encoding="cp949") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            all_data.append(row)

# Extract relevant columns and convert data types
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
        # Handle the case where the value cannot be converted to float
        print(f"Skipping row: {row}")

# Calculate mean and standard deviation for accuracy
accuracy_values = [x[4] for x in extracted_data]
accuracy_mean = calculate_mean(accuracy_values)
accuracy_std_dev = calculate_std_dev(accuracy_values, accuracy_mean)

# Identify outliers
def identify_outliers(data, mean, std_dev):
    outlier_upper_limit = mean + (3 * std_dev)
    outlier_lower_limit = mean - (3 * std_dev)
    outliers = []
    for x in data:
        if len(x) >= 6:  # Ensure the row has at least 6 elements
            if x[4] > outlier_upper_limit or x[4] < outlier_lower_limit:
                outliers.append(x[0])
    return set(outliers)

outliers = identify_outliers(extracted_data, accuracy_mean, accuracy_std_dev)

print("Outliers:", outliers)
