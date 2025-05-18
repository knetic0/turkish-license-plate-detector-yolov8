import cv2 as cv
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

def predict_and_annotate(img_to_predict: cv.Mat) -> cv.Mat:
    img_to_predict = cv.cvtColor(img_to_predict, cv.COLOR_BGR2RGB)
    results = model.predict(source=img_to_predict, conf=0.5)
    boxes = results[0].boxes
    annotated = img_to_predict.copy()
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].int().tolist()
        conf = box.conf[0].item()
        cls = int(box.cls[0].item())
        label = f"Class {cls} {conf:.2f}"
        cv.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv.putText(annotated, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return annotated