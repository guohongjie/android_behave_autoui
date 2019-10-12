Feature: 罐罐熊练字课-测试环境登录
Scenario: 单流程案例-测试环境登录
When 根据ID定位操作 com.yunshuxie.bearword:id/tv_my 元素,单击 我的tab页
Then 进入 我的 页面,校验 我的积分 文本值是否存在
When 根据ID定位操作 com.yunshuxie.bearword:id/tv_login 元素,单击 登录/注册
When 根据ID定位操作 com.yunshuxie.bearword:id/tv_pwd 元素,单击 账号密码登录
When 根据ID定位操作 com.yunshuxie.bearword:id/edt_login_num 元素,输入值 60000021384 文本值 输入用户名
When 根据ID定位操作 com.yunshuxie.bearword:id/edt_login_code 元素,输入值 123456 文本值 输入密码
Then 等待 2 秒,静等页面加载
When 根据ID定位操作 com.yunshuxie.bearword:id/tv_login 元素,单击 登录按钮
Then 进入 我的 页面,校验 积分商城 文本值是否存在