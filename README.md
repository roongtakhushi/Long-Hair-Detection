# Long Hair Detection GUI

This project uses OpenCV's DNN module with a pre-trained `.caffemodel` to detect long hair in images.

## Project Structure
```
.
├── long_hair_gui.py
├── deploy.prototxt
├── long_hair.caffemodel
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository or download the files.
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the GUI application:
```bash
python long_hair_gui.py
```

Upload an image and the model will predict if the person has long hair.

## Requirements
- Python 3.x
- OpenCV (cv2)
- Tkinter

## Notes
- Ensure that `deploy.prototxt` and `.caffemodel` are in the same folder as `long_hair_gui.py`.
- You can replace the `.caffemodel` with any compatible one trained for hair length detection.

