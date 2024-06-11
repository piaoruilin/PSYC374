import pandas as pd
import os

###first question
def read_excel_file(phoneme_grapheme):
    try:
        df = pd.read_excel(phoneme_grapheme)
        print(f"Data from {phoneme_grapheme}:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error reading {phoneme_grapheme}: {e}")
        return None
    
# Function to remove outliers based on standard deviation
def remove_outliers(df, column, num_sd):
    mean = df[column].mean()
    std_dev = df[column].std()
    lower_bound = mean - num_sd * std_dev
    upper_bound = mean + num_sd * std_dev
    original_count = len(df)
    df_filtered = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    removed_count = original_count - len(df_filtered)
    removed_percentage = (removed_count / original_count) * 100
    
    print(f"Removed {removed_count} outliers ({removed_percentage:.2f}%) using {num_sd} SD criterion.")
    return df_filtered

# Specify the directory containing the Excel files
directory_path = '/Users/piaoruilin/Desktop/DATASCIENCE/PSYC374/phoneme_grapheme'

# Check if the directory exists
if not os.path.exists(directory_path):
    print(f"Directory {directory_path} does not exist.")
else:
    # List all files in the specified directory
    file_list = os.listdir(directory_path)

    # Initialize an empty list to store DataFrames
    dataframes = []

    # Iterate over the files in the directory and read .xlsx files
    for file_name in file_list:
        if file_name.endswith(".xlsx"):
            file_path = os.path.join(directory_path, file_name)
            df = read_excel_file(file_path)
            if df is not None:
                dataframes.append(df)

    # Concatenate all DataFrames into one
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        #print("Combined DataFrame:")
        #print(combined_df.head())

        # User-defined number of standard deviations for outlier removal
        num_sd = float(input("Enter the number of standard deviations to use for outlier removal: "))
        
        # Specify the column to check for outliers
        column_to_check = 'exp_resp.rt'  # Example column, change as needed

        # Remove outliers
        combined_df = remove_outliers(combined_df, column_to_check, num_sd)
        
        #print("DataFrame after outlier removal:")
        #print(combined_df.head())

    else:
        print("No valid Excel files found in the directory.")
