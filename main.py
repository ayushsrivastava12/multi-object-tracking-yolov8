from ultralytics import YOLO
import cv2
import supervision as sv

# Load YOLO model
model = YOLO("yolov8n.pt")

# ByteTrack (safe version - works with all supervision versions)
tracker = sv.ByteTrack()

# Open video
cap = cv2.VideoCapture("input.mp4")

# Video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

# Annotators
box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detection
    results = model(frame)[0]

    # Convert to supervision format
    detections = sv.Detections.from_ultralytics(results)

    # Filter weak detections (important for stability)
    detections = detections[detections.confidence > 0.5]

    # Update tracker
    detections = tracker.update_with_detections(detections)

    # Create labels safely
    labels = []
    if detections.tracker_id is not None:
        for tracker_id in detections.tracker_id:
            if tracker_id is None:
                labels.append("ID ?")
            else:
                labels.append(f"ID {tracker_id}")

    # Draw boxes
    annotated_frame = box_annotator.annotate(frame, detections)

    # Draw labels
    annotated_frame = label_annotator.annotate(
        annotated_frame,
        detections,
        labels
    )

    # Show output
    cv2.imshow("Tracking", annotated_frame)

    # Save output video
    out.write(annotated_frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()