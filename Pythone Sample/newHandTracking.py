import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    # Draw the hand landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame_rgb.shape[1]), int(landmark.y * frame_rgb.shape[0])
                cv2.circle(frame_rgb, (x, y), 5, (0, 0, 255), -1)

    # Display the frame
    cv2.imshow("Hand Tracking", frame_rgb)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()
