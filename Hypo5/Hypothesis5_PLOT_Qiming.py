import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/home/qm/project/Hypothesis5_PM_Rainfall/correlation_p_results.csv')


df['Abs_Correlation'] = df['Correlation'].abs()


plt.figure(figsize=(10, 6))
plt.scatter(df[df['P-value'] >= 0.05]['P-value'], df[df['P-value'] >= 0.05]['Abs_Correlation'], color='blue', alpha=0.7, label='P-value >= 0.05')

plt.scatter(df[df['P-value'] < 0.05]['P-value'], df[df['P-value'] < 0.05]['Abs_Correlation'], color='green', alpha=0.7, label='P-value < 0.05')


plt.legend()
plt.axvline(x=0.05, color='red', linestyle='-', label='P=0.05 significance threshold')
plt.title('P-value vs. Absolute Correlation')
plt.xlabel('P-value')
plt.ylabel('Absolute Correlation')
plt.grid(True)
plt.show()