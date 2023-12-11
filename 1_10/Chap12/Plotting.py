import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('diabetes.csv')
corr = df.corr()
print(corr)
fig, ax = plt.subplots(figsize=(10, 10))
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(df.columns),1)
ax.set_xticks(ticks)
ax.set_xticklabels(df.columns)
plt.xticks(rotation = 500)
ax.set_yticklabels(df.columns)
ax.set_yticks(ticks)
#---print the correlation factor---
for i in range(df.shape[1]):
 for j in range(9):
    text = ax.text(j, i, round(corr.iloc[i][j],2),
    ha="center", va="center", color="w")
plt.show()