import os
from shutil import copy2

def split_dataset(source_dir, train_dir, val_dir, split_ratio=0.8):
    files = os.listdir(source_dir)
    train_size = int(len(files) * split_ratio)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    for i, file in enumerate(files):
        dest_dir = train_dir if i < train_size else val_dir
        copy2(os.path.join(source_dir, file), os.path.join(dest_dir, file))