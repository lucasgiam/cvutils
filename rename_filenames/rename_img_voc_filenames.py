import os
import xml.etree.ElementTree as ET

image_dir = r'C:\Users\Admin\Desktop\cam8\images'
annotation_dir = r'C:\Users\Admin\Desktop\cam8\annotations'
prefix = "image"
start_num = 1

def rename_images_and_annotations(image_dir, annotation_dir, prefix, start_num):
    image_files = os.listdir(image_dir)
    annotation_files = os.listdir(annotation_dir)
    digits = 5
    # digits = len(str(len(image_files)+start_num-1))
    for i, file in enumerate(image_files):
        ext = os.path.splitext(file)[1]
        new_image_name = f"{prefix}{str(i+start_num).zfill(digits)}{ext}"
        old_image_path = os.path.join(image_dir, file)
        new_image_path = os.path.join(image_dir, new_image_name)
        os.rename(old_image_path, new_image_path)
        old_annotation_name = file.split(".")[0] + ".xml"
        if old_annotation_name in annotation_files:
            new_annotation_name = f"{prefix}{str(i+start_num).zfill(digits)}.xml"
            old_annotation_path = os.path.join(annotation_dir, old_annotation_name)
            new_annotation_path = os.path.join(annotation_dir, new_annotation_name)
            os.rename(old_annotation_path, new_annotation_path)
            tree = ET.parse(new_annotation_path)
            root = tree.getroot()
            for elem in root.iter('filename'):
                elem.text = new_image_name
            tree.write(new_annotation_path)

rename_images_and_annotations(image_dir, annotation_dir, prefix, start_num)