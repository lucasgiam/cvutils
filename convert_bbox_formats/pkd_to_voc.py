import os
import re
import ast
import cv2
import numpy as np
import pandas as pd
import xml.etree.cElementTree as ET
from xml.dom import minidom

csv_file = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\all_annotations.csv'
img_dir =  r'C:\Users\s43482\Desktop\tfrecord2voc conversion\images'
xml_dir = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\xml_generated'

def pkd2voc(csv_file, img_dir, xml_dir):
    df = pd.read_csv(csv_file)
    for row_index, row_tuple in enumerate(df.itertuples()):
        # Preprocess bboxes and labels
        labels_str = row_tuple.bbox_labels
        labels_str = labels_str.replace("\n", "")
        labels_str = re.sub("\s+", ",", labels_str)
        labels = ast.literal_eval(labels_str)
        bboxes_str = row_tuple.bboxes
        bboxes_str = bboxes_str.replace("\n", "")
        bboxes_str = re.sub("\s+", ",", bboxes_str)
        bboxes = np.array(ast.literal_eval(bboxes_str))
        bboxes = bboxes.astype(float).tolist()

        # Get image height and width
        img_path = os.path.join(img_dir, row_tuple.filename)
        img = cv2.imread(img_path)
        height, width, _ = img.shape
        
        # Denormalize bbox coordinates
        bboxes = [[int(bbox[0] * width), int(bbox[1] * height), int(bbox[2] * width), int(bbox[3] * height)] for bbox in bboxes]

        # Create XML root element
        annotation = ET.Element("annotation")

        # Add filename and path elements
        ET.SubElement(annotation, "filename").text = row_tuple.filename
        ET.SubElement(annotation, "path").text = img_path

        # Add size elements
        size = ET.SubElement(annotation, "size")
        ET.SubElement(size, "width").text = str(width)
        ET.SubElement(size, "height").text = str(height)
        ET.SubElement(size, "depth").text = "3"

        # Add object elements for each bbox and label
        for bbox, label in zip(bboxes, labels):
            obj = ET.SubElement(annotation, "object")
            ET.SubElement(obj, "name").text = label
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = "0"
            ET.SubElement(obj, "difficult").text = "0"
            bndbox = ET.SubElement(obj, "bndbox")
            ET.SubElement(bndbox, "xmin").text = str(bbox[0])
            ET.SubElement(bndbox, "ymin").text = str(bbox[1])
            ET.SubElement(bndbox, "xmax").text = str(bbox[2])
            ET.SubElement(bndbox, "ymax").text = str(bbox[3])

            
            # Create the XML file
            xml_str = ET.tostring(annotation)
            xml_str = minidom.parseString(xml_str).toprettyxml(indent=' '*4)
            xml_path = os.path.join(xml_dir, row_tuple.filename.replace('jpg', 'xml'))
            with open(xml_path, 'w') as f:
                f.write(xml_str)

if __name__ == '__main__':
    pkd2voc(csv_file, img_dir, xml_dir)