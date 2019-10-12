#!/usr/bin/python
# -*-coding:utf-8
start_html = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!-- saved from url=(0104)http://uwsgi.sys.bandubanxie.com/Report/8/9/%E4%BA%91%E8%88%92%E5%86%99CRM%E7%B3%BB%E7%BB%9F_beta_7.html -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>《{project_cn}》--接口测试报告</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2.1">
        <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>

<style type="text/css" media="screen">
body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%; }
table       { font-size: 100%; }
/* -- heading ---------------------------------------------------------------------- */
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}
.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- report ------------------------------------------------------------------------ */
#total_row  { font-weight: bold; }
.passCase   { color: #5cb85c; }
.failCase   { color: #d9534f; font-weight: bold; }
.errorCase  { color: #f0ad4e; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
</style>

</head>
<body style="">
<script language="javascript" type="text/javascript">
output_list = Array();
/*level 调整增加只显示通过用例的分类 --Findyou
0:Summary //all hiddenRow
1:Failed  //pt hiddenRow, ft none
2:Pass    //pt none, ft hiddenRow
3:All     //pt none, ft none
*/
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level == 2 || level == 0 ) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level < 2) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
    }
    //加入【详细】切换文字变化 --Findyou
    detail_class=document.getElementsByClassName('detail');
	//console.log(detail_class.length)
	if (level == 3) {
		for (var i = 0; i < detail_class.length; i++){
			detail_class[i].innerHTML="收起"
		}
	}
	else{
			for (var i = 0; i < detail_class.length; i++){
			detail_class[i].innerHTML="详细"
		}
	}
}
function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        //ID修改 点 为 下划线 -Findyou
        tid0 = 't' + cid.substr(1) + '_' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        //修改点击无法收起的BUG，加入【详细】切换文字变化 --Findyou
        if (toHide) {
            document.getElementById(tid).className = 'hiddenRow';
            document.getElementById(cid).innerText = "详细"
        }
        else {
            document.getElementById(tid).className = '';
            document.getElementById(cid).innerText = "收起"
        }
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>
<script> 
function playPause(id)
{ 
    var myVideo=document.getElementById(id); 
	if (myVideo.paused) 
	  myVideo.play(); 
	else 
	  myVideo.pause(); 
} 
	function makeBig(id)
{ 
    var myVideo=document.getElementById(id); 
	myVideo.width=myVideo.width+30; 
} 
	function makeSmall(id)
{ 
    var myVideo=document.getElementById(id); 
	myVideo.width=myVideo.width-30; 
} 
	function makeNormal(id)
{ 
    var myVideo=document.getElementById(id); 
	myVideo.width=110; 
} 
</script> 
<div class="heading">
<h1 style="font-family: Microsoft YaHei">《{project_cn}》--接口测试报告</h1>
<p class="attribute"><strong>测试人员 : </strong> 最棒QA</p>
<p class="attribute"><strong>开始时间 : </strong> {start_time}</p>
<p class="attribute"><strong>结束时间 : </strong> {end_time}</p>
<p class="attribute"><strong>测试结果 : </strong> 共 {case_total}，通过 {case_pass}</p>
<p class="attribute"><strong>测试环境 : </strong> {env_flag}</p>
<p class="attribute"><strong>环境编号 : </strong> {env_num}</p>
<p class="description">云舒写CRM系统</p>
</div>
<p id="show_detail_line">
<a class="btn btn-primary" href="javascript:showCase(0)">概要{ 100.00% }</a>
<a class="btn btn-danger" href="javascript:showCase(1)">失败{ {case_fail} }</a>
<a class="btn btn-success" href="javascript:showCase(2)">通过{ {case_pass} }</a>
<a class="btn btn-info" href="javascript:showCase(3)">跳过{ {case_total} }</a>
</p>
 <table id="result_table" class="table table-condensed table-bordered table-hover" border="3">
"""
end_html = u"""
</table>
</body></html>"""

Feature_template = u"""
<tr class="passClass warning"> 
<td class="text-center" colspan="3">Feature : {Feature}</td>
</tr>
"""


start_Scenario_template = u"""
 <tr class="passClass warning">
    <td class="text-center" style="width:20%">Scenario : {Scenario}<td>
    <table border="1" width="100%" height="100%">
             <tr>
             	<th style="width:40%" class="text-center">Step</th>
             	<th style="width:10%" class="text-center">Status</th>
                <th style="width:40%" class="text-center">详细</th>
                <th style="width:10%" class="text-center">timmer</th>
             </tr>
    <tr class="passClass warning"><td colspan="4" class="text-center">StartActivity : {Activity}</td></tr>
"""
end_Scenario_template = u"""
<tr class="passClass warning"><td colspan="4" class="text-center">EndActivity : {Activity}</td></tr>
</table>
<td class="text-center">
<div style="text-align:center"> 
  <button onclick="playPause('{video_id}')">播放/暂停</button> 
  <button onclick="makeBig('{video_id}')">放大</button>
  <button onclick="makeSmall('{video_id}')">缩小</button>
  <button onclick="makeNormal('{video_id}')">普通</button>
  <br> 
  <video id="{video_id}" width="110">
    <source src="http://172.10.20.61:8080/video4272/{video_id}.mp4" type="video/mp4">
    您的浏览器不支持 HTML5 video 标签。
  </video>
</div></td>
</tr>

"""
Step_template = u"""
<tr class="passClass warning">
<td class="text-center">{Step}</td>
<td class="text-center"><button type="button" class="{status_class}" data-toggle="collapse" data-target="#btn_msg_{file_name}">{Status}</button>
<div id="btn_msg_{file_name}" class="collapse" style="height: 0px;"> 
<pre>{msg}</pre>
</div>
</td>
<td class="text-center">
<button id="btn_resp_json" type="button" class="btn btn-success btn-xs collapsed" data-toggle="collapse" data-target="#btn_{file_name}">详细</button>
<div id="btn_{file_name}" class="collapse" style="height: 0px;"> 
<img class="text-center" src="http://172.10.20.61:8080/image4272/{file_path_name}.png" height="60%" width="60%" />
</div></td>
<td class="text-center">{timeer}</td>
</tr>
"""
if __name__ == "__main__":
    Feature = "WCTV_FEATURE"
    Scenario = "WCTV_Scenario"
    Step = "WCTV_Step"
    Status = "pass"
    StepDetail = "StepDetail"
    timeer = "0.01"
    with open("wctv.html","a+") as f:
        f.write(Feature_template.format(Feature=Feature).encode("utf8"))
        f.write(start_Scenario_template.format(Scenario=Scenario).encode("utf8"))
        f.write(Step_template.format(Step=Step,Status=Status,StepDetail=StepDetail,timeer=timeer).encode("utf8"))
        f.write(end_Scenario_template.encode("utf8"))
        f.write(end_html.encode("utf8"))

