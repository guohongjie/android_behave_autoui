#!/usr/bin/python
#-*-coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import traceback
import time
import random
def get_count(retry_count=0):
    def outer(func):
        count = [0]
        def inner(*args,**kwargs):
            try:
                func(*args,**kwargs)
            except Exception as e:
                if count[0]==retry_count:
                    s = traceback.format_exc()
                    msg ="尝试{count}次操作,未成功执行该方法!\n{error}".format(count=count,error=s)
                    raise Exception,msg
                else:
                    count[0]+=1
                    return inner(*args,**kwargs)
        return inner
    return outer



def elementById_click(context,element):
    """根据ID查找元素并点击元素"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_id(element))
    curr_ele = context.driver.find_element_by_id(element)
    return curr_ele.click()

def elementByAccessibilityID_click(context,element):
    """根据AccessibilityID查找元素并点击元素"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_accessibility_id(element))
    curr_ele = context.driver.find_element_by_accessibility_id(element)
    return curr_ele.click()

def elementsById_click(context,element,index):
    """根据ID获取一组元素，并根据位置单击"""
    WebDriverWait(context, 10, 0.5).until(lambda x: x.driver.find_element_by_id(element))
    curr_ele = context.driver.find_elements_by_id(element)
    for m in range(len(curr_ele)):
        if int(index) == m :
            return curr_ele[m].click()
def elementById_sendKey(context,element,value):
    """根据ID查找元素并输入内容"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_id(element))
    curr_ele = context.driver.find_element_by_id(element)
    curr_ele.clear()  #清空输入框内容
    # curr_ele.hide_keyboard()
    return curr_ele.send_keys(value)
def elementsById_sendKey(context,element,index,value):
    """根据ID获取一组元素并输入内容"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_id(element))
    curr_ele = context.driver.find_elements_by_id(element)
    for m in range(len(curr_ele)):
        if int(index) == m :
            curr_ele[m].clear()  #清空输入框内容
            # curr_ele.hide_keyboard()
            return curr_ele[m].send_keys(value)


def elementByClass_click(context,element):
    """根据CLASS查找元素并点击元素"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_class_name(element))
    curr_ele = context.driver.find_element_by_class_name(element)
    return curr_ele.click()

def elementByClass_sendkey(context,element,value):
    """根据CLASS查找元素并输入值"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_class_name(element))
    curr_ele = context.driver.find_element_by_class_name(element)
    curr_ele.clear()  # 清空输入框内容
    # curr_ele.hide_keyboard()
    return curr_ele.send_keys(value)

def elementsByClass_click(context,element,index):
    """根据CLASS获取一组元素，并根据位置单击"""
    WebDriverWait(context, 10, 0.5).until(lambda x: x.driver.find_element_by_class_name(element))
    curr_ele = context.driver.find_elements_by_class_name(element)
    for m in range(len(curr_ele)):
        if int(index) == m :
            return curr_ele[m].click()

def elementsByClass_sendkey(context,element,index,value):
    """根据CLASS获取一组元素，并根据位置输入内容"""
    WebDriverWait(context, 10, 0.5).until(lambda x: x.driver.find_element_by_class_name(element))
    curr_ele = context.driver.find_elements_by_class_name(element)
    for m in range(len(curr_ele)):
        if int(index) == m :
            curr_ele.clear()
            return curr_ele[m].send_keys(value)

def elementByXpath_click(context,element):
    """根据xpath查找元素并点击元素"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_xpath(element))
    curr_ele = context.driver.find_element_by_xpath(element)
    return curr_ele.click()
def elementsByXpath_click(context,element,index):
    """根据xpath查找元素并点击元素"""
    WebDriverWait(context, 10, 0.5).until(lambda x: x.driver.find_element_by_xpath(element))
    curr_ele = context.driver.find_elements_by_xpath(element)
    for m in range(len(curr_ele)):
        if int(index) == m:
            return curr_ele[m].click()

def elementByXpath_sendKey(context,element,value):
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_xpath(element))
    curr_ele = context.driver.find_element_by_xpath(element)
    curr_ele.clear()
    # curr_ele.hide_keyboard()
    return curr_ele.send_keys(value)

def elementsByXpath_sendKey(context,element,index,value):
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_xpath(element))
    curr_ele = context.driver.find_elements_by_xpath(element)
    for m in range(len(curr_ele)):
        if int(index) == m :
            curr_ele[m].clear()  #清空输入框内容
            # curr_ele.hide_keyboard()
            return curr_ele[m].send_keys(value)

def is_element_exist(context,text):
    """校验texts是否存在于page"""
    time.sleep(1)
    source = context.driver.page_source
    if text in source:
        return True
    else:
        return False

def alert_text_by_Id(context,element):
    """定位元素,打印元素text值"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_id(element))
    value_text = context.driver.find_element_by_id(element).text
    return value_text

def alert_text_by_xpath(context,element):
    """定位元素,打印元素text值"""
    WebDriverWait(context,10,0.5).until(lambda x:x.driver.find_element_by_xpath(element))
    value_text = context.driver.find_element_by_xpath(element).text
    print value_text
    return value_text

def scroll_page(context,start_ele,end_ele,miao):
    miao = int(miao) * 1000
    start_ele = context.driver.find_element_by_android_uiautomator('new UiSelector().textContains("%s")'%(start_ele))
    end_ele = context.driver.find_element_by_android_uiautomator('new UiSelector().textContains("%s")'%(end_ele))
    context.driver.scroll(start_ele,end_ele,miao)
def swipeUp(context,t=500,n=1):  #t 滑动时间.n 滑动次数
    """中心点向上滑动"""
    l = context.driver.get_window_size()  #获取屏幕大小
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        context.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(1)
def swipeDown(context, t=500, n=1):
    '''向下滑动屏幕'''
    l = context.driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        context.driver.swipe(x1, y1, x1, y2,t)
        time.sleep(1)
def swipeLeft(context, t=500, n=1):
    '''向左滑动屏幕'''
    l = context.driver.get_window_size()
    x1 = l['width'] * 0.85
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        context.driver.swipe(x1, y1, x2, y1, t)
        time.sleep(1)
def swipeRight(context, t=500, n=1):
    '''向右滑动屏幕'''
    l = context.driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.85
    for i in range(n):
        context.driver.swipe(x1, y1, x2, y1, t)
        time.sleep(1)
def customizeSlide(context, t=500, n=1 ,width=0,height=0,x_width=0,y_width=0):
    '''向右滑动屏幕'''
    l = context.driver.get_window_size()
    x1 = l['width'] * width
    y1 = l['height'] * height
    x2 = l['width'] * x_width
    y2 = l['width'] * y_width
    for i in range(n):
        context.driver.swipe(x1, y1, x2, y2, t)
        time.sleep(1)
def tap(context,coordinate,t=500):
    """模拟手指点击元素左边"""
    list_tuple_coordinate = eval(coordinate)
    context.driver.tap(list_tuple_coordinate,t)
def random_tap(context,count,t):
    """随机点击屏幕坐标，count 点击次数 t点击时常"""
    l = context.driver.get_window_size()
    x = l['width']
    y = l['height']
    for tap in range(1,int(count)):
        random_x = random.randint(0, x)
        random_y = random.randint(0, y)
        context.driver.tap([(random_x,random_y)],t)
