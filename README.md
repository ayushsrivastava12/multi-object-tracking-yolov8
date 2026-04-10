# Multi-Object Detection and Tracking using YOLOv8

## Overview
This project implements a real-time multi-object detection and tracking system using YOLOv8 and ByteTrack. The system detects multiple objects in a video and assigns a unique ID to each object, maintaining consistency across frames.

---

## Features
- Real-time object detection using YOLOv8  
- Multi-object tracking with persistent ID assignment  
- Bounding box visualization with labels  
- Handles multiple moving objects in video  
- Filters low-confidence detections for improved stability  

---

## Technologies Used
- Python  
- OpenCV  
- Ultralytics YOLOv8  
- Supervision (ByteTrack)

---

## How It Works

1. **Load YOLOv8 Model**
   - Pre-trained model (`yolov8n.pt`) is used for object detection.

2. **Read Video**
   - Input video is processed frame-by-frame using OpenCV.

3. **Object Detection**
   - YOLO detects objects and returns bounding boxes and confidence scores.

4. **Filter Detections**
   - Low-confidence detections are removed to improve tracking accuracy.

5. **Object Tracking**
   - ByteTrack assigns unique IDs and tracks objects across frames.

6. **Annotation**
   - Bounding boxes and IDs are drawn on each frame.

7. **Output**
   - Processed video is displayed and saved as `output.mp4`.

---
