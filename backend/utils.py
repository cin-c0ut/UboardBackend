from ultralytics import YOLO
import cv2
import numpy as np
import json

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive histogram equalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # Denoise
    denoised = cv2.fastNlMeansDenoising(enhanced)
    
    # Convert back to BGR
    return cv2.cvtColor(denoised, cv2.COLOR_GRAY2BGR)

def postprocess_detections(detection_data, min_confidence=0.5):
    # Filter low confidence detections
    valid_indices = [i for i, conf in enumerate(detection_data['confidences']) 
                    if conf >= min_confidence]
    
    filtered_data = {
        'boxes': [detection_data['boxes'][i] for i in valid_indices],
        'confidences': [detection_data['confidences'][i] for i in valid_indices],
        'classes': [detection_data['classes'][i] for i in valid_indices],
        'masks': [detection_data['masks'][i] for i in valid_indices] if detection_data['masks'] else None
    }
    
    return filtered_data

def hold_detection(image_file):
    # Load and preprocess image
    image = cv2.imread(image_file)
    processed_image = preprocess_image(image)
    
    # Load model
    model = YOLO('train4/weights/best.pt')
    
    # Run detection
    result = model(processed_image)[0]
    
    # Prepare detection data
    detection_data = {
        'boxes': result.boxes.xyxy.tolist(),
        'confidences': result.boxes.conf.tolist(),
        'classes': result.boxes.cls.tolist(),
        'masks': result.masks.data.tolist() if result.masks is not None else None
    }
    
    # Post-process detections
    processed_data = postprocess_detections(detection_data)
    
    return processed_data
