import cv2
import numpy as np
import os

# Create a blank image (500x500 pixels, white background)
img = np.ones((500, 500, 3), np.uint8) * 255

# Draw a simple face
cv2.circle(img, (250, 250), 100, (0, 0, 0), 2)  # Head
cv2.circle(img, (200, 220), 20, (0, 0, 0), -1)  # Left eye
cv2.circle(img, (300, 220), 20, (0, 0, 0), -1)  # Right eye
cv2.ellipse(img, (250, 300), (50, 20), 0, 0, 180, (0, 0, 0), 2)  # Smile

# Save the image
current_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_dir, 'test_image.png')
cv2.imwrite(output_path, img)
print(f"Test image created successfully at: {output_path}")
