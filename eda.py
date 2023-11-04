from load import diabetes_df
insight_1 = diabetes_df.describe()

# Save insight as a text file
with open('eda-1.txt', 'w') as file:
    file.write(insight_1.to_string())

# 2. Insight 2
# Check the first few rows of the dataset
insight_2 = diabetes_df.head()

# Save insight as a text file
with open('eda-2.txt', 'w') as file:
    file.write(insight_2.to_string())

# 3. Insight 3
# Get unique values in a specific column
insight_3 = diabetes_df['Pregnancies'].unique()

# Save insight as a text file
with open('eda-3.txt', 'w') as file:
    for item in insight_3:
        file.write("%s\n" % item)