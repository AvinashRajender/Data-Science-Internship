import pandas as pd

# Skip the first 5 rows so Pandas uses the correct header
df = pd.read_excel("data/Inventory-Records-Sample-Data.xlsx", skiprows=5)

# Clean column names
df.columns = [col.strip().replace("\n", " ") for col in df.columns]

print("Columns:", df.columns.tolist())
print(df.head())
