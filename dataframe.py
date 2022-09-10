import pandas as pd
data = {'name' : ['Santosh', 'Sandesh', 'Arjun', 'Kalpana'], 'age' : [23, 19, 45, 42]}

df = pd.DataFrame(data)
df.to_csv('fromdf.csv', index=False)
