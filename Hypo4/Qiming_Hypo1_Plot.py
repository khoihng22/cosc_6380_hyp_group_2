import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm


#---------------------------------------------------------------------------------------------------
# # PM25 WITH Density(100/km2), plot
#---------------------------------------------------------------------------------------------------

# Load the data
file_path = '/home/qm/project/assignment2Group2/population.xlsx'
df = pd.read_excel(file_path, sheet_name='test', usecols=['PM25', 'Population', 'Area(km2)', 'Density(100perkm2)', 'GDP', 'GDPDensity(100GDPperKM2)'])
df['Density(100perkm2)'] = df['Population'] / df['Area(km2)'] /100
df['GDPDensity(100GDPperKM2)'] = df['GDP'] * df['Density(100perkm2)']


df['GDP_squared'] = df['Density(100perkm2)'] ** 2
X = df[['Density(100perkm2)', 'GDP_squared']]
X = sm.add_constant(X)  
y = df['PM25']


model = sm.OLS(y, X).fit()


print(model.summary())


sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
plt.scatter(df['Density(100perkm2)'], df['PM25'], alpha=0.5)


gdp_vals = np.linspace(df['Density(100perkm2)'].min(), df['Density(100perkm2)'].max(), 100)
gdp_squared_vals = gdp_vals ** 2
preds = model.predict(exog=sm.add_constant(np.column_stack((gdp_vals, gdp_squared_vals))))

plt.plot(gdp_vals, preds, color='red', linewidth=2)
plt.title('PM25 vs Density(100perkm2) with Polynomial Regression Line')
plt.xlabel('Density(100perkm2)')
plt.ylabel('PM25')
plt.grid(True)
plt.show()

#---------------------------------------------------------------------------------------------------
# # PM25 WITH GDP, plot 


# # Load the data
# file_path = '/home/qm/project/assignment2Group2/population.xlsx'
# df = pd.read_excel(file_path, sheet_name='test', usecols=['GDP', 'PM25'])


# df['GDP_squared'] = df['GDP'] ** 2
# X = df[['GDP', 'GDP_squared']]
# X = sm.add_constant(X) 
# y = df['PM25']


# model = sm.OLS(y, X).fit()


# print(model.summary())


# sns.set_style('whitegrid')
# plt.figure(figsize=(10, 6))
# plt.scatter(df['GDP'], df['PM25'], alpha=0.5)


# gdp_vals = np.linspace(df['GDP'].min(), df['GDP'].max(), 100)
# gdp_squared_vals = gdp_vals ** 2
# preds = model.predict(exog=sm.add_constant(np.column_stack((gdp_vals, gdp_squared_vals))))

# plt.plot(gdp_vals, preds, color='red', linewidth=2)
# plt.title('PM25 vs GDP with Polynomial Regression Line')
# plt.xlabel('GDP')
# plt.ylabel('PM25')
# plt.grid(True)
# plt.show()
