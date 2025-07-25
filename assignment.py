#  SONU KUMAR SHARMA--ECE3A--66
#   Write a code to illustrate panda in python. 



import pandas  as pd

# Step 1: Create a DataFrame

# Example data: List of dictionaries (can also use lists, arrays, etc.)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 120000, 90000, 95000]
}

# Creating DataFrame from the dictionary
df = pd.DataFrame(data)

# Step 2: Basic DataFrame operations

# Display the DataFrame
print("DataFrame:")
print(df)

# Accessing specific columns
print("\nAccessing 'Name' column:")
print(df['Name'])

# Selecting multiple columns
print("\nAccessing 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])

# Step 3: Descriptive statistics

# Get summary statistics of numeric columns
print("\nSummary statistics:")
print(df.describe())

# Step 4: Filtering data (Example: Select rows where Age > 25)
filtered_df = df[df['Age'] > 25]
print("\nRows where Age > 25:")
print(filtered_df)

# Step 5: Adding a new column
df['Bonus'] = df['Salary'] * 0.1  # 10% bonus based on salary
print("\nDataFrame after adding 'Bonus' column:")
print(df)

# Step 6: Modifying data (Example: Update Salary for Alice)
df.loc[df['Name'] == 'Alice', 'Salary'] = 75000  # Update Alice's salary
print("\nDataFrame after updating Alice's salary:")
print(df)

# Step 7: Sorting by a column (Sort by Age)
sorted_df = df.sort_values(by='Age')
print("\nDataFrame sorted by Age:")
print(sorted_df)
