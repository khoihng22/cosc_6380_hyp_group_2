import pandas as pd
import xarray as xr

# PM25
csv_file = '/home/qm/project/Hypothesis5_PM_Rainfall/DataClean/cleaned_data_0.75_0.25.csv'
df = pd.read_csv(csv_file)

# PRE
nc_file = '/home/qm/project/Hypothesis5_PM_Rainfall/54statesPM_Rainfall/precip.2023.nc'
ds = xr.open_dataset(nc_file)


rainfall_amounts = []

for index, row in df.iterrows():
    date = pd.to_datetime(row['Date'])
    lat = row['SITE_LATITUDE']
    lon = row['SITE_LONGITUDE']

    rainfall = ds['precip'].sel(time=date, lat=lat, lon=lon, method='nearest').values.item()
    

    rainfall_amounts.append(rainfall)


df['Rainfall'] = rainfall_amounts


output_csv = '/home/qm/project/Hypothesis5_PM_Rainfall/finaldata.csv'
df.to_csv(output_csv, index=False)
