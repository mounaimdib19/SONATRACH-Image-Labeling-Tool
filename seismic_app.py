import streamlit as st
import os
import cv2
import numpy as np
import zipfile
import io
from PIL import Image
from datetime import datetime

# Initialize session state
if "images" not in st.session_state:
    st.session_state.images = []
if "filenames" not in st.session_state:
    st.session_state.filenames = []
if "labels" not in st.session_state:
    st.session_state.labels = {}
if "index" not in st.session_state:
    st.session_state.index = 0
if "done" not in st.session_state:
    st.session_state.done = False

def create_zip(folder_name, files):
    """Create a zip buffer from labeled images"""
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for fname, img in files:
            # Save image in memory
            img_pil = Image.fromarray(img)
            img_bytes = io.BytesIO()
            img_pil.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            zip_file.writestr(fname, img_bytes.read())
    zip_buffer.seek(0)
    return zip_buffer

st.title("🖼️ Image Labeling Tool")
st.write("Upload images and classify them as **Clean** or **Noisy**.")

# Upload section
uploaded_files = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], accept_multiple_files=True)

if uploaded_files:
    if not st.session_state.images:  # only load once
        for f in uploaded_files:
            img = Image.open(f)
            st.session_state.images.append(np.array(img.convert("RGB")))
            st.session_state.filenames.append(f.name)

# Show labeling interface
if st.session_state.images and not st.session_state.done:
    idx = st.session_state.index
    img = st.session_state.images[idx]
    fname = st.session_state.filenames[idx]

    st.image(img, caption=f"Image {idx+1}/{len(st.session_state.images)} - {fname}", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🟢 Clean"):
            st.session_state.labels[fname] = "clean"
            st.session_state.index += 1
            if st.session_state.index >= len(st.session_state.images):
                st.session_state.done = True
            st.rerun()
    with col2:
        if st.button("🔴 Noisy"):
            st.session_state.labels[fname] = "noisy"
            st.session_state.index += 1
            if st.session_state.index >= len(st.session_state.images):
                st.session_state.done = True
            st.rerun()

# After labeling all images
if st.session_state.done:
    st.success("✅ All images labeled!")

    # Separate images into two groups
    clean_imgs = [(f, img) for f, img in zip(st.session_state.filenames, st.session_state.images) if st.session_state.labels[f] == "clean"]
    noisy_imgs = [(f, img) for f, img in zip(st.session_state.filenames, st.session_state.images) if st.session_state.labels[f] == "noisy"]

    col1, col2 = st.columns(2)
    with col1:
        if clean_imgs:
            clean_zip = create_zip("clean", clean_imgs)
            st.download_button(
                "📦 Download Clean Images",
                data=clean_zip,
                file_name=f"clean_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                mime="application/zip"
            )
    with col2:
        if noisy_imgs:
            noisy_zip = create_zip("noisy", noisy_imgs)
            st.download_button(
                "📦 Download Noisy Images",
                data=noisy_zip,
                file_name=f"noisy_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                mime="application/zip"
            )
