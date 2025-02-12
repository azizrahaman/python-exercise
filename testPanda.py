import pandas as pd

# Load a CSV file into a DataFrame
df = pd.read_csv('refined_ecommerce_product_data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Basic data manipulation
# df['CCCCC'] = df['Product_Name'] + "Hola"

# Save the modified DataFrame to a new CSV file
# df.to_csv('modified_data.csv', index=False)
print(df.describe())