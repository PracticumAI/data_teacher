import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Load the dataset
data = pd.read_csv('data/Iris.csv')

# Create scatter plots for each species: Iris-setosa, Iris-versicolor, and Iris-virginica
plt.scatter(data[data['Species'] == 'Iris-setosa']['SepalLengthCm'], data[data['Species'] == 'Iris-setosa']['SepalWidthCm'], label='Iris-setosa', color='red')
plt.scatter(data[data['Species'] == 'Iris-versicolor']['SepalLengthCm'], data[data['Species'] == 'Iris-versicolor']['SepalWidthCm'], label='Iris-versicolor', color='blue')
plt.scatter(data[data['Species'] == 'Iris-virginica']['SepalLengthCm'], data[data['Species'] == 'Iris-virginica']['SepalWidthCm'], label='Iris-virginica', color='green')

# Add labels and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Scatter Plot of Sepal Length vs Sepal Width by Species')

# Add legend
plt.legend()

# Show the plot
plt.show()