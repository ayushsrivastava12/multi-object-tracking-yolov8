# Multi-Object Detection and Tracking

## Overview
This project performs multi-object detection and tracking on sports/event video using YOLOv8 and DeepSORT.

## Features
- Detects multiple objects (players/people)
- Assigns unique IDs
- Maintains ID consistency across frames
- Handles occlusion and motion

## Technologies Used
- Python
- YOLOv8 (Ultralytics)
- DeepSORT
- OpenCV

## How to Run
1. Install dependencies:
   pip install ultralytics opencv-python deep-sort-realtime

2. Run:
   python main.py

## Output
- Annotated video saved as output.mp4

## Challenges
- ID switching during occlusion
- Similar-looking players

## Improvements
- Can use custom trained model
- Add re-identification model
- Improve tracking with more tuning