import pandas as pd


csv_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/Columns_deleted.csv'
df = pd.read_csv(csv_file, low_memory=False)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

df.to_csv('/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/modified_data.csv', index=False)  