import pandas as pd

surface_data = pd.read_csv(
    "codeinsee.csv",
    sep=";",
    dtype=str
)

print(surface_data.columns.tolist())
print(surface_data.head())
print(surface_data.shape)