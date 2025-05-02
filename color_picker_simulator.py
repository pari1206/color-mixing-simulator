import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Color Picker & Mixing Simulator", layout="centered")
st.title("🎨 IoT-Based Color Recognition and Mixing Simulator")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Click anywhere on the image to select a color", use_column_width=True)

    # Convert image to NumPy array
    img_array = np.array(image)

    # Display the image with click interaction
    st.write("Click on the image below to get RGB values:")

    # Let user click on image
    clicked = st.image(image, use_column_width=True)

    x = st.number_input("X-coordinate (horizontal)", min_value=0, max_value=img_array.shape[1] - 1, value=0)
    y = st.number_input("Y-coordinate (vertical)", min_value=0, max_value=img_array.shape[0] - 1, value=0)

    # Get RGB from selected pixel
    r, g, b = img_array[y, x]
    total = r + g + b if (r + g + b) != 0 else 1

    # Normalize to simulate pump timing (%)
    r_perc = r / total * 100
    g_perc = g / total * 100
    b_perc = b / total * 100

    # Show selected color and RGB
    st.markdown(f"**🟥 Selected Color RGB:** ({r}, {g}, {b})")
    st.markdown(
        f"<div style='width:100px;height:50px;background-color:rgb({r},{g},{b});border:1px solid #000'></div>",
        unsafe_allow_html=True
    )

    # Simulate pump output
    st.subheader("🔧 Simulated Pump Mixing Output")
    st.write(f"🔴 Red: {r_perc:.1f}%")
    st.write(f"🟢 Green: {g_perc:.1f}%")
    st.write(f"🔵 Blue: {b_perc:.1f}%")

    # Plot bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(['Red', 'Green', 'Blue'], [r_perc, g_perc, b_perc], color=['red', 'green', 'blue'])
    ax.set_ylim(0, 100)
    ax.set_ylabel('Pump Output (%)')
    st.pyplot(fig)

else:
    st.info("👆 Upload an image to get started.")
