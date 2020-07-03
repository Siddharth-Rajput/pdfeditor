from PIL import Image
import os
os.chdir("B:\pdf editor\\1rot")
length = len(os.listdir())
for i in range (1,201):
    image_file = str(i)+".jpg"
    im = Image.open(image_file)
    if i%2==1:
        im_crop = im.crop((0,155,1659,1259))
        im_crop.save(image_file)
    else:
        im_crop = im.crop((0,0,1659,1104))
        im_crop.save(image_file)