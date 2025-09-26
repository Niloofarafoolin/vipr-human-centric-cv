# TROUBLESHOOTING

## Common issues & fixes

### 1) `ModuleNotFoundError` (mediapipe, cv2, numpy)
- You’re likely not in the right Conda env. Run `conda activate vipr-cv` then reinstall:
  ```bash
  pip install -r requirements.txt
  ```

### 2) Camera not opening (`VideoCapture(0)` returns False)
- Close Teams/Zoom/OBS — they may be holding the camera.
- **macOS**: System Settings → Privacy & Security → Camera → allow Terminal/VS Code.
- **Windows**: Settings → Privacy → Camera → allow desktop apps.

### 3) OpenCV window doesn’t show / blank window
- Try:
  - `conda install -c conda-forge opencv`
  - or run from a standard terminal (not inside notebook); avoid WSL for camera tests.

### 4) Mediapipe import errors on macOS (Apple Silicon)
- Ensure Python 3.10 or 3.11. Then:
  ```bash
  pip install mediapipe==0.10.8
  ```
- If you see protobuf version conflicts:
  ```bash
  pip install "protobuf<4.0.0"
  ```

### 5) Performance too slow
- Lower webcam resolution in the code (e.g., 640×480).
- Increase `min_detection_confidence` to reduce re-detections.
- Close browser tabs / heavy apps.

### 6) No webcam / lab desktop only
- Use **file mode** scripts with provided images/videos:
  ```bash
  python code/03_mediapipe_file_mode.py --image_dir sample_data/images --save
  ```

### 7) OpenPose on Windows
- Install Visual Studio 2022 Desktop C++ workload.
- Download OpenPose release zip and models; run the `OpenPoseDemo.exe` examples.
- If models not found, copy the `models/` folder into the main OpenPose directory.

### 8) `cv2.imshow` crashes on macOS with Metal/AVFoundation
- Use a conda‑forge OpenCV build: `conda install -c conda-forge opencv`
- Or switch to Jupyter and render frames inline (slower).

---
If stuck, take a photo/screenshot of the error and post it in Teams; include your OS, Python, and command you ran.
