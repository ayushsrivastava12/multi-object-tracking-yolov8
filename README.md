# Multi-Object Detection and Tracking using YOLOv8

## Overview
This project implements a computer vision pipeline for detecting and tracking multiple objects in a video. It uses YOLOv8 for object detection and ByteTrack for assigning consistent IDs to objects across frames.

---

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayushsrivastava12/multi-object-tracking-yolov8.git
cd multi-object-tracking-yolov8

2. (Optional) Create virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install required libraries:
pip install ultralytics opencv-python supervision

## Dependencies
Python 3.x
ultralytics (YOLOv8)
opencv-python
supervision

## How to Run the Pipeline
1. Place your input video in the project folder and name it:
input.mp4

2. Run the script:
python main.py
3. Output:
A window showing real-time tracking
Processed video saved as:
output.mp4

## Model / Tracker Choices:
YOLOv8 (yolov8n.pt)
Used for object detection due to its speed and efficiency.
ByteTrack
Used for multi-object tracking and assigning unique IDs to detected objects.
## Assumptions Taken:
Input video contains detectable objects (e.g., people, players)
Objects are visible for most frames
Video quality is sufficient for detection
Objects are not fully occluded for long durations

## Limitations:
ID switching may occur during:
Occlusion
Fast motion
Similar-looking objects
Tracking depends on detection accuracy
No appearance-based tracking (like DeepSORT)
Performance may reduce in crowded scenes
