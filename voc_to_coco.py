import os
import json
import xml.etree.ElementTree as ET

xml_dir = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\renamed_annotations'
json_file = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\ann_renamed.json'

def voc2coco(xml_dir, json_file):
    categories = {}
    coco_output = {
        "images": [],
        "categories": [],
        "annotations": []
    }

    image_id = 1
    annotation_id = 1

    for xml_file in os.listdir(xml_dir):
        tree = ET.parse(os.path.join(xml_dir, xml_file))
        root = tree.getroot()

        # extract image information
        image = {}
        image['file_name'] = root.find('filename').text
        image['height'] = int(root.find('size')[1].text)
        image['width'] = int(root.find('size')[0].text)
        image['id'] = image_id
        coco_output["images"].append(image)

        # extract annotations
        for obj in root.iter('object'):
            category = obj.find('name').text
            if category not in categories:
                new_id = len(categories)
                categories[category] = new_id
            category_id = categories[category]

            xmin = int(obj.find('bndbox').find('xmin').text)
            ymin = int(obj.find('bndbox').find('ymin').text)
            xmax = int(obj.find('bndbox').find('xmax').text)
            ymax = int(obj.find('bndbox').find('ymax').text)
            width = xmax - xmin
            height = ymax - ymin

            annotation = {}
            annotation['id'] = annotation_id
            annotation['image_id'] = image_id
            annotation['category_id'] = category_id
            annotation['bbox'] = [xmin, ymin, width, height]
            annotation['area'] = width * height
            annotation['iscrowd'] = 0

            coco_output["annotations"].append(annotation)
            annotation_id += 1

        image_id += 1
        
    for category, id in categories.items():
        coco_output["categories"].append({"id": id, "name": category})
        
    with open(json_file, 'w') as output_json_file:
        json.dump(coco_output, output_json_file)

voc2coco(xml_dir, json_file)