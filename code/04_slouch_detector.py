# 04_slouch_detector.py
import cv2, numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
PL = mp_holistic.PoseLandmark

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def put_text(img, text, pos=(20,40), color=(0,0,255)):
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as h:
    while True:
        ok, frame = cap.read()
        if not ok: break
        rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        res = h.process(rgb)
        frame = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        if res.pose_landmarks:
            lm = res.pose_landmarks.landmark
            nose_y = lm[PL.NOSE].y
            l_sh_y = lm[PL.LEFT_SHOULDER].y
            r_sh_y = lm[PL.RIGHT_SHOULDER].y
            sh_avg = (l_sh_y + r_sh_y)/2.0

            # larger y means lower on screen; tune threshold
            threshold = 0.07
            if nose_y > sh_avg + threshold:
                put_text(frame, "SLOUCHING!", (20,50), (0,0,255))
            else:
                put_text(frame, "GOOD POSTURE", (20,50), (0,200,0))

        mp_drawing.draw_landmarks(frame, res.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        cv2.imshow("Slouch Detector — press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
