import os

image_dir = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\images_renamed'
prefix = "image"
start_num = 1

def rename_images(image_dir, prefix, start_num):
    files = os.listdir(image_dir)
    digits = 5
    # digits = len(str(len(files)+start_num-1))
    for i, file in enumerate(files):
        ext = os.path.splitext(file)[1]
        new_name = f"{prefix}{str(i+start_num).zfill(digits)}{ext}"
        old_path = os.path.join(image_dir, file)
        new_path = os.path.join(image_dir, new_name)
        os.rename(old_path, new_path)

rename_images(image_dir, prefix, start_num)