import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Set the style
sns.set_style('dark')

# Create a pairplot with hue, palette, and dropna settings
sns.pairplot(iris, hue='species', palette='gist_heat', dropna=True)

# Show the plot
plt.show()