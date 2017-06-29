#coding: utf-8


import sys
import os
import dlib
import glob
import numpy
from skimage import io



if len( sys.argv ) != 5:
    print "请检查参数是否正确"
    exit()


# 1.人脸关键点检测器
predictor_path = sys.argv[1]

# 2.人脸识别模型
face_del_model_path = sys.argv[2]

# 3.候选人脸文件夹
faces_folder_path = sys.argv[3]

# 4.需要识别的人脸
img_path = sys.argv[4]


# 1.加载正脸检测器
detector = dlib.get_frontal_face_detector

# 2.加载人脸关键点检测器
sp = dlib.shape_predictor( predictor_path )

# 3.加载人脸识别模型
facedel = dlib.face_recognition_model_v1()

# win = dlib.image_window()


# 候选人脸描述子list
descriptors = []


# 对文件夹下的每一个人脸进行：
# 1.人脸检测
# 2.关键点检测
# 3.描述子提取


for i 
