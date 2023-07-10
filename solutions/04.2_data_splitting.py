import pandas as pd

# Create a dictionary with the data
data = {
    'date': ['2023-01-01', '2023-01-05', '2023-01-02', '2023-01-04', '2023-01-03', '2023-01-06', '2023-01-09', '2023-01-07', '2023-01-08', '2023-01-10'],
    'temperature': [25, 23, 22, 20, 24, 18, 19, 21, 20, 22],
    'rainfall': [5, 7, 3, 2, 4, 6, 5, 3, 4, 2],
    'crop_yield': [30, 32, 28, 29, 31, 27, 26, 29, 28, 30]
}

# Create the dataframe
df = pd.DataFrame(data)

# Define the proportions for train, validation, and test sets
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

# First we need to sort the dataset by the desired column
df.sort_values(by='date', ascending=True, inplace=True)

# Calculate the sizes of each set
train_size = int(len(df) * train_ratio)
valid_size = int(len(df) * valid_ratio)
test_size = len(df) - train_size - valid_size

# Split the dataset into train, validation, and test sets
df_train = df[:train_size]
df_valid = df[train_size:train_size+valid_size]
df_test = df[train_size+valid_size:]