import os

# User inputs
img_dir = r'C:\Users\Admin\Desktop\TTJ Annotations\cam8_images97-500\raw_DELETE'
ann_dir = r'C:\Users\Admin\Desktop\TTJ Annotations\cam8_images97-500\ann'

# List all files in img_dir and ann_dir
img_files = os.listdir(img_dir)
ann_files = os.listdir(ann_dir)

# Create a set of filenames of annotation files without the file extension
ann_filenames = set(os.path.splitext(filename)[0] for filename in ann_files)

# Iterate through image files, delete if corresponding annotation file doesn't exist
deleted_count = 0
for img_filename in img_files:
    img_basename = os.path.splitext(img_filename)[0]
    if img_basename not in ann_filenames:
        os.remove(os.path.join(img_dir, img_filename))
        deleted_count += 1

print(f"Deleted {deleted_count} images that do not contain any annotations.")