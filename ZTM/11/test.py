# Excercise JPG to PNG converter: Another Example
from PIL import Image
import sys
import os
img_path=sys.argv[0]
new_path=sys.argv[1]
print(img_path,new_path)
if not os.path.exists(new_path):
    os.makedirs(new_path)
for filename in os.listdir(img_path):
    img=Image.open(f'{img_path}{filename}')
    new_file=os.path.split(filename)[0]
    img.save(f'{new_path}{new_file}.png','png')
    print('All done')
