import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def predict_attributes(image_path):
    # Read image and convert to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade for face
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return "No face", "-", "-"

    for (x, y, w, h) in faces:
        # Estimate face area
        face_roi = img[y:y+h, x:x+w]

        # Dummy logic for gender (based on aspect ratio)
        gender = "Female" if h / w > 1.1 else "Male"

        # Dummy logic for hair length (based on pixels below the face)
        hair_region = img[y+h:y+h+int(h/2), x:x+w]
        hair_gray = cv2.cvtColor(hair_region, cv2.COLOR_BGR2GRAY)
        hair_density = np.mean(hair_gray < 50)  # dark pixel ratio

        hair = "Long" if hair_density > 0.25 else "Short"

        # Dummy logic for age
        age = 25 if gender == "Female" else 30

        return gender, age, hair

    return "Unknown", "-", "-"

def upload_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    gender, age, hair = predict_attributes(file_path)

    img = Image.open(file_path)
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    result_label.config(
        text=f"Predicted Gender: {gender}\nAge: {age}\nHair: {hair}"
    )

# GUI setup
root = tk.Tk()
root.title("Hair & Gender Detection")
root.geometry("400x500")

image_label = tk.Label(root)
image_label.pack()

result_label = tk.Label(root, text="Upload an image to detect", font=("Arial", 14))
result_label.pack(pady=10)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

root.mainloop()
