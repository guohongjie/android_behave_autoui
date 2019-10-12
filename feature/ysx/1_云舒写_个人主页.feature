Feature: 云舒写
Scenario: 个人中心-设置中心-护眼模式/消息免打扰/清除缓存
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
Then 向上滑动屏幕,操作时间 500 ,滑动 1 次,用于 查看设置中心
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_setting 元素,单击 设置中心
Then 进入 设置 页面,校验 退出账号 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/iv_eye 元素,单击 护眼模式开关按钮
When 根据ID定位操作 com.yunshuxie.main:id/ll_mian_darao 元素,单击 消息免打扰按钮
Then 进入 消息提醒 页面,校验 离线消息推送 文本值是否存在
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch 元素,单击 离线消息推送开启按钮
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch 元素,单击 自定义C2C消息推送声音关闭按钮
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch 元素,单击 自定义C2C消息推送声音开启按钮
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch 元素,单击 自定义群消息推送声音关闭按钮
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch 元素,单击 自定义群消息推送声音开启按钮
When 根据ID定位操作 com.yunshuxie.main:id/title_back 元素,单击 返回按钮
Then 进入 设置 页面,校验 消息免打扰 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_clean_deate 元素,单击 清除缓存
Then 进入 清除缓存提示 页面,校验 是否清除本地缓存文件 文本值是否存在
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1] 元素,单击 是按钮
Then 进入 设置 页面,校验 清除缓存 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_clean_deate 元素,单击 清除缓存
When 根据XPATH定位操作 /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2] 元素,单击 否按钮
Then 进入 设置 页面,校验 清除缓存 文本值是否存在



Scenario: 个人中心-登录验证
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 登录/注册 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_mine_login 元素,单击 登录/注册
Then 进入 登录 页面,校验 密码登录 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/_edt_login_num 元素,输入值 60000008001 文本值 输入学习账号
When 根据ID定位操作 com.yunshuxie.main:id/ll_pas 元素,输入值 123456 文本值 输入密码
When 根据ID定位操作 com.yunshuxie.main:id/_btn_login_login 元素,单击 登录
Then 根据ID定位操作弹出 家长监护模式 文本框,根据 com.yunshuxie.main:id/tvOpen 元素校验文本提示信息 开启家长监护模式 文本
When 根据ID定位操作 com.yunshuxie.main:id/tvSure 元素,单击 我知道了按钮
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在

Scenario: 个人中心-阅读能量值验证
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_read_count 元素,单击 阅读能量值
When 根据ID定位操作 com.yunshuxie.main:id/linear_all 元素,单击 课程位图
Then 进入 阅历 页面,校验 阅历 文本值是否存在

Scenario: 个人中心-积分记录-我的积分-如何获得积分
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_mine_jifen 元素,单击 积分记录
Then 进入 我的积分 页面,校验 我的积分 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/text_rule 元素,单击 如何获得积分
Then 进入 积分规则 页面,校验 积分 文本值是否存在

Scenario: 个人中心-积分记录-我的积分-积分商城/我的兑换
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_mine_jifen 元素,单击 积分记录
Then 进入 我的积分 页面,校验 积分明细 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_exchange_integral 元素,单击 我的兑换
When 根据CLASS定位操作 android.widget.ImageButton 元素,单击 返回按钮
When 根据ID定位操作 com.yunshuxie.main:id/tv_integral_mall 元素,单击 积分商城
Then 进入 积分商城 页面,校验 积分商城 文本值是否存在
When 根据AccessibilityID定位操作 如何获得积分 元素,单击 如何获得积分
Then 进入 积分规则 页面,校验 积分规则 文本值是否存在
When 根据CLASS定位操作 android.widget.ImageButton 元素,单击 返回按钮

