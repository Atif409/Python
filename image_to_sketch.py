import cv2
import numpy as np

def create_sketch(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (21, 21), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, threshold1=10, threshold2=5)
    
    # Invert the binary image to get a white sketch on black background
    inverted_edges = cv2.bitwise_not(edges)
    
    return inverted_edges

# Provide the path to the input image
input_image_path = "1.jfif"

# Create the sketch
sketch = create_sketch(input_image_path)

# Display the sketch
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
