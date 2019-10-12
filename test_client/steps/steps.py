#!/usr/bin/python
# -*-coding:utf-8 -*-
from behave import *
from ..base import bases
import time


@Given(u"打开 {app_name} 程序,获得当前页面前端源码")
def get_app_sourxe(context, app_name):
    context.driver.page_source
    time.sleep(1)


@Given(u"打开 {app_name} 程序,输入启动 {activity} Activity")
def start_activity(context, app_name, activity):
    context.driver.start_activity(app_name, activity)
    time.sleep(1)


@Then(u"进入 {page} 页面,校验 {text} 文本值是否存在")
def inPage_assert_element(context, page, text):
    boolean = bases.is_element_exist(context, text)
    assert boolean == True, "Not equal"


@Then(u"等待 {sleep} 秒,静等页面加载")
def sleep_time(context, sleep):
    time.sleep(int(sleep))


# 获取单一ID操作
@When(u"根据ID定位操作 {element} 元素,单击 {case}")
def click_element_by_Id(context, element, case):
    bases.elementById_click(context, element)

@When(u"根据AccessibilityID定位操作 {element} 元素,单击 {case}")
def click_element_by_Id(context, element, case):
    bases.elementByAccessibilityID_click(context, element)

@When(u"根据ID定位操作 {element} 元素,输入值 {value} 文本值 {case}")
def sendkeys_element_Id(context, element, value, case):
    bases.elementById_sendKey(context, element, value)

@Then(u"根据ID定位操作弹出 {title} 文本框,根据 {element} 元素校验文本提示信息 {value} 文本")
def alert_msg_assert_by_Id(context, title, element, value):
    text = bases.alert_text_by_Id(context, element)
    assert text == value, "Not equal!"

@Then(u"根据XPATH定位操作弹出 {title} 文本框,根据 {element} 元素校验文本提示信息 {value} 文本")
def alert_msg_assert_by_xpath(context, title, element, value):
    text = bases.alert_text_by_xpath(context, element)
    assert text == value, "Not equal!"

# 获取一组ID操作
@When(u"根据ID定位获取组 {element} 元素,单击第 {index} 个元素 {case}")
def click_elements_by_Id(context, element, index, case):
    bases.elementsById_click(context, element, index)


@When(u"根据ID定位获取组 {element} 元素,在第 {index} 个元素内输入值 {value} 文本值 {case}")
def sendkeys_elements_Id(context, element, index, value, case):
    bases.elementsById_sendKey(context, element, index, value)


# 根据class获取单个元素
@When(u"根据CLASS定位操作 {element} 元素,单击 {case}")
def click_element_by_Class(context, element, case):
    bases.elementByClass_click(context, element)


@When(u"根据CLASS定位操作 {element} 元素,输入值 {value} 文本值 {case}")
def sendkeys_element_Class(context, element, value, case):
    bases.elementByClass_sendkey(context, element, value)


# 根据class获取一组操作
@When(u"根据CLASS定位获取组 {element} 元素,单击第 {index} 个元素 {case}")
def click_elements_by_Class(context, element, index, case):
    bases.elementsByClass_click(context, element, index)


@When(u"根据CLASS定位获取组 {element} 元素,在第 {index} 个元素内输入值 {value} 文本值 {case}")
def sendkeys_elements_Class(context, element, value, index, case):
    bases.elementsByClass_sendkey(context, element, index, value)


# XPATH获取单一ID操作
@When(u"根据XPATH定位操作 {element} 元素,单击 {case}")
def click_element_by_Xpath(context, element, case):
    bases.elementByXpath_click(context, element)


@When(u"根据XPATH定位操作 {element} 元素,输入值 {value} 文本值 {case}")
def sendkeys_element_Xpath(context, element, value, case):
    bases.elementByXpath_sendKey(context, element, value)


