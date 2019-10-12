#!/usr/bin/python
#-*-coding:utf-8 -*-
import os
import cv2
import shutil
import time
def picvideo(port,path, video_path):
    timestamp = "%d"%time.time()
    filelist = os.listdir(path)
    port_image_list = []
    for item in filelist:
        if item.startswith(port):
            port_image_list.append(item)
    sp = cv2.imread(path+"/%s"%(port_image_list[0])).shape #获取第一张图片分辨率
    height = sp[0]  # height(rows) of image
    width = sp[1]  # width(colums) of image
    size = (width,height)
    file_name = "%s_%s"%(port,timestamp)
    file_path = video_path +"/"+file_name +".mp4" # 导出路径
    fps = 2
    video = cv2.VideoWriter(file_path, -1, fps, size)
    for item in filelist:
        if item.endswith('.png'):  # 判断图片后缀是否是.png
            if item.startswith(port):
                item = path + '/' + item
                img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
                video.write(img)  # 把图片写进视频
    video.release()  # 释放
    cv2.destroyAllWindows()
    return file_name
if __name__ == "__main__":
    print picvideo(port='4271',path="../image")