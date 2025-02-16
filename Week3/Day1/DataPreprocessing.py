
import pandas as pd
data = pd.Series([1, 3, 5, 7, 9])
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
df = pd.read_csv(r'train.csv')
print(df.head())
sex = df['Sex'] 
print(sex)