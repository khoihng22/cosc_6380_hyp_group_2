import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.stats import pearsonr


#---------------------------------------------------------------------------------------------------
# # PM25 WITH Density(100/km2), Correlation and P-value 
#---------------------------------------------------------------------------------------------------



# Load the data
file_path = '/home/qm/project/assignment2Group2/population.xlsx'
df = pd.read_excel(file_path, sheet_name='test', usecols=['PM25', 'Population', 'Area(km2)', 'Density(100perkm2)', 'GDP', 'GDPDensity(100GDPperKM2)'])
df['Density(100perkm2)'] = df['Population'] / df['Area(km2)'] /100
df['GDPDensity(100GDPperKM2)'] = df['GDP'] * df['Density(100perkm2)']

# Calculate and print the correlation and p-value
correlation, p_value = pearsonr(df['Density(100perkm2)'], df['PM25'])  # This line is changed
print(f"Correlation between PM25 and Density(100perkm2): {correlation}")
print(f"P-value of the correlation: {p_value}")  # Print the p-value

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['PM25'], df['Density(100perkm2)'], alpha=0.5)
plt.title('PM25 vs Density(100perkm2)')
plt.xlabel('PM25')
plt.ylabel('Density(100perkm2)')
plt.grid(True)
plt.show()




#---------------------------------------------------------------------------------------------------
# # PM25 WITH GDP, Correlation and P-value

# file_path = '/home/qm/project/assignment2Group2/population.xlsx'
# df = pd.read_excel(file_path, sheet_name='test', usecols=['GDP', 'PM25'])

# # Calculate and print the correlation and p-value
# correlation, p_value = pearsonr(df['GDP'], df['PM25'])  # This line is changed
# print(f"Correlation between PM25 and GDP: {correlation}")
# print(f"P-value of the correlation: {p_value}")  # Print the p-value

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.scatter(df['PM25'], df['GDP'], alpha=0.5)
# plt.title('PM25 vs GDP')
# plt.xlabel('PM25')
# plt.ylabel('GDP')
# plt.grid(True)
# plt.show()

