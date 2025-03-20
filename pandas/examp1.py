import pandas as pd
data = [
    {'name': 'john', 'age': 25, 'city': 'bansgadhi'},
    {'name': 'madhab', 'age': 35, 'city': 'jhapa'},
    {'name': 'dikesh', 'age': 24, 'city': 'pokhara'}
]

data.extend(
    [
        {'name': 'john', 'age': 25, 'city': 'bansgadhi'},
        {'name': 'john', 'age': 25, 'city': 'bansgadhi'}
    ]
)
# convert list to dataframe
df = pd.DataFrame(data)

print(df)


df.info      