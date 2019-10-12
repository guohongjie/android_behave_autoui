#!/usr/bin/python
#-*-coding:utf-8 -*-
import os
import subprocess
import sys
if sys.getdefaultencoding() !="utf8":
    reload(sys)
    sys.setdefaultencoding("utf8")
project = sys.argv[1]
# if project=="ggx":
#     project=u"ggx"
# elif project=="ysx":
#     project=u"ysx"
current_path = os.getcwd()
test_path = os.getcwd() + "\\test_group"
file_test_path = lambda x:[x+"\\"+ m for m in os.listdir(x)]
group_test_path = file_test_path(test_path)
featureFileList =  ["*.feature"]
for featureFile in featureFileList:
    for test_port_path in group_test_path:
        #print test_port_path
        os.system(r"del {test_port_path}\\*.feature".format(test_port_path=test_port_path))
        os.system(r"copy .\\feature\\{project}\\*.feature  {test_port_path}\\".format(project=project,test_port_path=test_port_path))
    #复制feature文件至测试文件夹内
def start_test(start_dir):
    subprocess.Popen(["behave","{start_dir}".format(start_dir=start_dir)])
for start_dir in group_test_path:
    #t = multiprocessing.Process(target=start_test,args=(start_dir,))
    #t.start()
    print start_dir
    start_test(start_dir)
