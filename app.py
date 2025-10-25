import streamlit as st
from ui import render_ui
from image_utils import load_image
from algorithms import sobel, laplacian, canny

st.set_page_config(page_title="Edge Detection Visualizer", layout="wide")

def main():
    st.title("Edge Detection Visualizer")

    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])

    if image_file:
        image = load_image(image_file)

        algo_name, params = render_ui()

        if algo_name == "Sobel":
            output = sobel.apply_sobel(image, params)
        elif algo_name == "Laplacian":
            output = laplacian.apply_laplacian(image, params)
        elif algo_name == "Canny":
            output = canny.apply_canny(image, params)
        else:
            st.warning("Select a valid algorithm.")
            return

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Input Image")
            st.image(image, use_column_width=True)
        with col2:
            st.subheader(f"Output ({algo_name})")
            st.image(output, use_column_width=True)
    else:
        st.info("Please upload an image to begin.")

if __name__ == "__main__":
    main()
