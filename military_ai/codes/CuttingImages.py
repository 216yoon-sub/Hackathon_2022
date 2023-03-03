# Import modules and libraries
import os
from pathlib import Path
from PIL import Image

def ImgResizing(p, lt_imgs):
    lt_resize = []
    """for i in lt_imgs:
        img = Image.open(p + i)
        img_resize = img.resize((512,256))
        lt_resize.append(img_resize)"""
    img = Image.open(p+lt_imgs[0])
    img_resize = img.resize((512,256))
    lt_resize.append(img_resize)
    return lt_resize

def ImgCroppingAndSaving(img_names, rs, l_path, r_path):
    """left = rs[0].crop((0,0,256,256))
    right = rs[0].crop((256,0,512,256))
    left.save(l_path + img_names[0], 'png')
    right.save(r_path + img_names[0], 'png')"""
    for i in range(len(rs)):
        left = rs[i].crop((0,0,256,256))
        right = rs[i].crop((256,0,512,256))
        left.save(l_path + img_names[i], 'png')
        right.save(r_path + img_names[i], 'png')

def main():
    # Path
    train_x_path = Path("train\_x")
    train_y_path = Path("train\_y")
    test_x_path = Path("test\x")
    print(f'train_x_path: {train_x_path}') # for test
    print(f'train_y_path: {train_y_path}')

    # number of images
    lt_x = os.listdir(train_x_path)
    lt_y = os.listdir(train_y_path)
    lt_test_x = os.listdir(test_x_path)
    num_x = len(lt_x)
    num_y = len(lt_y)
    num_test_x = len(lt_test_x)
    print(f'num_x: {num_x}') # for test
    print(f'num_y: {num_y}')

    # check image
    """i = Image.open('D:/military_ai/train/_x/2015_DMG_1LB_000006.png')
    i.show()"""

    # Image Resizing
    resizing_x = ImgResizing(str(train_x_path) + "/", lt_x)
    resizing_y = ImgResizing(str(train_y_path) + "/", lt_y)
    resizing_test_x = ImgResizing(str(test_x_path) + "/", lt_test_x)
    
    # Image Cropping
    # x or y 폴더 속 이미지 이름 리스트, left 사진 저장 경로 + '/', right 사진 저장 경로 + '/'
    ImgCroppingAndSaving(lt_x, resizing_x, 'D:/military_ai/train/_x/x_left/', 'D:/military_ai/train/_x/x_right/')
    ImgCroppingAndSaving(lt_y, resizing_y, 'D:/military_ai/train/_y/y_left/', 'D:/military_ai/train/_y/y_right/')
    ImgCroppingAndSaving(lt_test_x, resizing_test_x, 'D:/military_ai/test/x/x_left', 'D:/military_ai/test/x/x_right')

main()