# XPATH获取一组ID,选取其中一个操作
@When(u"根据XPATH定位获取组 {element} 元素,单击第 {index} 个元素 {case}")
def click_elements_by_xpath(context, element, index, case):
    bases.elementsByXpath_click(context, element, index)


@When(u"根据XPATH定位获取组 {element} 元素,在第 {index} 个元素内输入值 {value} 文本值 {case}")
def sendkeys_elements_xpath(context, element, index, value, case):
    bases.elementsByXpath_sendKey(context, element, index, value)


@When(u"根据Text定位,从元素 {start_element} 焦点转移至 {end_element} ,持续 {miao} 时间")
def scroll_by_text(context, start_element, end_element, miao):
    bases.scroll_page(context, start_ele=start_element, end_ele=end_element, miao=miao)


@When(u"根据Text定位,获取起点 {start} 坐标和终点 {end} 坐标设置参数值等于 {value} 参数值 {case}")
def setText(context, value, start, end, case):
    start_ele = context.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % start)
    s_x = start_ele.location.get('x')
    s_y = start_ele.location.get('y')
    end_ele = context.driver.find_element_by_android_uiautomator('new UiSelector().textContains("%s")' % end)
    e_x = end_ele.location.get('x')
    e_y = end_ele.location.get('y')
    if value == "stage":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "beta":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "2":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "3":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "4":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "5":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "6":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "7":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    elif value == "8":
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)
    else:
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)



@When(u"根据ID定位,获取起点 {start} 坐标和终点 {end} 坐标,滑动 {count} 次, {case}")
def setText(context, start, end, count, case):
    start_ele = context.driver.find_element_by_id(start)
    s_x = start_ele.location.get('x')
    s_y = start_ele.location.get('y')
    end_ele = context.driver.find_element_by_id(end)
    e_x = end_ele.location.get('x')
    e_y = end_ele.location.get('y')
    for i in range(1, int(count)):  # 滑动次数
        time.sleep(1)
        context.driver.swipe(start_x=e_x, start_y=e_y, end_y=s_y, end_x=s_x, duration=3000)


@Then(u"向上滑动屏幕,操作时间 {date} ,滑动 {count} 次,用于 {case}")
def getSwipeUp(context, date, count, case):
    bases.swipeUp(context, t=int(date), n=int(count))


@Then(u"向下滑动屏幕,操作时间 {date} ,滑动 {count} 次,用于 {case}")
def getSwipeDown(context, date, count, case):
    bases.swipeDown(context, t=int(date), n=int(count))


@Then(u"向左滑动屏幕,操作时间 {date} ,滑动 {count} 次,用于 {case}")
def getSwipeLeft(context, date, count, case):
    bases.swipeLeft(context, t=int(date), n=int(count))


@Then(u"向右滑动屏幕,操作时间 {date} ,滑动 {count} 次,用于 {case}")
def getSwipeRight(context, date, count, case):
    bases.swipeRight(context, t=int(date), n=int(count))


@Then(u"自定义滑动屏幕,操作时间 {date} ,滑动 {count} 次,起始百分比 {width} 宽和 {height} 高,终止百分比 {x_width} 宽和 {y_width} 高,用于 {case}")
def getSwipeRight(context, date, count, case,width,height,x_width,y_width):
    bases.customizeSlide(context, t=int(date), n=int(count),width=float(width),height=float(height),
                         x_width=float(x_width),y_width=float(y_width))

@Then(u"模拟手指点击 {coordinate} ,点击时常 {n} 毫秒,用于 {case}")
def tap_coordinate(context, coordinate, n, case):
    bases.tap(context, coordinate, int(n))


@Then(u"查看当前页面Activity属性")
def cat_activity(context):
    current_activity = context.driver.current_activity
    print current_activity
    with open("wctv", "w") as f:
        f.write(current_activity)


@Then(u"随机点击屏幕坐标 {count} 次,点击时常 {t} 毫秒")
def random_tap(context, count, t):
    bases.random_tap(context, count, t)
