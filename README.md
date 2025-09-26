# Human‑Centric Computer Vision — VIPR (Innovation Factory, UGA)

This starter kit gets VIPR students from zero → a **live face + hands + posture tracker** on their own laptop in under an hour, plus two tiny ergonomics/safety mini‑projects.

> Works best with a fresh Conda env. Supports Windows 11, macOS (Intel & Apple Silicon).

## Repository map

```
if-vipr-human-centric-cv/
├─ code/
│  ├─ 00_check_python_env.py
│  ├─ 01_test_opencv_camera.py
│  ├─ 02_mediapipe_holistic_live.py
│  ├─ 03_mediapipe_file_mode.py
│  ├─ 04_slouch_detector.py
│  ├─ 05_hand_above_head.py
│  └─ 06_roi_safety_zone.py
├─ sample_data/
│  ├─ images/  # drop a few JPG/PNG head+hands photos here
│  └─ videos/  # drop a short MP4 of a person standing/sitting
├─ docs/
│  ├─ TROUBLESHOOTING.md
│  ├─ QUICK_START.md
│  └─ LICENSE
├─ requirements.txt
├─ environment.yml
└─ README.md
```

## Quick start (Conda)

```bash
# 1) Create env
conda create -n vipr-cv python=3.10 -y
conda activate vipr-cv

# 2) Install core deps
pip install -r requirements.txt

# 3) Sanity check camera
python code/01_test_opencv_camera.py       # press q to quit

# 4) Live multi‑signal tracker (face + hands + pose)
python code/02_mediapipe_holistic_live.py  # press q to quit
```

## Mini‑projects (choose one to finish this week)

- **Ergonomics — Slouch Detector** (`code/04_slouch_detector.py`)
- **Gesture — Hand Above Head** (`code/05_hand_above_head.py`)
- **Safety — ROI Danger Zone** (`code/06_roi_safety_zone.py`)

## OpenPose fallback (Windows)

If you need a heavier model or MediaPipe fails, use the prebuilt OpenPose demo:

1. Install **Visual Studio 2022** (Desktop C++ workload).
2. Download OpenPose release and **models/** (see `docs/TROUBLESHOOTING.md`).
3. From the `openpose/` folder:
   ```bat
   .\bin\OpenPoseDemo.exe --camera 0 --display 1 --hand --face
   .\bin\OpenPoseDemo.exe --image_dir path\to\images --write_images out\
   ```

---

© University of Georgia — Innovation Factory (VIPR). For teaching purposes.
