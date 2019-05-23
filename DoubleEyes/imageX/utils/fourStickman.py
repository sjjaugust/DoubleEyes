# coding:utf-8

from ctypes import *
from django.conf import settings
import os


def four_stickman():
    # dll 文件路径
    DLL_PATH_DoubleEye = os.path.join(settings.BASE_DIR, 'imageX', 'utils', "DLL", "DoubleEye.dll")
    DoubleEye = cdll.LoadLibrary(DLL_PATH_DoubleEye)

    rectify_0_path = os.path.join(settings.IMG_URL, "rectify_0.png").replace('\\', '\\\\')
    rectify_1_path = os.path.join(settings.IMG_URL, "rectify_1.png").replace('\\', '\\\\')

    out_path = str(settings.IMG_URL+'\\').replace('\\','\\\\')

    img_l = c_char_p(bytes(rectify_0_path, 'utf-8'))
    img_r = c_char_p(bytes(rectify_1_path, 'utf-8'))
    out = c_char_p(bytes(out_path, 'utf-8'))
    number = c_int(0)
    number = DoubleEye.FourStickman(img_l, img_r, out)
    print(number)
    return number