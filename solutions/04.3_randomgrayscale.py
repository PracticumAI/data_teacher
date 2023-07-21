import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
image_path = 'images/04/cat.jpg' 
# image source: https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat
image = Image.open(image_path, mode='r')

# Define the RandomGrayscale transformation with a probability of 1.0
transform = transforms.Compose([
    transforms.RandomGrayscale(p=1.0),
])

# Apply the transformation to the image
transformed_image = transform(image)

# Display the original and transformed images using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(transformed_image)
plt.title("Transformed Image")
plt.axis('off')

plt.show()