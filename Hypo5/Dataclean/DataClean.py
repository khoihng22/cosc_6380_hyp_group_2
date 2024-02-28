import pandas as pd

csv_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/Raw_data.csv'
df = pd.read_csv(csv_file, low_memory=False)



columns_to_keep = [
    'Date', 'Daily Mean PM2.5 Concentration', 'Site Name',  'SITE_LATITUDE', 'SITE_LONGITUDE']


selected_columns_df = df[columns_to_keep]


selected_columns_df.to_csv('/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/Columns_deleted.csv', index=False)

