from pathlib import Path
import xml.etree.ElementTree as ET

# User input
xml_dir = r'C:\Users\Admin\Desktop\TTJ Annotations\cam9\annotations'

xml_names = sorted(list(Path.iterdir(Path(xml_dir))))

bbox_labels_count = {}

for xmlname in xml_names:
    tree = ET.parse(xmlname)
    root = tree.getroot()

    objects = root.findall('object')

    for node in objects:
        label_node = node.find('name')
        if label_node.text not in bbox_labels_count.keys():
            bbox_labels_count[label_node.text] = 1
        else:
            bbox_labels_count[label_node.text] += 1

print("number of classes:", len(bbox_labels_count))
print("total bbox instances:", sum(bbox_labels_count.values()))
print("bbox instances by class:", bbox_labels_count)