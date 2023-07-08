import pandas as pd

# create a sample data frame
data = pd.DataFrame({'crop_yield': [50, 100, 75, 120, 90, 80, 110, 95]})

# create bins for different yield categories
bins = [0, 80, 100, 120, float('inf')]
labels = ['low', 'medium', 'high', 'very high']
data['yield_category'] = pd.cut(data['crop_yield'], bins=bins, labels=labels)

# display the updated data frame
print(data)