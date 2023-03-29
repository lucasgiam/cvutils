import os
import xml.etree.ElementTree as ET

# User inputs
xml_dir = r'C:\Users\Admin\Desktop\TTJ Annotations\cam9\annotations'
conv_dict = {'car': 'vehicle', 'truck': 'vehicle', 'bus': 'vehicle'}
# Note that conv_dict is a dictionary whose keys are the CURRENT class labels and values are the NEW class labels

# Loop through all XML files in the directory
for filename in os.listdir(xml_dir):
    if filename.endswith('.xml'):
        filepath = os.path.join(xml_dir, filename)
        
        # Parse the XML file
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # Loop through all objects in the XML file
        for obj in root.findall('object'):
            # Get the current class label
            curr_label = obj.find('name').text
            
            # Check if the current class label is in the conversion dictionary
            if curr_label in conv_dict:
                # If it is, change the class label to the new label
                new_label = conv_dict[curr_label]
                obj.find('name').text = new_label
        
        # Save the modified XML file
        tree.write(filepath)