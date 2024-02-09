import pandas as pd

data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

df = pd.DataFrame(data)

# Calculate mean, maximum, and minimum of temperature
temperature_mean = df['temperature'].mean()
temperature_max = df['temperature'].max()
temperature_min = df['temperature'].min()

# Display the results
print(f"Mean Temperature: {temperature_mean}")
print(f"Maximum Temperature: {temperature_max}")
print(f"Minimum Temperature: {temperature_min}")