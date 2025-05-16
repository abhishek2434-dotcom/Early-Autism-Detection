import cv2
import mediapipe as mp
from utils.eye_tracker import detect_eye_contact
from utils.behavior_analysis import detect_repetitive_behavior, assess_social_reciprocity

cap = cv2.VideoCapture(0)  # or 'sample_videos/toddler_example.mp4'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = detect_eye_contact(frame)
    frame = detect_repetitive_behavior(frame)
    frame = assess_social_reciprocity(frame)

    cv2.imshow("Autism Detection", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
