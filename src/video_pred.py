import cv2
from ultralytics import YOLO

# Define paths
model_path = '# Path to the model file'
video_input_path = '# Path to the input video file'
video_output_path = '# Path to the output video file'

# Load the model
model = YOLO(model_path)

# Open the input video
cap = cv2.VideoCapture(video_input_path)

# Check if the video file opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {video_input_path}")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Check if the fps is available
if fps == 0:
    print("Warning: FPS value is 0. Setting FPS to 30 as default.")
    fps = 30

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_output_path, fourcc, fps, (frame_width, frame_height))

frame_count = 0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (YOLO models expect RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform object detection
    results = model(rgb_frame)

    # Draw the results on the original frame
    annotated_frame = results[0].plot()

    # Write the annotated frame to the output video
    out.write(cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR))

    frame_count += 1
    print(f'Processing frame {frame_count}/{total_frames}')

# Release the video objects
cap.release()
out.release()

print('Video processing complete. Output saved to', video_output_path)
