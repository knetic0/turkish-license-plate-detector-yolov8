import streamlit as st
import numpy as np
import cv2 as cv
import torch

torch.classes.__path__ = []

from prediction import predict_and_annotate

st.title("Turkish License Plate Detector with YOLOv8")

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    image = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    st.image(cv.cvtColor(image, cv.COLOR_BGR2RGB), caption="Uploaded Image")

    if st.button("Predict"):
        prediction_ann = predict_and_annotate(image)
        st.image(cv.cvtColor(prediction_ann, cv.COLOR_BGR2RGB), caption="Predicted Image")
        st.download_button(
            label="Download Annotated Image",
            data=cv.imencode('.jpg', prediction_ann)[1].tobytes(),
            file_name="annotated_image.jpg",
            mime="image/jpeg"
        )
        st.success("Prediction completed!")
        st.balloons()
        st.write("The model has detected the license plate and annotated the image.")
        st.write("You can download the annotated image using the button above.")