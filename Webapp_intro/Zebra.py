import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to convert image to grayscale
def convert_to_grayscale(image):
    # Convert PIL Image to OpenCV format
    cv_image = np.array(image)
    img = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert grayscale image back to PIL format
    gray_pil_image = Image.fromarray(gray_img)

    return gray_pil_image

def main():
    st.set_page_config(layout="wide", page_title="Convert Colour to Grey Scale")

    st.title("Convert a Colour Image to Grey")

    st.write(":dog: Try uploading an image to convert a colour image to gray. Full-quality images can be downloaded from the sidebar.:grin:")

    # Create the file uploader
    my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Create the columns
    col1, col2 = st.columns(2)

    # Convert the image!
    if my_upload is not None:
        input_image = Image.open(my_upload)
        col1.image(input_image, use_column_width=True, caption="Original Image :camera:")

        # Convert to grayscale
        gray_image = convert_to_grayscale(input_image)

        col2.image(gray_image, use_column_width=True, caption="Converted Image :wrench:")
    else:
        st.sidebar.warning("Please upload an image.")

if __name__ == "__main__":
    main()







