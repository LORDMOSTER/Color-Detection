
# 🎨 Coloré – A Click-to-Color Identifier App

**Coloré** is a fun, fast, and easy-to-use web application to detect and name colors from images using Streamlit.

## 🚀 Features

- Upload your own images (.jpg, .png)
- Click on any pixel to identify the color
- Displays:
  - RGB values
  - Closest color name (from 800+ colors)
  - Emoji representation
- Copy RGB value to clipboard
- Fully browser-based – no installations needed

## 🌐 Hosted on Streamlit
You can try the app live here:  
[👉 Click to Launch Coloré on Streamlit](https://color-detection-zzmu2aj88xwcmcs6vbsa2j.streamlit.app/)

## 📦 Installation

```bash
git clone https://github.com/yourusername/colore.git
cd colore
pip install -r requirements.txt
````

### Requirements

* streamlit
* pillow
* pandas
* streamlit-image-coordinates
* pyperclip

## 🛠️ How to Run Locally

```bash
streamlit run app.py
```

## 📂 File Structure

```
📁 colore/
├── app.py                  # Main Streamlit app
├── colors.csv              # Color dataset with RGB and names
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

## 🧠 How It Works

1. User uploads an image.
2. Image is processed using Pillow.
3. Click detection via streamlit-image-coordinates.
4. RGB values are extracted at the clicked pixel.
5. Euclidean distance is used to find the nearest named color from `colors.csv`.
6. Results are displayed along with a color emoji and copy option.

