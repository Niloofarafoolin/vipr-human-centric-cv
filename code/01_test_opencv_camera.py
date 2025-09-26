# 01_test_opencv_camera.py
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Could not open camera. Is it in use by Teams/Zoom? Permissions granted?")
    raise SystemExit(1)

# Try to lower resolution for performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ok, frame = cap.read()
    if not ok:
        print("Frame grab failed — check webcam / permissions.")
        break
    cv2.imshow("Camera Test — press q to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
