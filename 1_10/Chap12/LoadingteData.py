import numpy as np
import pandas as pd
df = pd.read_csv('diabetes.csv')
df.info()

#---check for null values---
print("Nulls")
print("=====")
print(df.isnull().sum())