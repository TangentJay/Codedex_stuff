# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:06:14 2024

@author: TANGENT J
"""

from google.cloud import vision_v1
from google.cloud.vision_v1 import types

# Set the path to your JSON credentials fil
json_credentials_path = "C:/Users/TANGENT J/Downloads/stalwart-motif-416421-9ef2724005ae.json"

client = vision_v1.ImageAnnotatorClient.from_service_account_file(json_credentials_path)


image_path = 'C:/Users/TANGENT J/Downloads/2 ran.jpg'


with open(image_path, 'rb') as image_file:
    content = image_file.read()


image = types.Image(content=content)


response = client.label_detection(image=image)
labels = response.label_annotations

# Print detected labels
print('Labels:')
for label in labels:
    print(label.description)
