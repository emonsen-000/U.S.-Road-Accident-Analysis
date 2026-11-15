import pandas as pd

df=pd.read_csv("US_Accidents_March23.csv")
df.to_parquet("US_Accidents_March23.parquet", engine="pyarrow", index=False)