#Import libraries
import numpy as np
import cv2
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import os
import random
import shutil
import secrets

# ── CONFIG ────────────────────────────────────────────────────────────────────
INPUT_DIR      = "data/classification_folder"          # folder with original class subfolders
OUTPUT_DIR     = "data/augmented"    # folder where balanced dataset is saved
TARGET_COUNT   = 1500                # target number of images per class
IMG_SIZE       = 640                 # resize all images to this (640x640)
RANDOM_SEED    = 42                  # for reproducibility



# ── This function is to  elemenate blur images────────────────────────────────────────────────────────────────────

def detect_blur_batch(folder_path, threshold=100.0, limit=3500):
    # Supported image extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    # Get list of images and limit to first 1000
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]
    images = images[:limit]

    blurry_count = 0
    sharp_count = 0

    print(f"Processing {len(images)} images...")

    for filename in images:
        path = os.path.join(folder_path, filename)

        # Load image in grayscale for faster processing
        image = cv2.imread(path)
        if image is None:
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        score = cv2.Laplacian(gray, cv2.CV_64F).var()

        if score < threshold:
            print(f"[BLURRY] {filename} - Score: {score:.2f}")
            blurry_count += 1
            os.remove(path)
        else:
            sharp_count += 1

    print("\n--- Summary ---")
    print(f"Total Processed: {len(images)}")
    print(f"Sharp Images: {sharp_count}")
    print(f"Blurry Images: {blurry_count}")


# Replace with your actual folder path
for subfolder in range(16):
 folder = f"{INPUT_DIR}/{subfolder}"
 detect_blur_batch(folder)


# ── This function is to move images into distination folder for training────────────────────────────────────────────────────────────────────

def move_files(list_data, i, source_folder):
    # 1. Create destination folder if it doesn't exist
    destination_folder = f"{OUTPUT_DIR}/{i}"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    # 2. Loop through the list and move each file
    for filename in list_data:
        old_path = os.path.join(source_folder, filename)
        new_path = os.path.join(destination_folder, filename)

        # CHECK: If the file already exists in the destination, skip it
        if os.path.exists(new_path):
            print(f"Skipping: {filename} (already exists in destination)")
            continue

        try:
            shutil.move(old_path, new_path) # Changed from os.rename to shutil.move
        except FileNotFoundError:
            print(f"Skipping: {filename} (not found in source)")

# ── This function is to perform rotation of images────────────────────────────────────────────────────────────────────

def rotation_rezise(folder_path,img_group):

   # Loop through list
   for g_a in img_group:
     #build the full path to the original file
     src=os.path.join(folder_path,g_a)

     #Check if thee original file exist
     if os.path.exists(src):
        #It will split name (cat.jpg into cat and .jpg)
        name, ext=os.path.splitext(g_a)

        # To generte uni name
        unique=secrets.token_urlsafe(3)

        #Define the new name for the copy
        new_name=f"{name}{unique}{ext}"
        dst=os.path.join(folder_path,new_name)


        #Copy the file to the same folder with the new name
        shutil.copy(src,dst)

        # Single random integer between 10 and 50 (50 is excluded)
        rng = np.random.default_rng()
        valx = rng.integers(low=130, high=300)
        valy = rng.integers(low=130, high=300)

        im=cv2.imread(dst)
        if im is not None:
            sim=cv2.resize(im,(valx,valy))
            rim=cv2.rotate(sim,cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(dst,rim)
        else:
            print(f"Warning: Could not read image {dst} for augmentation")

     else:
      print(f"File {g_a} does not exist for augmentation")

# ── This function is to add images if a class has less than 1500 images────────────────────────────────────────────────────────────────────

def dataaugmentation(folder_path,img_required):

    # 1. Define valid image extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    # 2. Get a list of all image files in the directory
    all_images = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]

    if not all_images:
        print(f"No images found in {folder_path} for augmentation.")
        return

    # 3. Ensure we don't try to sample more than what's available
    actual_sample_size = min(len(all_images), img_required)

    # 4. Pick random files (without duplicates)
    if actual_sample_size > 0:
        random_selection = random.sample(all_images, actual_sample_size)
        rotation_rezise(folder_path,random_selection)
    else:
        print(f"No images required for augmentation in {folder_path}.")


# ── This function is to  select random 1500 images────────────────────────────────────────────────────────────────────

def img_random_selector(folder_path,numsample):
    # 1. Define valid image extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    # 2. Get a list of all image files in the directory
    all_images = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]

    if not all_images:
        return "No images found in the specified folder."

    # 3. Ensure we don't try to sample more than what's available
    actual_sample_size = min(len(all_images), numsample)

    # 4. Pick random files (without duplicates)
    random_selection = random.sample(all_images, actual_sample_size)

    return random_selection


# ── This function is to check folder and ditribute equal images in every folder────────────────────────────────────────────────────────────────────

def Findfoldersize(folder_path):

  imgg=glob(f'{folder_path}/*.png')
  high_count = 1
  low_count = 0
  Total_samples=1500
  img_count=len(imgg)

  img_required=Total_samples-img_count if Total_samples > img_count else img_count-Total_samples
  if img_count>=1500:
    return high_count, img_required
  else:
    return low_count, img_required


for i in range(16):
 folder_path = f"../content/drive/MyDrive/classification/{i}"
 if not os.path.exists(folder_path):
    print(f"Folder not found: {folder_path}. Skipping.")
    continue

 hilow,img_required=Findfoldersize(folder_path)

 if hilow==1 :
    # train_d,test_d=img_random_selector(folder_path,numsample=1500,percentage=0.8)
    random_nu=img_random_selector(folder_path,numsample=1500)
    move_files(random_nu,i,folder_path)

 elif hilow==0:
    print(f"Performing data augmentation for folder {i}. Images required: {img_required}")
    dataaugmentation(folder_path,img_required)
    # After augmentation, re-select images (now there might be more)
    random_nu=img_random_selector(folder_path,numsample=1500)
    move_files(random_nu,i,folder_path)