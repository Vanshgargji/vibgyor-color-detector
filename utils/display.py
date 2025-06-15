import streamlit as st
import cv2

def show_result(output):
    result_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    st.image(result_rgb, caption="Detected Colors", use_column_width=True)
