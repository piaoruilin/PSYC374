import pandas as pd
import os
import numpy as np

# Function to read and display an Excel file using pandas
def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f"Data from {file_path}:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Function to handle outliers based on standard deviation
def handle_outliers(df, column, num_sd, method):
    mean = df[column].mean()
    std_dev = df[column].std()
    lower_bound = mean - num_sd * std_dev
    upper_bound = mean + num_sd * std_dev
    original_count = len(df)

    df_filtered = df.copy()
    outliers_mask = (df[column] < lower_bound) | (df[column] > upper_bound)

    if method == 'remove':
        df_filtered = df_filtered[~outliers_mask]
    elif method == 'missing':
        df_filtered.loc[outliers_mask, column] = np.nan
    elif method == 'mean':
        replacement_value = df_filtered.loc[~outliers_mask, column].mean()
        df_filtered.loc[outliers_mask, column] = replacement_value
    elif method == 'median':
        replacement_value = df_filtered.loc[~outliers_mask, column].median()
        df_filtered.loc[outliers_mask, column] = replacement_value

    removed_count = outliers_mask.sum()
    removed_percentage = (removed_count / original_count) * 100

    print(f"Processed {removed_count} outliers ({removed_percentage:.2f}%) using {num_sd} SD criterion.")
    return df_filtered

# Function to print descriptive statistics
def print_statistics(df, columns):
    stats = df[columns].describe().transpose()
    stats['variance'] = df[columns].var()
    print("Descriptive Statistics:")
    print(stats)

# Function to calculate and print distribution
def print_distribution(df, column, n_splits):
    quantiles = np.linspace(0, 1, n_splits + 1)
    distribution = df[column].quantile(quantiles).to_frame()
    distribution['percentage'] = 100 / n_splits
    print(f"Distribution of {column} in {n_splits} splits:")
    print(distribution)

# Function to analyze Correct response, miss, false alarm, correct rejection
def analyze_sdt(df):
    df['SDT'] = np.nan
    df.loc[(df['Cond'] == 'F') & (df['exp_resp.corr'] == 1), 'SDT'] = 'CR'
    df.loc[(df['Cond'] == 'R') & (df['exp_resp.corr'] == 1), 'SDT'] = 'CORR'
    df.loc[(df['Cond'] == 'F') & (df['exp_resp.corr'] == 0), 'SDT'] = 'F_Alarm'
    df.loc[(df['Cond'] == 'R') & (df['exp_resp.corr'] == 0), 'SDT'] = 'Miss'
    
    lenf = len(df[df['Cond'] == 'F'])
    lenr = len(df[df['Cond'] == 'R'])
    CR = len(df[df['SDT'] == 'CR']) / lenf
    CORR = len(df[df['SDT'] == 'CORR']) / lenr
    F_Alarm = len(df[df['SDT'] == 'F_Alarm']) / lenf
    Miss = len(df[df['SDT'] == 'Miss']) / lenr
    
    SDT_total = pd.DataFrame({
        ' ': ['Correct Response', 'Miss', 'False Alarm', 'Correct Rejection'],
        'Count': [len(df[df['SDT'] == 'CORR']), len(df[df['SDT'] == 'Miss']),
                  len(df[df['SDT'] == 'F_Alarm']), len(df[df['SDT'] == 'CR'])],
        'Proportion': [CORR, Miss, F_Alarm, CR]
    })
    print("SDT Analysis:")
    print(SDT_total)

# Main function to run the script
def main():
    # File selection
    while True:
        file_path = input("Enter the path of the directory containing the Excel files: ")
        if os.path.exists(file_path) and os.path.isdir(file_path):
            break
        else:
            print("The specified directory does not exist. Please check the path and try again.")

    # List all Excel files in the directory
    file_list = [f for f in os.listdir(file_path) if f.endswith(('.xlsx', '.xls'))]
    if not file_list:
        print("No Excel files found in the directory.")
        return

    # Read and combine all Excel files
    dataframes = []
    for file_name in file_list:
        df = read_excel_file(os.path.join(file_path, file_name))
        if df is not None:
            dataframes.append(df)
    if not dataframes:
        print("Failed to read any valid Excel files.")
        return

    combined_df = pd.concat(dataframes, ignore_index=True)
    print("Combined DataFrame:")
    print(combined_df.head())

    # Analysis type selection
    while True:
        analysis_type = input("Select analysis type (A, B, C, D, E): ").strip().upper()
        if analysis_type in ['A', 'B', 'C', 'D', 'E']:
            break
        else:
            print("Invalid analysis type selected. Please choose from A, B, C, D, E.")

    column_to_check = 'exp_resp.rt'  # Example column, change as needed

    if analysis_type == 'A':
        num_sd = float(input("Enter the number of standard deviations to use for outlier removal: "))
        combined_df = handle_outliers(combined_df, column_to_check, num_sd, 'remove')
        print("DataFrame after outlier removal:")
        print(combined_df.head())

    elif analysis_type == 'B':
        num_sd = float(input("Enter the number of standard deviations to use for outlier handling: "))
        while True:
            method = input("Enter method to handle outliers (missing, mean, median): ").strip().lower()
            if method in ['missing', 'mean', 'median']:
                break
            else:
                print("Invalid method. Please choose from missing, mean, median.")
        combined_df = handle_outliers(combined_df, column_to_check, num_sd, method)
        print("DataFrame after handling outliers:")
        print(combined_df.head())

    elif analysis_type == 'C':
        columns = ['exp_resp.rt', 'exp_resp.corr']  # Example columns, change as needed
        print_statistics(combined_df, columns)

    elif analysis_type == 'D':
        n_splits = int(input("Enter the number of splits for distribution analysis: "))
        print_distribution(combined_df, column_to_check, n_splits)

    elif analysis_type == 'E':
        analyze_sdt(combined_df)

    # Save the results
    while True:
        output_path = input("Enter the path to save the results (including filename, e.g., results.xlsx): ")
        if os.path.isdir(os.path.dirname(output_path)):
            break
        else:
            print("The specified path to save the results does not exist. Please check the path and try again.")

    combined_df.to_excel(output_path, index=False)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    main()
