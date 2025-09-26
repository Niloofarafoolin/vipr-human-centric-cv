# 03_mediapipe_file_mode.py

import argparse, cv2, os, glob
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def annotate_image(path, out_dir):
    img = cv2.imread(path)
    if img is None: 
        print(f"Skip (cannot read): {path}")
        return
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    with mp_holistic.Holistic(static_image_mode=True) as h:
        res = h.process(rgb)
    img = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(img, res.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
    mp_drawing.draw_landmarks(img, res.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(img, res.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(img, res.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, os.path.basename(path).rsplit(".",1)[0] + "_annotated.jpg")
    cv2.imwrite(out_path, img)
    print("Saved:", out_path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image_dir", type=str, default="sample_data/images")
    ap.add_argument("--save", action="store_true")
    args = ap.parse_args()

    images = sorted(glob.glob(os.path.join(args.image_dir, "*.*")))
    if not images:
        print("No images found. Drop JPG/PNG files into:", args.image_dir)
        return

    out_dir = os.path.join(args.image_dir, "out")
    for p in images:
        annotate_image(p, out_dir if args.save else args.image_dir)

if __name__ == "__main__":
    main()
