import streamlit as st
import numpy as np
import cv2
from PIL import Image

def main():
    st.title("Image Processing with OpenCV and Streamlit")
    
    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)

        # Convert to numpy array
        img_array = np.array(image)

        # Convert to grayscale
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2Lab)

        # Display grayscale image
        st.image(gray_image, caption='Grayscale Image', use_container_width=True)

if __name__ == "__main__":
    main()
