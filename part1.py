import pandas as pd

# Create a Pandas Series
data = [1, 4, 9, 6, 7]
index = ['a', 'x', 'c', '2', 'e']
series = pd.Series(data, index=index, dtype='int64')

# Display the Series
print(series)
