#!/usr/bin/python
#-*-coding:utf-8 -*-
from flask import Flask,jsonify,request,send_file
import subprocess
import shutil
import os
import sys
if sys.getdefaultencoding() !="utf-8":
    reload(sys)
    sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
UPLOAD_FOLDER = "G:\\win_auto_ui_app\\package\\"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
@app.route("/start",methods=["GET"])
def start_group_test():
    try:
        project = request.args.get("project")
        branch = request.args.get("branch")
        qa_name = request.args.get("qa_name")
        message = request.args.get("message")
        subprocess.Popen(["python","start_group_test.py","{project}".format(project=project)],shell=True)
        return jsonify({"code":"200","msg":"操作成功"})
    except Exception as e:
        return jsonify({"code":"400","msg":str(e)})
@app.route("/<html>")
def report_html(html):
    try:
       # with open(".\\templates\\{port_num}".format(port_num=html)) as f:
        #    inner_html = f.read()
        return send_file(".\\templates\\{port_num}".format(port_num=html))
    except Exception as e:
        return jsonify({"code":"400","msg":str(e)})
@app.route("/upload",methods=["POST"])
def upload_file():
    try:
        apk_file = request.files["file"]
        os.system("del %s*.apk"%(UPLOAD_FOLDER))
        apk_file.save(UPLOAD_FOLDER+apk_file.filename)  #保存APK 至package
        return jsonify({"code":"200","msg":"上传成功"})
    except Exception as e:
        print e
        return jsonify({"code":"200","msg":str(e)})
@app.route("/test_group/<port>/image/<png>")
def get_png_file(port,png):
    try:
        with open(".\\test_group\\{port}/image/{png}".format(port=port,png=png),"rb") as f:
            inner_html = f.read()
        return inner_html
    except Exception as e:
        return jsonify({"code":"400","msg":str(e)})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=1234,debug=True)
