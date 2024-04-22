import openpyxl
import math
open('/Users/piaoruilin/Desktop/DATASCIENCE/PSYC374/midterm/exp1_data.xlsx')

filename = "/Users/piaoruilin/Desktop/DATASCIENCE/PSYC374/midterm/exp1_data.xlsx"

# Function to clean the data
def clean_data(data):
    # Implement your data cleaning logic here
    pass

# Function to calculate mean
def calculate_mean(data):
    total = sum(data)
    return total / len(data)

# Function to calculate standard deviation
def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Function to identify outliers
def identify_outliers(data, mean, std_dev):
    threshold = 3 * std_dev
    outliers = [x for x in data if abs(x - mean) > threshold]
    return outliers

# Main function
def main():
    # Load the Excel file
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active

    # Extract data from the Excel sheet
    data = []
    for row in sheet.iter_rows(values_only=True):
        for value in row:
            # Add your data extraction logic here
            data.append(value)

    # Clean the data
    clean_data(data)

    # Calculate mean and standard deviation
    mean = calculate_mean(data)
    std_dev = calculate_standard_deviation(data)

    # Identify outliers
    outliers = identify_outliers(data, mean, std_dev)

    # Output the results
    print("Mean:", str(mean))
    print("Standard Deviation:", str(std_dev))
    print("Outliers:", str(outliers))


if __name__ == "__main__":
    main()
