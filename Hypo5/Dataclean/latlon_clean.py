import pandas as pd


csv_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/modified_data.csv'


df = pd.read_csv(csv_file)


print("原始数据行数:", len(df))

if 'SITE_LATITUDE' in df.columns and 'SITE_LONGITUDE' in df.columns:

    df_cleaned = df.dropna(subset=['SITE_LATITUDE', 'SITE_LONGITUDE'])
    print("清洗后数据行数:", len(df_cleaned))
else:
    print("警告：数据中缺少 'SITE_LATITUDE' 或 'SITE_LONGITUDE' 列。")
    df_cleaned = df

output_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/cleaned_data.csv'  
df_cleaned.to_csv(output_file, index=False)


