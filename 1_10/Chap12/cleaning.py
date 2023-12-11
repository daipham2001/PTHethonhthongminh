# import numpy as np
import pandas as pd
df = pd.read_csv('diabetes.csv')

#---check for null values---
print("Nulls")
print("=====")
print(df.isnull().sum())

#---check for 0s---
print("0s")
print("==")
print(df.eq(0).sum())