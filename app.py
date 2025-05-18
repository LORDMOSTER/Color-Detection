import streamlit as st
from PIL import Image
import pandas as pd
import math
from streamlit_image_coordinates import streamlit_image_coordinates
import pyperclip

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv")

colors = load_colors()

def get_closest_color(r, g, b):
    min_dist = float('inf')
    closest_color = ""
    for _, row in colors.iterrows():
        dist = math.sqrt(
            (r - int(row[3]))**2 +
            (g - int(row[4]))**2 +
            (b - int(row[5]))**2
        )
        if dist < min_dist:
            min_dist = dist
            closest_color = row[1]
    return closest_color

if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

if st.session_state.show_welcome:
    st.markdown("""
    <style>
    #welcome-anim {
        background: linear-gradient(135deg, #232526, #fd5949, #d6249f, #285AEB, #232526);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite, fadeOut 2s 2.5s forwards;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0; left: 0;
        z-index: 9999;
    }
    @keyframes gradientShift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    @keyframes popIn {
      0% { transform: scale(0.7); opacity: 0; }
      80% { transform: scale(1.05); opacity: 1; }
      100% { transform: scale(1); }
    }
    @keyframes fadeOut {
      to { opacity: 0; pointer-events: none; }
    }
    #welcome-anim h1 {
      font-size: 3em;
      color: #fd5949;
      margin-bottom: 0.5em;
      animation: popIn 1s;
      letter-spacing: 2px;
      text-shadow: 0 2px 16px #000a;
    }
    #welcome-anim h2 {
      font-size: 1.5em;
      color: #fdf497;
      animation: popIn 1.5s;
      letter-spacing: 1px;
      text-shadow: 0 2px 16px #000a;
    }
    </style>
    <div id="welcome-anim">
        <h1>Welcome to Coloré</h1>
        <h2>Discover colors instantly!</h2>
    </div>
    <script>
    setTimeout(function() {
        var el = window.parent.document.getElementById('welcome-anim');
        if (el) el.style.display = 'none';
    }, 4500);
    </script>
    """, unsafe_allow_html=True)
    st.session_state.show_welcome = False

st.markdown("<h1 class='title'>Coloré</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Click on any image to get RGB value & color name</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    max_width = 800
    st.image(image, caption="Click anywhere on the image.", use_container_width=True, width=max_width)

    coords = streamlit_image_coordinates(image, key="click")

    if coords:
        x, y = int(coords["x"]), int(coords["y"])
        r, g, b = image.getpixel((x, y))
        color_name = get_closest_color(r, g, b)
        
        # Emoji based on color
        emoji = "🎨"
        if "Blue" in color_name:
            emoji = "🔵"
        elif "Red" in color_name:
            emoji = "🔴"
        elif "Green" in color_name:
            emoji = "🟢"
        elif "Yellow" in color_name:
            emoji = "🟡"

        st.markdown(f"""
        <div class="result">
            <div>
                <b>Coordinates:</b> ({x}, {y})<br>
                <b>RGB:</b> ({r}, {g}, {b})<br>
                <b>Closest Color:</b> {color_name}
            </div>
            <div class="emoji">{emoji}</div>
        </div>
        <div class="color-box" style="background-color: rgb({r},{g},{b});"></div>
        """, unsafe_allow_html=True)

        if st.button("Copy RGB to Clipboard"):
            rgb_values = f"{r}, {g}, {b}"
            pyperclip.copy(rgb_values)
            st.success(f"Copied RGB values: {rgb_values}")

