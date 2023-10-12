import pandas as pd

# Sample DataFrame with unknown column names
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}

df = pd.DataFrame(data)

df.iloc[:, 0:2] = df.iloc[:, 0:2].astype(int)


# Calculate the mean for each row without knowing column names
df['Mean'] = df.iloc[:, 0:2].mean(axis=1)

# Display the updated DataFrame
print(df)
