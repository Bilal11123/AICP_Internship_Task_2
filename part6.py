import pandas as pd

# Specify the columns you want to import
columns_to_import = ['First Name', 'Sex', 'Email', 'Phone', 'Job Title']

# Specify the rows you want to skip
rows_to_skip = [1, 5]

# Provide the list of columns and skiprows parameter when reading the CSV file
df = pd.read_csv('people.csv', usecols=columns_to_import, skiprows=rows_to_skip)

# Set 'Sex' and 'Job Title' as index columns
df.set_index(['Sex', 'Job Title'], inplace=True)

# Display the DataFrame
print(df)

# Export the DataFrame to a new CSV file
df.to_csv('NewPeople.csv')
