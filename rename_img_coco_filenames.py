import os
import json

image_dir = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\renamed_images'
annotation_file = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\renamed_annotations\ann_renamed.json'
prefix = "image"
start_num = 1

def rename_images_and_annotations(image_dir, annotation_file, prefix, start_num):
    image_files = os.listdir(image_dir)
    with open(annotation_file) as f:
        data = json.load(f)
    annotations = data["annotations"]
    images = data["images"]
    digits = 5
    # digits = len(str(len(image_files)+start_num-1))
    for i, file in enumerate(image_files):
        ext = os.path.splitext(file)[1]
        new_image_name = f"{prefix}{str(i+start_num).zfill(digits)}{ext}"
        old_image_path = os.path.join(image_dir, file)
        new_image_path = os.path.join(image_dir, new_image_name)
        os.rename(old_image_path, new_image_path)
        for image in images:
            if image["file_name"] == file:
                image["file_name"] = new_image_name
                for annotation in annotations:
                    if annotation["image_id"] == image["id"]:
                        annotation["file_name"] = new_image_name
                        break
    with open(annotation_file, "w") as f:
        json.dump(data, f)

rename_images_and_annotations(image_dir, annotation_file, prefix, start_num)