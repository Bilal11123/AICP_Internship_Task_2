import pandas as pd

data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

df = pd.DataFrame(data)

# Set the index of each row to 'a', 'b', 'c', 'd', 'e', 'f'
df.set_index(pd.Index(['a', 'b', 'c', 'd', 'e', 'f']), inplace=True)

# Display the modified DataFrame
print(df)
