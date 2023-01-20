import cv2

# User-defined inputs
input_video_file = r'C:\Users\Admin\Desktop\model_iou\test.mp4'
output_save_file = r'C:\Users\Admin\Desktop\model_iou\test_new.mp4'
final_video_fps = 20

# Open the input video file
cap = cv2.VideoCapture(input_video_file)

# Get the video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_save_file, fourcc, fps, (frame_width, frame_height))

# Compress the video into the desired number of frames
compression_factor = int(frame_count / final_video_fps)
i = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if i % compression_factor == 0:
        out.write(frame)
    i += 1

# Release the file
cap.release()
out.release()