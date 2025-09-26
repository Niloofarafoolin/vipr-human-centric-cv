# 05_hand_above_head.py
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
PL = mp_holistic.PoseLandmark

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as h:
    while True:
        ok, frame = cap.read()
        if not ok: break
        rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        res = h.process(rgb)
        frame = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        msg = "Raise a hand above your head"
        color = (0,200,0)

        if res.pose_landmarks:
            lm = res.pose_landmarks.landmark
            head_y = lm[PL.NOSE].y  # proxy for head level

            # use wrist landmarks
            l_wrist_y = lm[PL.LEFT_WRIST].y
            r_wrist_y = lm[PL.RIGHT_WRIST].y

            if l_wrist_y < head_y or r_wrist_y < head_y:
                msg = "HAND ABOVE HEAD!"
                color = (0,0,255)

        cv2.putText(frame, msg, (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
        mp_drawing.draw_landmarks(frame, res.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        cv2.imshow("Hand Above Head — press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
