#!/usr/bin/python
#-*-coding:utf-8 -*-
import time
from appium import webdriver
import os
import shutil
from .base.template import *
from .base.getXml import get_mobile_params
from .base.makeVideo import picvideo
xml_file = "./config/config.xml"
service = get_mobile_params(xml_file,"service")  #获取启动端参数
mobile = get_mobile_params(xml_file,"mobile")  #获取启动手机参数
desired_caps = {
    "appPackage": mobile["appPackage"],
    "appActivity": mobile["appActivity"],
    "noReset": eval(mobile["noReset"]),
    "platformName": mobile["platformName"],
    "platformVersion": mobile["platformVersion"],
    "deviceName":mobile["deviceName"],
    "unicodeKeyboard": eval(mobile["unicodeKeyboard"]),
    "resetKeyboard": eval(mobile["resetKeyboard"]),
    "autoGrantPermissions": eval(mobile["resetKeyboard"])
}  #设置APP启动参数
service_url = service["host"]
service_port = service["port"]
def before_all(context):
    """在feature运行之前运行,初始化"""
    #close_shell = "adb -s "+ udid +" shell settings put global policy_control immersive.full=*"  # 关闭手机的状态栏
    #os.system(close_shell)
    context.driver = webdriver.Remote('http://{url}:{port}/wd/hub'.format(url=service_url,port=service_port),desired_caps)#初始化手机
    image_path = "./image"
    report_path = "./report"
    video_path = "./video"
    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    os.mkdir(image_path)
    if os.path.exists(report_path):
        shutil.rmtree(report_path)
    os.mkdir(report_path)
    if os.path.exists(video_path):
        shutil.rmtree(video_path)
    os.mkdir(video_path)
    with open("./report/%s.html"%(service_port), "w") as f:  #制作报告
        f.write(start_html.encode("utf8"))
def after_all(context):
    """在feature运行完毕之后,删除APP"""
    #pass
    with open("./report/%s.html"%(service_port),"a+") as f:
        f.write(end_html.encode("utf8"))
    #context.driver.remove_app("com.yunshuxie.bearword")  #删除APP
    #context.driver.close()
    context.driver.quit()
    #close_shell = "adb -s " + udid + " shell settings put global policy_control null "#开启手机状态栏
    #os.system(close_shell)
def before_feature(context, feature):
    """在feature运行之前运行,添加featue报告"""
    with open("./report/%s.html"%(service_port),"a+") as f:
        f.write(Feature_template.format(Feature=feature.name).encode("utf8"))
def after_feature(context, feature):
    """在feature运行之后运行,结束featue报告"""
    pass
def before_scenario(context, scenario):
    """在scenario运行之前运行, 添加scenario报告"""
    start_activity = context.driver.current_activity
    with open("./report/%s.html"%(service_port),"a+") as f:
        f.write(start_Scenario_template.format(Scenario=scenario.name,Activity=start_activity).encode("utf8"))
def after_scenario(context, scenario):
    """在scenario运行之后运行, 结束scenario报告"""
    end_activity = context.driver.current_activity
    video_id = picvideo(port=service_port,path="./image",video_path="./video")
    with open("./report/%s.html"%(service_port),"a+") as f:
        f.write(end_Scenario_template.format(Activity=end_activity,video_id=video_id).encode("utf8"))
def after_step(context,step):
    """每步完成后进行图片保存,日志表记录"""
    port = service_port
    file_name = "%s_%d"%(service_port,time.time())
    file_path_name = "../image/"+file_name
    with open("./report/%s.html"%(service_port),"a+") as f:
        if step.exc_traceback == None:
            msg = u"正确执行"
            status_class = "btn btn-success btn-xs collapsed"
        else:
            status_class = "btn btn-danger btn-xs collapsed"
            msg = step.exc_traceback.tb_frame.f_locals["error"]
        f.write(Step_template.format(Step=step.name,Status=step.status,file_name=file_name,file_path_name=file_path_name,
                                     msg=msg,status_class=status_class,
                                     timeer="%0.2f"%(step.duration)).encode("utf8"))
    img = context.driver.get_screenshot_as_file('./image/%s.png'%(file_name))