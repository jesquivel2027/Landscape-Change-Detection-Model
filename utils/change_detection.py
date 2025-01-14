import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_changes(image1_path, image2_path):
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(img1, img2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    return thresh

def visualize_changes(before_path, after_path, diff):
    before = cv2.imread(before_path)
    after = cv2.imread(after_path)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.title("Before")
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 3, 2)
    plt.title("After")
    plt.imshow(cv2.cvtColor(after, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 3, 3)
    plt.title("Change Detection")
    plt.imshow(diff, cmap="gray")
    plt.show()