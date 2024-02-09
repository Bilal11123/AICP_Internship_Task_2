import pandas as pd

# Create a dictionary with names and ages
data = {'Bilal': 42, 'Ayesha': 38, 'Hadia': 39}

# Create a Pandas Series from the dictionary
series = pd.Series(data, dtype='int64')

# Display the Series
print(series)
