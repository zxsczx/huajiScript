#   --------------------------------注释区--------------------------------
#   入口:微信打开 http://280766611022122.sqji03licp.cn/r?14u=37x&a4i=5qm&g2z=y8q&iyq=bi2&upuid=2807666&vi6=p1x
#   走个头谢谢 不然没更新动力了呜呜呜
#
#   抓取m.zzyi4cf7z8.cn域名下的请求头中udtauth12的值填入
#   如微信提现:
#   直接在变量里直接填入udtauth12的值
#   如支付宝提现:
#   则填写 udtauth12的值#支付宝账号或邮箱#支付宝真实姓名
#
#   在抓取上面的udtauth12时同时抓取请求头中的user-agent填入yuanshen_useragent 多号也只需一个，与其他阅读通用，之前填过了或其他阅读填过了无需再增加
#
#   corn: 一小时一次即可
#
#   检测配置：
#   只能使用Wxpusher进行检测文章推送 不阅读检测文章会导致黑号
#   在https://wxpusher.zjiecode.com/admin/login 登录Wxpusher 新建一个应用和在应用内创建一个主题 并且使用微信关注你创建的主题
#   在yuanshen_apptoken 填入你的wxpusher的apptoken (就是你创建的应用的apptoken)
#   在yuanshen_topicid 填入你的wxpusher的TopicId (就是你创建的主题的的TopicId) 此项是5位数字 并不是Uid
#   不懂看 https://wxpusher.zjiecode.com/docs/#/ 或 百度 或 打钱
#   收到推送时 使用微信点击推送 即可自动跳转到检测文章完成阅读 一定要手动点击否则会黑号 黑号需要等待第二天后才能再次跑
#
#   下面的配置 !!!不懂默认 不懂默认 不懂默认!!!
#   如需改动在脚本内改,而不是新建环境变量!!
withdrawal_money = 3000 # 提现金币数量 1000金币=0.1r
Quantity_limit = 180  # 阅读上限篇数 跑满(195篇左右)概率封号
fuck_list = [1,2,126] # 强制识别为检测文章并推送篇数 不懂默认 需要新加的话在后面用 英文逗号加篇数 新增自定义参数就行 
max_threads = 1 #运行线程数 不懂默认
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
'''
Powered By Huaji
QQ Group:901898186
Create at [2024-11-02 21:21]

 __    __   __    __       ___             __   __  
|  |  |  | |  |  |  |     /   \           |  | |  | 
|  |__|  | |  |  |  |    /  ^  \          |  | |  | 
|   __   | |  |  |  |   /  /_\  \   .--.  |  | |  | 
|  |  |  | |  `--'  |  /  _____  \  |  `--'  | |  | 
|__|  |__|  \______/  /__/     \__\  \______/  |__|                                                

'''

import base64, zlib, lzma, bz2, gzip
exec((lambda MoegbymG: compile(MoegbymG, '<string>', 'exec'))(zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode('H4sIAFknJmcC/wHaKiXVQlpoOTFBWSZTWV1dmy0AFDt/////////////////////////////////////////////4BpfXa7zPvnrbfd3vnvd8r599ufV7nrfb4lOz7tb33d7qj59ut19e8+5b75vu9759vd989908+6vu73tvt98e83W12+5vm7b77ee++6++27vbl73be997c5d7vvffe87729vkKn6aZTw0J5DTQqfgDSameRoIxPRNNoBoTCj00xpMjCbRqbRPRNNTYATVPwNSbKb1Mp+gmJqY00aJ6TYTyDVPBGNAaT000GIABommZEodVPzSbUwk/VP0mamaRk1PCYExqYTJ6FPAmqfiGGmgaFPCaYNCHqZMNCp+jTDQyjExJtMI8EMmiemRiDIABBptCaj9BBiaaYTTUbRlRCp+mGphPU0yMRgDU9VP8hR6aYTap+hoEeiTwI02kbUxPUepgZKeSabGU2gMmITMjKeKepmimwibGp6EzUxoTACYaak9NDUeRgpmmRpP1PSGKIU/RND0Ew1NpNNTxoTCniHkTJp6DU9BMp4nghpphTyNGpmjCJmU1PEZpT0NGJpkymeqbNJtTEwammIYTIYU8jJ6EMhk2piNNPUxMNU9Gmp4kOqeU/TQDQpsammnoap5T8TTTEZTJ5MmmmIaaI0YFPJ6k9GAj1NqeQmTAATU9pNkMgCJk9Mk9J6ZNpMCjZTaZGp4p6angEGJk00YnqnhNNTynkh1T8mQxMRpiYjAmptKfo0yCT2hJ5NGR6mU3pop+oJsaUzTGppptJo0yek0yPKnqejMU0whiT1PI9TEMCNTzRTZqTwnqNNJsE9FNiZBoNqCenqm1PCIBAQDQOBboCAiPMCANYH72lh/3adk4HfW83dB6gNo3OiljZ2lvRPlajySwHxVbjPbJZ4oa2kE7ISra2xk1CN1b+Xuwf3/KE4yX1umG/CoA6wsg1jhhGapII2/V+KykETfwPZUKUqnYcp5rREV8ViFmMegjy3mdF0qLtaaeXsTdItsQcYwLylpzz/5pzlY7SNbxWbTW2ouRY7w1zMbmduREjb7TL+vNtKPbyLPGM/qwkgugfvLwZF9iGV71iVNGtJYA2Wgf+cVVTHuxiI0fV8YcsZwHlNYmo26rch9gSYDAwY+aJAVDLreMu06fgFzKb5xfFiNWDWEeWl3nmB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'))))).decode()))
#!Look Your Mother! At the end there was nothing!
