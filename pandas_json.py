import pandas.io.json as pd

f = open('data.JSON', 'r')
data = pd.loads(f.read())
df = pd.json_normalize(data , record_path= 'records')

print(df.head(2).to_json())
print(df.head(2).to_json(orient = 'records'))