# 06_roi_safety_zone.py

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
PL = mp_holistic.PoseLandmark

# Define a fixed "danger zone" rectangle on screen (e.g., where a moving part exists)
# Tune these coordinates for your camera framing
ZONE = (350, 150, 250, 200)  # x, y, w, h

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as h:
    while True:
        ok, frame = cap.read()
        if not ok: break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = h.process(rgb)

        # Draw the safety region of interest
        x,y,w,h = ZONE
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,165,255), 2)  # orange box

        alert = False
        if res.pose_landmarks:
            lm = res.pose_landmarks.landmark
            # use wrist & hand points as proxies for "hand region"
            image_h, image_w, _ = frame.shape
            hand_points = [
                lm[PL.LEFT_WRIST], lm[PL.RIGHT_WRIST]
            ]
            for p in hand_points:
                px, py = int(p.x * image_w), int(p.y * image_h)
                cv2.circle(frame, (px, py), 6, (255,0,0), -1)
                if x <= px <= x+w and y <= py <= y+h:
                    alert = True

        if alert:
            cv2.putText(frame, "WARNING: HAND IN DANGER ZONE!", (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, cv2.LINE_AA)

        mp_drawing.draw_landmarks(frame, res.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        cv2.imshow("ROI Safety Zone — press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
