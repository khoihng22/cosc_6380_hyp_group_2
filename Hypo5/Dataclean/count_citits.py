import pandas as pd


csv_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/Columns_deleted.csv'
df = pd.read_csv(csv_file, low_memory=False)

site_counts = df['Site Name'].value_counts()


output_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/countresults.txt'
with open(output_file, 'w') as file:
    for site_name, count in site_counts.items():
        file.write(f"{site_name},{count}\n")