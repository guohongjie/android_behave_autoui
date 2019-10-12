#!/usr/bin/python
#-*-coding:utf-8 -*-
import requests
def sendQYWechatMSG(port,appPackage):
    qiye_wechat_url = r"http://msg.inf.bandubanxie.com/api/v0.2/msg/qiye_weixin"
    content = """ANDROID罐罐熊发布自动化测试结果:
发布项目: {developer_project}
发布分支: {branch}
结果查看地址: {report_url}""".format(
branch="Android_APP",
developer_project=appPackage,
report_url="http://172.10.20.61:8080/{port}.html".format(port=port)
)
    params = {"tos": "guohongjie,renhuihui,zhaohongling,pengjunxia,wangmengxiao,hongchen,tianningxue,liushuang,xuhongying,panze,jiayujiao,huyanfeng,liangguoqing",
        "content": content, "app": "qa", "sed": "guohongjie"}
    requests.post(url=qiye_wechat_url, data=params)
