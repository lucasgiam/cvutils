import json
import os
import xml.etree.ElementTree as ET

json_file = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\ann.json'
xml_dir = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\xml_ann_2'

def coco2voc(json_file, xml_dir):
    with open(json_file) as f:
        data = json.load(f)
    images = data["images"]
    annotations = data["annotations"]
    categories = data["categories"]

    if not os.path.exists(xml_dir):
        os.makedirs(xml_dir)

    # create xml files for each image
    for image in images:
        image_id = image["id"]
        file_name = image["file_name"]
        width = image["width"]
        height = image["height"]

        root = ET.Element("annotation")

        ET.SubElement(root, "folder").text = "coco_folder"
        ET.SubElement(root, "filename").text = file_name
        ET.SubElement(root, "path").text = file_name

        source = ET.SubElement(root, "source")
        ET.SubElement(source, "database").text = "coco_database"

        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(width)
        ET.SubElement(size, "height").text = str(height)
        ET.SubElement(size, "depth").text = "3"

        ET.SubElement(root, "segmented").text = "0"

        # add object elements for each annotation
        for annotation in annotations:
            if annotation["image_id"] != image_id:
                continue

            obj = ET.SubElement(root, "object")
            ET.SubElement(obj, "name").text = categories[annotation["category_id"]]["name"]
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = "0"
            ET.SubElement(obj, "difficult").text = "0"

            bbox = annotation["bbox"]
            xmin, ymin, w, h = bbox
            xmax = xmin + w
            ymax = ymin + h

            bndbox = ET.SubElement(obj, "bndbox")
            ET.SubElement(bndbox, "xmin").text = str(xmin)
            ET.SubElement(bndbox, "ymin").text = str(ymin)
            ET.SubElement(bndbox, "xmax").text = str(xmax)
            ET.SubElement(bndbox, "ymax").text = str(ymax)

        # write xml file
        xml_str = ET.tostring(root, encoding="unicode")
        xml_str = xml_str.replace("\n", "\n    ")
        with open(f"{xml_dir}/{file_name.split('.')[0]}.xml", "w") as f:
            f.write(xml_str)

coco2voc(json_file, xml_dir)