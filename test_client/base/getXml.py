#!/usr/bin/python
#-*-coding:utf-8 -*-
import xml.etree.ElementTree as ET
def get_mobile_params(file,gen):
    tree = ET.parse(file)
    root = tree.getroot()
    s = [dict(simgleMobile) for simgleMobile in map(lambda x:[(y.tag,y.text) for y in x],[mobile for mobile in root.findall(gen) if mobile.attrib["use"]=="true"])][0] if len([mobile for mobile in root.findall(gen)  if mobile.attrib["use"]=="true" ])==1 else 0
    if s:
        return s
    else:
        raise Exception,'Error :   <mobile use="true">存在多个配置,只能存在一个使用配置！'
if __name__ == "__main__":
    print get_mobile_params("../config/config.xml",gen="service")["host"]