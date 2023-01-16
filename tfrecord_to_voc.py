import os
import csv
import xml.etree.ElementTree as ET
from collections import defaultdict

tfrecord_path = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\tensorflow_style_df.csv'
xml_save_dir = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\xml_ann'

def parse_csv(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = defaultdict(list)
        for row in csv_reader:
            if line_count == 0:
                headers = row
            else:
                data[row[0]].append(row[1:])
            line_count += 1
    return dict(data)

def create_voc_xml(height, width, filename, bboxes, classes, xml_dir):
    # Create the root element
    annotation = ET.Element("annotation")

    # Add the folder element
    folder = ET.SubElement(annotation, "folder")
    folder.text = "images"

    # Add the filename element
    filename_element = ET.SubElement(annotation, "filename")
    filename_element.text = filename

    # Add the size element
    size = ET.SubElement(annotation, "size")
    width_element = ET.SubElement(size, "width")
    width_element.text = str(width)
    height_element = ET.SubElement(size, "height")
    height_element.text = str(height)
    depth_element = ET.SubElement(size, "depth")
    depth_element.text = "3"

    # Add the object elements
    for i in range(len(bboxes)):
        object = ET.SubElement(annotation, "object")
        name = ET.SubElement(object, "name")
        name.text = classes[i]
        bndbox = ET.SubElement(object, "bndbox")
        xmin_element = ET.SubElement(bndbox, "xmin")
        xmin_element.text = str(bboxes[i][0])
        ymin_element = ET.SubElement(bndbox, "ymin")
        ymin_element.text = str(bboxes[i][1])
        xmax_element = ET.SubElement(bndbox, "xmax")
        xmax_element.text = str(bboxes[i][2])
        ymax_element = ET.SubElement(bndbox, "ymax")
        ymax_element.text = str(bboxes[i][3])

    # Create the XML tree
    tree = ET.ElementTree(annotation)

    # Save the XML file
    tree.write(os.path.join(xml_dir, (filename.split(".")[0] + ".xml")))

annotations = parse_csv(tfrecord_path)

for filename, rows in annotations.items():
    width = rows[0][0]
    height = rows[0][1]
    bboxes = []
    classes = []
    for row in rows:
        bboxes.append([row[3],row[4],row[5],row[6]])
        classes.append(row[2])
    create_voc_xml(height, width, filename, bboxes, classes, xml_save_dir)