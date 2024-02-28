import pandas as pd
import numpy as np

def round_to_nearest_quarter(value):

    abs_value = abs(value)

    rounded_value = np.round(abs_value * 4) / 4

    fraction = rounded_value % 1
    if fraction == 0.5:
        rounded_value = rounded_value - 0.25 if (abs_value - rounded_value) < 0 else rounded_value + 0.25
    return rounded_value


csv_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/cleaned_data.csv'
df = pd.read_csv(csv_file)


df['SITE_LATITUDE'] = df['SITE_LATITUDE'].apply(round_to_nearest_quarter)
df['SITE_LONGITUDE'] = df['SITE_LONGITUDE'].apply(round_to_nearest_quarter)

output_csv = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/cleaned_data_0.75_0.25.csv'
df.to_csv(output_csv, index=False)
