import os
import json
from collections import Counter

ann_file = r'C:\Users\s43482\Desktop\tfrecord2voc conversion\ann.json'

def cat_count(annotations=None):
    cats = []
    for i in annotations['annotations']:
        j = i['category_id']
        for cat in annotations['categories']:
            if j == cat['id']:
                cats.append(cat['name'])
    count_dict = dict(Counter(cats))
    num_classes = len(count_dict)
    print("number of classes:", num_classes)
    print("total bbox instances", sum(count_dict.values()))
    print("bbox instances by class:", count_dict)

def main():
    with open(os.path.join(ann_file), 'rt', encoding='UTF-8') as annotations:
        ann = json.load(annotations)
    cat_count(ann)

if __name__ == "__main__":
    main()