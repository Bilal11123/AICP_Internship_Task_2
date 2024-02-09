data = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'Kabir', 'jazim'],
    'Age': [27, 24, 22, 32, 23],
    'Address': ['Lahore', 'Karachi', 'Sialkot', 'Peshawar', 'lhr'],
    'Qualifications': ['Msc', 'MA', 'MCA', 'Phd', 'bsc']
}

AICP_DF = pd.DataFrame(data)

# Select the 'Name' and 'Qualifications' columns and save them to df1
df1 = AICP_DF[['Name', 'Qualifications']]

# Add a new column 'Height' to AICP_DF
AICP_DF['Height'] = [5.1, 6.2, 5.1, 5.2, 5.1]

# Set 'Name' as the index column
AICP_DF.set_index('Name', inplace=True)

# Display the modified DataFrame
print("AICP_DF:")
print(AICP_DF)

# Retrieve row with index 'Hifza'
row_hifza = AICP_DF.loc['Hifza']
print("\nRow with index 'Hifza':")
print(row_hifza)

# Retrieve row with index 3
row_index_3 = AICP_DF.iloc[2]  # Note: Indices start from 0, so index 2 corresponds to the third row
print("\nRow with index 3:")
print(row_index_3)

# Drop row with index 'Bilal'
AICP_DF.drop(index='Bilal', inplace=True)

# Display the DataFrame after dropping the row
print("\nAICP_DF after dropping row 'Bilal':")
print(AICP_DF)
