# 02_mediapipe_holistic_live.py
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Could not open camera. Close Teams/Zoom, check permissions.")
    raise SystemExit(1)

# Optional: constrain resolution for speed
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        # flip for mirror view and convert BGR->RGB
        frame_rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        results = holistic.process(frame_rgb)

        # back to BGR for display
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        # draw face mesh
        mp_drawing.draw_landmarks(
            frame, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)

        # draw pose
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # draw hands
        mp_drawing.draw_landmarks(
            frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        cv2.imshow("Holistic (face+hands+pose) — press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