Scenario: 个人中心-积分商城-商品兑换
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_mine_jifenmap 元素,单击 积分商城
Then 进入 积分商城 页面,校验 积分 文本值是否存在
When 根据XPATH定位操作 (//android.view.View[@content-desc="价格 "])[1] 元素,单击 价格Tab
When 根据XPATH定位操作 (//android.view.View[@content-desc="价格 "])[1]/android.view.View/android.view.View[2] 元素,单击 价格排序按钮
When 根据XPATH定位操作 (//android.view.View[@content-desc="热门兑换"])[1] 元素,单击 热门兑换Tab
When 根据XPATH定位操作 //android.view.View[@content-desc="感恩母亲红色零钱包 250分 兑换"] 元素,单击 感恩母亲红色零钱包
Then 进入 商品详情 页面,校验 立即兑换 文本值是否存在
Then 模拟手指点击 [(int("221"),int("924"))] ,点击时常 300 毫秒,用于 点击立即兑换
Then 模拟手指点击 [(int("221"),int("924"))] ,点击时常 300 毫秒,用于 点击立即兑换
Then 进入 积分不足弹窗 页面,校验 抱歉，您的积分不足 文本值是否存在
When 根据XPATH定位操作 //android.view.View[@content-desc="确认"] 元素,单击 确认按钮


Scenario: 个人中心-邀请返现-返现说明/查看明细（有问题）
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_mine_fanxian 元素,单击 邀请返现
Then 进入 邀请返现 页面,校验 返现课程 文本值是否存在
When 根据XPATH定位操作 //android.view.View[@content-desc="返现说明"] 元素,单击 返现说明
Then 进入 邀请帮助 页面,校验 返现规则 文本值是否存在
When 根据CLASS定位操作 android.widget.ImageButton 元素,单击 返回按钮
When 根据XPATH定位操作 //android.view.View[@content-desc="查看明细"] 元素,单击 查看明细
Then 进入 邀请明细 页面,校验 点击去邀请 文本值是否存在
Then 模拟手指点击 [(int("261"),int("717"))] ,点击时常 300 毫秒,用于 点击去邀请
When 根据XPATH定位操作 (//android.view.View[@content-desc="点击邀请"])[1] 元素,单击 点击邀请
Then 进入 分享 页面,校验 好友报名后您可获得 文本值是否存在
When 根据CLASS定位操作 android.widget.Image 元素,单击 关闭按钮
Then 进入 邀请好友 页面,校验 邀请好友 文本值是否存在


Scenario: 个人中心-代金券
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/tv_mine_daijinquan 元素,单击 代金券
Then 进入 代金券 页面,校验 我的代金券 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_villusefragment 元素,单击 待生效
Then 进入 待生效Tab 页面,校验 还没有即将生效代金券 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_usedfragment 元素,单击 已用/过期
Then 进入 已用/过期Tab 页面,校验 暂无过期或已使用过的代金券 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_usingfragment 元素,单击 可用
Then 进入 可用Tab 页面,校验 暂无可用代金券 文本值是否存在

Scenario: 个人中心-作品点评
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 	com.yunshuxie.main:id/ll_mine_dianping 元素,单击 作品点评
Then 进入 作品点评 页面,校验 资深名师一对一作品点评 文本值是否存在

Scenario: 个人中心-能量统计
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_energy 元素,单击 能量统计
Then 进入 阅读能量 页面,校验 分能量值 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/rl_bookDetail_plan 元素,单击 展示交流TAB
Then 进入 展示交流 页面,校验 作品互动 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/rl_bookDetail_teacher 元素,单击 阅读品味TAB
Then 进入 阅读品味 页面,校验 我的阅历 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/rl_bookDetail_shuoming 元素,单击 阅读质量TAB
Then 进入 阅读质量 页面,校验 阅读字数 文本值是否存在

Scenario: 个人中心-我的成就
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_chengjiu 元素,单击 我的成就
Then 进入 我的成就 页面,校验 我的成就 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_classjob 元素,单击 班级作品
Then 进入 班级作品 页面,校验 班级作品 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_achievement 元素,单击 个人奖状
Then 进入 个人奖状 页面,校验 个人奖状 文本值是否存在

Scenario: 个人中心-我的班级
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_class 元素,单击 我的班级
Then 进入 我的班级 页面,校验 还没有加入过班级 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/main_top_right 元素,单击 加入班级
Then 进入 加入班级 页面,校验 已经获得班级号和密码的学生 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/et_workcenter 元素,输入值 001 文本值 输入班级号
When 根据ID定位操作 com.yunshuxie.main:id/et_workcenter_pwd 元素,输入值 abc123 文本值 输入密码
When 根据ID定位操作 com.yunshuxie.main:id/workCenter_bt_pre 元素,单击 确认

Scenario: 个人中心-学习签到
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_checkin 元素,单击 学习签到
Then 进入 签到记录 页面,校验 签到积分说明 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/main_top_right 元素,单击 已签到
When 根据ID定位操作 com.yunshuxie.main:id/btn_right 元素,单击 日历向右按钮
When 根据ID定位操作 com.yunshuxie.main:id/btn_left 元素,单击 日历向左按钮

Scenario: 个人中心-课程订单
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_orders 元素,单击 课程订单
Then 进入 课程订单 页面,校验 咨询 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/main_top_right 元素,单击 咨询
Then 进入 呼叫弹窗 页面,校验 400-600-9950 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/dilaog_helper_double_left 元素,单击 取消按钮
Then 进入 课程订单 页面,校验 课程订单 文本值是否存在

Scenario: 个人中心-我的下载
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
Then 向上滑动屏幕,操作时间 500 ,滑动 1 次,用于 查看我的下载
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_download 元素,单击 我的下载
When 根据ID定位操作 com.yunshuxie.main:id/rb_right 元素,单击 下载中TAB
Then 进入 下载中 页面,校验 暂无下载任务 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/rb_left 元素,单击 已下载TAB
Then 进入 已下载 页面,校验 暂无缓存视频 文本值是否存在

Scenario: 个人中心-给个好评
Given 打开 com.yunshuxie.main 程序,输入启动 .MainUI Activity
Then 进入 首页 页面,校验 云舒写 文本值是否存在
When 根据ID定位操作 com.yunshuxie.main:id/btn_apply_class 元素,单击 个人中心
Then 进入 个人中心 页面,校验 潘泽 文本值是否存在
Then 向上滑动屏幕,操作时间 500 ,滑动 1 次,用于 查看给个好评
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_comment 元素,单击 给个好评
Then 进入 选择哪个平台评价 页面,校验 选择要使用的应用 文本值是否存在
Then 模拟手指点击 [(int("152"),int("493"))] ,点击时常 300 毫秒,用于 点击软件商店
Then 进入 软件商店 页面,校验 106万次安装 文本值是否存在
Then 模拟手指点击 [(int("50"),int("75"))] ,点击时常 300 毫秒,用于 点击返回按钮
When 根据ID定位操作 com.yunshuxie.main:id/ll_mine_comment 元素,单击 给个好评
Then 模拟手指点击 [(int("378"),int("427"))] ,点击时常 300 毫秒,用于 点击豌豆荚
Then 进入 豌豆荚 页面,校验 更新说明 文本值是否存在
When 根据ID定位操作 com.wandoujia.phoenix2:id/e_ 元素,单击 返回按钮
Then 进入 个人中心 页面,校验 给个好评 文本值是否存在