## YOLO Object Detection Streamlit App

This repository contains a Streamlit-based web application for real-time object detection using a custom-trained YOLO model. The app allows users to upload images, run predictions, and visualize bounding boxes directly in the browser.

![Ekran Kaydı 2025-05-18 16 20 01 (2)](https://github.com/user-attachments/assets/639d5927-db1a-41eb-b710-37cc9998c366)

### Features

* Upload images via the web interface
* Perform object detection with a YOLO model (Ultralytics)
* Display original and annotated images side by side
* Simple and intuitive UI

### Prerequisites

* Python 3.8 or higher
* A custom YOLOv8 model trained with Ultralytics

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/knetic0/turkish-license-plate-detector-yolov8.git
   cd turkish-license-plate-detector-yolov8
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\\Scripts\\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Place your trained YOLO model weights (`best.pt`) in the `runs/detect/train/weights/` directory.

### Usage

1. Run the Streamlit application:

   ```bash
   streamlit run main.py
   ```

2. Open the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload an image in the "Browse files" section.

4. Click **Predict** to view the detection results.

### File Structure

```
├── plate-detector.ipynb    # Train file
├── prediction.py           # Prediction and Annotate
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── runs/
│   └── detect/
│       └── train/
│           └── weights/
│               └── best.pt # Trained YOLO model
└── README.md               # This documentation file
```

### Customization

* **Model Path**: Change the path to your YOLO weights if stored elsewhere.

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

### License

This project is licensed under the MIT License.

### Contact

For questions or suggestions, please open an issue or contact the maintainer.

- **Email**: solakmehmet02@gmail.com
- **Github**: [Github](https://github.com/knetic0)
- **LinkedIn**: [Mehmet Solak](https://www.linkedin.com/in/mehmetsolak0/)
