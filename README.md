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
   ```bash
   git clone <repo-url>
   cd <repo-folder>
````

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install streamlit pillow numpy opencv-python
   ```

---

## ▶️ Running the App

From the project folder, run:

```bash
streamlit run seismic_app.py
```

Then open the link shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## 📂 Output

* After labeling all images:

  * **Clean images** → downloadable as `clean_images_YYYYMMDD_HHMMSS.zip`
  * **Noisy images** → downloadable as `noisy_images_YYYYMMDD_HHMMSS.zip`

---

Do you want me to also **generate the `requirements.txt` file** for you so you can run `pip install -r requirements.txt` directly?
```
