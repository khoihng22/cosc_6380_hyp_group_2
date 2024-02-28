import pandas as pd
import numpy as np
from scipy.stats import pearsonr


csv_file = '/home/qguo2/Dataa/finaldata.csv' 
df = pd.read_csv(csv_file)


results_df = pd.DataFrame(columns=['Site Name', 'Longitude', 'Latitude', 'Correlation', 'P-value'])


for site_name, group in df.groupby('Site Name'):

    group_clean = group.dropna(subset=['Rainfall', 'Daily Mean PM2.5 Concentration'])


    if len(group_clean) > 1:

        correlation, p_value = pearsonr(group_clean['Rainfall'], group_clean['Daily Mean PM2.5 Concentration'])
        

        longitude = group_clean['SITE_LONGITUDE'].iloc[0]
        latitude = group_clean['SITE_LATITUDE'].iloc[0]
        

        temp_df = pd.DataFrame({
            'Site Name': [site_name],
            'Longitude': [longitude],
            'Latitude': [latitude],
            'Correlation': [correlation if np.isfinite(correlation) else np.nan],  
            'P-value': [p_value if np.isfinite(p_value) else np.nan]  
        })
        results_df = pd.concat([results_df, temp_df], ignore_index=True)


results_csv = '/home/qguo2/Dataa/correlation_p_results.csv'  
results_df.to_csv(results_csv, index=False)
