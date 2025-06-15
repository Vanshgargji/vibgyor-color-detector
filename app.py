import streamlit as st
from utils.image_upload import load_and_prepare_image
from utils.color_definitions import color_ranges, label_colors
from utils.detection import detect_colors
from utils.display import show_result

st.set_page_config(page_title="VIBGYOR Color Detection", layout="centered")
st.title("🌈 VIBGYOR Color Detection App")
st.markdown("Upload an image to detect Violet, Indigo, Blue, Green, Yellow, Orange, and Red regions.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_cv, hsv = load_and_prepare_image(uploaded_file)
    output = detect_colors(image_cv, hsv, color_ranges, label_colors)
    show_result(output)
else:
    st.info("Please upload an image to begin.")
