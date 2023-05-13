import pandas as pd
import numpy as np

data = {"grammer":["Python", "C", "Java", "Go", np.nan, "SQL", "PHP", "Python"],"score":[1, 2, np.nan, 4, 5, 6, 7, 10]}
df = pd.DataFrame(data)

print(df)



print(df[df["grammer"]=="Python"])

print(df.columns)

df.rename(columns = {"score": "popularity"}, inplace=True)
print(df)

print(df["grammer"].value_counts())

