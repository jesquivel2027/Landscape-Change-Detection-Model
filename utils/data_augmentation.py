import albumentations as A
from albumentations.augmentations.transforms import RandomBrightnessContrast
from PIL import Image
import numpy as np

def augment_image(image_path, save_path):
    image = np.array(Image.open(image_path))
    augment = A.Compose([
        A.HorizontalFlip(p=0.5),
        RandomBrightnessContrast(p=0.2),
        A.Rotate(limit=15, p=0.5)
    ])
    augmented = augment(image=image)
    Image.fromarray(augmented["image"]).save(save_path)