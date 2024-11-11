import cv2
import streamlit as st
import numpy as np
from PIL import Image

# Image processing functions
def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright

def blur_image(image, amount):
    blur_amount = int(amount)  # Ensures blur amount is integer
    if blur_amount % 2 == 0:
        blur_amount += 1  # GaussianBlur requires odd kernel size
    blur_img = cv2.GaussianBlur(image, (blur_amount, blur_amount), 0)
    return blur_img

def enhance_details(image):
    hdr = cv2.detailEnhance(image, sigma_s=12, sigma_r=0.15)
    return hdr

# Streamlit app setup
st.title("OpenCV Demo App")
st.subheader("Play with Image Filters using OpenCV and Streamlit")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Convert uploaded image to OpenCV format
    image = Image.open(uploaded_file)
    img = np.array(image.convert('RGB'))  # Convert to RGB array
    
    # Enhance details
    enhanced_img = enhance_details(img)

    # Brighten Image
    brightness = st.slider("Brightness", min_value=0, max_value=100, value=25)
    brightened_img = brighten_image(enhanced_img, amount=brightness)

    # Blur Image
    blur = st.slider("Blur", min_value=1, max_value=21, step=2, value=5)
    blurred_img = blur_image(brightened_img, amount=blur)
    
    # Display final image
    st.image(blurred_img, caption='Processed Image', use_column_width=True)
