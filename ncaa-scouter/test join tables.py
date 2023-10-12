import pandas as pd

# Sample data for two tables
data1 = {'ID': [1, 2, 3, 4],
         'Value1': ['A', 'B', 'C', 'D']}
data2 = {'ID': [3, 4, 5, 6],
         'Value2': ['X', 'Y', 'Z', 'W']}

# Create DataFrames from the sample data
table1 = pd.DataFrame(data1)
table2 = pd.DataFrame(data2)

# Merge the tables on the 'ID' column, combining data from both tables
merged_table = pd.merge(table1, table2, on='ID', how='outer')

# Display the merged table
print(table1)
print()
print(table2)
print()
print(merged_table)
