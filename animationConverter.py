import cv2

def apply_cartoon_effect(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply bilateral filter for cartoon-like effect
    blurred = cv2.bilateralFilter(gray, 9, 75, 75)
    
    # Apply edge detection
    edges = cv2.Canny(blurred, 30, 150)
    
    # Convert edges to color
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    # Combine original frame with the edges
    cartoon_frame = cv2.bitwise_and(frame, edges_color)
    
    return cartoon_frame

# Open the video
video_path = "imranKhan.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_animation.avi', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply cartoon effect to the frame
    cartoon_frame = apply_cartoon_effect(frame)
    
    # Write the cartoon frame to the output video
    output_video.write(cartoon_frame)
    
    cv2.imshow('Animation Effect', cartoon_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
output_video.release()
cv2.destroyAllWindows()
