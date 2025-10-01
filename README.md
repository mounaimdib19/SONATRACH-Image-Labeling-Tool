# SONATRACH-Image-Labeling-Tool

A simple Streamlit web app for manually classifying seismic images as **Clean** or **Noisy**.  
Specialists can review images one by one, assign labels, and then download the organized datasets.

---

## 🚀 Features
- Upload multiple seismic images (`.png`, `.jpg`, `.jpeg`)
- Display each image with **Clean** / **Noisy** buttons
- Save results automatically in memory
- Download labeled images as **ZIP folders** (Clean and Noisy)

---

## 📦 Installation

1. **Clone this repository** (or copy the script):
   
   git clone <repo-url>
   cd <repo-folder>


2. **Create a virtual environment** (recommended):

   
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   

3. **Install required packages**:
   
   pip install streamlit pillow numpy opencv-python
   

---

## ▶️ Running the App

From the project folder, run:


streamlit run seismic_app.py


Then open the link shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## 📂 Output

* After labeling all images:

  * **Clean images** → downloadable as `clean_images_YYYYMMDD_HHMMSS.zip`
  * **Noisy images** → downloadable as `noisy_images_YYYYMMDD_HHMMSS.zip`


