from PIL import Image
from utils import dynamic_quality
import os
def compress(filename,originpath,targetpath):
    name = filename.rstrip('.png').rstrip('.jpg')
    im = Image.open(originpath+filename)
    im = im.convert('RGB')
    im.format = "JPEG"
    new_photo = im.copy()
    new_photo.thumbnail(im.size,resample=Image.ANTIALIAS)
    save_args = {'format':im.format}
    save_args['quality'],value= dynamic_quality.jpeg_dynamic_quality(im)
    save_args['optimize']=True
    save_args['progressive=True']=True

    new_photo.save(targetpath+name+".jpg",**save_args)

if __name__ == '__main__':
    '''
    在originpath和targetpath中填写源文件夹与目标文件夹
    '''
    originpath = "D:/1/"
    targetpath = "D:/2/"
    for root, dirs, files in os.walk(originpath):
        for file in files:
            compress(file,originpath,targetpath)
