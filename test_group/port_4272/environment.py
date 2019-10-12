#!/usr/bin/python
#-*-coding:utf-8 -*-
import time
from appium import webdriver
import os
from .base.template import *
from .base.qy_wechat import sendQYWechatMSG
from .base.makeVideo import picvideo
import datetime
import shutil
#app_path = ".\\templates\\package"  #APP存放路径
app_path = r"G:\\win_auto_ui_app\\package\\"
apk_list = os.listdir(app_path)
apk_list.remove("__init__")
install_app_path = os.path.join(app_path,apk_list[0] )
if apk_list[0][:3].upper() == "YSX":
    appPackage = "com.yunshuxie.main"
    appActivity = "com.yunshuxie.main.SplashActivity"
elif apk_list[0][:3].upper() == "GGX":
    appPackage = "com.yunshuxie.bearword"
    appActivity = "com.yunshuxie.bearword.ui.activity.SplashActivity"
udid = "Q5S5T19419004309"
desired_caps = {
    "app": install_app_path,
    "appPackage": appPackage,
    "appActivity": appActivity,
    "noReset": True,
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "huawei p20",
    "udid":udid,
    "unicodeKeyboard": True,
    "resetKeyboard": True, "autoGrantPermissions": True
}  #设置APP启动参数

def before_all(context):
    """在feature运行之前运行,初始化"""
    now_time = datetime.datetime.now()
    context.driver = webdriver.Remote('http://172.10.20.61:4272/wd/hub',desired_caps)#初始化手机
    image_path = ".\\test_group\\port_4272\\image"
    report_path = ".\\test_group\\port_4272\\report"
    video_path = ".\\test_group\\port_4272\\video"
    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    os.mkdir(image_path)
    if os.path.exists(report_path):
        shutil.rmtree(report_path)
    os.mkdir(report_path)
    if os.path.exists(video_path):
        shutil.rmtree(video_path)
    os.mkdir(video_path)
    if os.listdir(image_path):
        os.popen("del {path}\\*.png".format(path=image_path))
    with open(".\\templates\\4272.html", "w") as f:  #制作报告
        html_1 = start_html.replace("{{{project_cn}}}",appPackage)
        html_2 = html_1.replace("{{{start_time}}}",str(now_time))
        f.write(html_2.encode("utf8"))
    #close_shell = "adb -s " + udid + " shell settings put global policy_control immersive.full=*"  # 关闭手机的状态栏
    #os.system(close_shell)
def after_all(context):
    """在feature运行完毕之后,删除APP"""
    #pass
    with open(".\\templates\\4272.html","a+") as f:
        now_time = datetime.datetime.now()
        script = u"""<script>$('#report_status').append('<p class="attribute"><strong>结束时间 : </strong> {end_time}</p>')</script>""".format(end_time=str(now_time))
        f.write(end_html.format(script=script).encode("utf8"))
    context.driver.remove_app("{appPackage}".format(appPackage=appPackage))  #删除APP
    context.driver.quit()
    sendQYWechatMSG("4272",appPackage)
    #close_shell = "adb -s " + udid + " shell settings put global policy_control null "#开启手机状态栏
    #os.system(close_shell)

def before_feature(context, feature):
    """在feature运行之前运行,添加featue报告"""
    with open(".\\templates\\4272.html","a+") as f:
        f.write(Feature_template.format(Feature=feature.name).encode("utf8"))
def after_feature(context, feature):
    """在feature运行之后运行,结束featue报告"""
    pass
def before_scenario(context, scenario):
    """在scenario运行之前运行, 添加scenario报告"""
    start_activity = context.driver.current_activity
    with open(".\\templates\\4272.html","a+") as f:
        f.write(start_Scenario_template.format(Scenario=scenario.name,Activity=start_activity).encode("utf8"))
def after_scenario(context, scenario):
    """在scenario运行之后运行, 结束scenario报告"""
    end_activity = context.driver.current_activity
    video_id = picvideo(port="4272", path=".\\test_group\\port_4272\\image", video_path=".\\test_group\\port_4272\\video")
    #context.driver.close_app()
    with open(".\\templates\\4272.html","a+") as f:
        f.write(end_Scenario_template.format(Activity=end_activity,video_id=video_id).encode("utf8"))
def after_step(context,step):
    """每步完成后进行图片保存,日志表记录"""
    port = "4272"
    file_name = "4272_%d"%(time.time())
    file_path_name = ".\\test_group\\port_4272\\image\\"+file_name
    with open(".\\templates\\4272.html","a+") as f:
        if step.exc_traceback == None:
            msg = u"正确执行"
            status_class = "btn btn-success btn-xs collapsed"
        else:
            status_class = "btn btn-danger btn-xs collapsed"
            msg = step.exc_traceback.tb_frame.f_locals["error"]
        f.write(Step_template.format(Step=step.name,Status=step.status,file_name=file_name,file_path_name=file_name,
                                     msg=msg,status_class=status_class,
                                     timeer="%0.2f"%(step.duration)).encode("utf8"))
    img = context.driver.get_screenshot_as_file('.\\test_group\\port_4272\\image\\%s.png'%(file_name))

