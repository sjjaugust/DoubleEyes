# coding:utf-8

from ctypes import *

import os

# dll 文件路径
DLL_PATH_DoubleEye = os.path.join("DLL", "DoubleEye.dll")
DoubleEye = cdll.LoadLibrary(DLL_PATH_DoubleEye)

def test():
	number = c_int(0)
	number = DoubleEye.FourStickman()
	print(number)

if __name__ == '__main__':
	test()