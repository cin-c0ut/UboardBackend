from ultralytics import YOLO
import cv2
import numpy as np
import json

def hold_detection(image_file):
    model = YOLO('train4/weights/best.pt')
    image = cv2.imread(image_file)
    print(f'image_file: {image_file}')

    result = model(image)[0]
    detection_data = {
        'boxes' : result.boxes.xyxy.tolist(),
        'confidences': result.boxes.conf.tolist(),
        'classes': result.boxes.cls.tolist(),
        'masks': result.masks.data.tolist() if result.masks is not None else None
    }

    return detection_data
