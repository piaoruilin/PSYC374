import pandas as pd

data = pd.read_csv('organizations-1000.csv')

#결과1
filter1_data = data[(data['Industry'] == 'Library') | (data['Country'] == 'Korea')]
filter1_data.to_excel('pandas결과1_2022320311_박예린.xlsx', index=False)

#결과2
filter2_data = data[data['Founded'] < 2000]
filter22_data = filter2_data.groupby(['Industry', 'Country'])['Number of employees'].mean().reset_index()
filter22_data.to_excel('pandas결과2_2022320311_박예린.xlsx', index=False)
