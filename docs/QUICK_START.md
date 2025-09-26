# QUICK START (Windows/macOS)

## 0) Install Conda
- Windows: install Miniconda or Anaconda
- macOS: install Miniconda (Apple Silicon supported)

## 1) New environment
```bash
conda create -n vipr-cv python=3.10 -y
conda activate vipr-cv
```

## 2) Install Python deps
```bash
pip install -r requirements.txt
```
> On macOS, if GUI windows don't show, try: `conda install -c conda-forge opencv`

## 3) Camera test
```bash
python code/01_test_opencv_camera.py
```

## 4) Live holistic model
```bash
python code/02_mediapipe_holistic_live.py
```
Press **q** to quit any OpenCV window.
