"""
    基础过程
"""
API_target = "https://wx.qq.com"  # 主页
API_target_login = "https://login.wx.qq.com"  # 登录
API_jsLogin = f"{API_target_login}/jslogin?appid=wx782c26e4c19acffb&redirect_uri={API_target}/cgi-bin/mmwebwx-bin/webwxnewloginpage&fun=new&lang=zh_CN"
API_qrcode = f"{API_target_login}/qrcode/"  # 二维码
API_login = f"{API_target}/cgi-bin/mmwebwx-bin/login"
API_check_login = f"{API_target_login}/cgi-bin/mmwebwx-bin/login"
API_synccheck = "https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck"  # 消息监测
API_webwxdownloadmedia = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetmedia"
API_webwxuploadmedia = f"{API_target}/cgi-bin/mmwebwx-bin/webwxuploadmedia"
API_webwxpreview = f"{API_target}/cgi-bin/mmwebwx-bin/webwxpreview"
API_webwxinit = f"{API_target}/cgi-bin/mmwebwx-bin/webwxinit"
API_webwxgetcontact = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetcontact"
API_webwxsync = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsync"
API_webwxbatchgetcontact = f"{API_target}/cgi-bin/mmwebwx-bin/webwxbatchgetcontact"
API_webwxgeticon = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgeticon"
API_webwxlogout = f"{API_target}/cgi-bin/mmwebwx-bin/webwxlogout"


"""
    消息发送
"""
API_webwxsendmsg = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsendmsg"
API_webwxsendmsgimg = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsendmsgimg"
API_webwxsendmsgvedio = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsendvideomsg"
API_webwxsendemoticon = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsendemoticon"
API_webwxsendappmsg = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsendappmsg"


"""
    消息获取
"""
API_webwxgetheadimg = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetheadimg"
API_webwxgetmsgimg = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetmsgimg"
API_webwxgetmedia = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetmedia"
API_webwxgetvideo = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetvideo"
API_webwxgetvoice = f"{API_target}/cgi-bin/mmwebwx-bin/webwxgetvoice"


API_webwxupdatechatroom = f"{API_target}/cgi-bin/mmwebwx-bin/webwxupdatechatroom"
API_webwxcreatechatroom = f"{API_target}/cgi-bin/mmwebwx-bin/webwxcreatechatroom"

# 获取msgid
API_webwxstatusnotify = f"{API_target}/cgi-bin/mmwebwx-bin/webwxstatusnotify"

API_webwxcheckurl = f"{API_target}/cgi-bin/mmwebwx-bin/webwxcheckurl"
API_webwxverifyuser = f"{API_target}/cgi-bin/mmwebwx-bin/webwxverifyuser"
API_webwxfeedback = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsendfeedback"
API_webwxreport = f"{API_target}/cgi-bin/mmwebwx-bin/webwxstatreport"
API_webwxsearch = f"{API_target}/cgi-bin/mmwebwx-bin/webwxsearchcontact"
API_webwxoplog = f"{API_target}/cgi-bin/mmwebwx-bin/webwxoplog"
API_checkupload = f"{API_target}/cgi-bin/mmwebwx-bin/webwxcheckupload"
API_webwxrevokemsg = f"{API_target}/cgi-bin/mmwebwx-bin/webwxrevokemsg"
API_webwxpushloginurl = f"{API_target}/cgi-bin/mmwebwx-bin/webwxpushloginurl"

# -------------------------------------------------------------------------

oplogCmdId = {"TOPCONTACT": 3, "MODREMARKNAME": 2}
SP_CONTACT_FILE_HELPER = "filehelper"
SP_CONTACT_NEWSAPP = "newsapp"
SP_CONTACT_RECOMMEND_HELPER = "fmessage"
CONTACTFLAG_CONTACT = 1
CONTACTFLAG_CHATCONTACT = 2
CONTACTFLAG_CHATROOMCONTACT = 4
CONTACTFLAG_BLACKLISTCONTACT = 8
CONTACTFLAG_DOMAINCONTACT = 16
CONTACTFLAG_HIDECONTACT = 32
CONTACTFLAG_FAVOURCONTACT = 64
CONTACTFLAG_3RDAPPCONTACT = 128
CONTACTFLAG_SNSBLACKLISTCONTACT = 256
CONTACTFLAG_NOTIFYCLOSECONTACT = 512
CONTACTFLAG_TOPCONTACT = 2048
MM_USERATTRVERIFYFALG_BIZ = 1
MM_USERATTRVERIFYFALG_FAMOUS = 2
MM_USERATTRVERIFYFALG_BIZ_BIG = 4
MM_USERATTRVERIFYFALG_BIZ_BRAND = 8
MM_USERATTRVERIFYFALG_BIZ_VERIFIED = 16
MM_DATA_TEXT = 1
MM_DATA_HTML = 2
MM_DATA_IMG = 3
MM_DATA_PRIVATEMSG_TEXT = 11
MM_DATA_PRIVATEMSG_HTML = 12
MM_DATA_PRIVATEMSG_IMG = 13
MM_DATA_VOICEMSG = 34
MM_DATA_PUSHMAIL = 35
MM_DATA_QMSG = 36
MM_DATA_VERIFYMSG = 37
MM_DATA_PUSHSYSTEMMSG = 38
MM_DATA_QQLIXIANMSG_IMG = 39
MM_DATA_POSSIBLEFRIEND_MSG = 40
MM_DATA_SHARECARD = 42
MM_DATA_VIDEO = 43
MM_DATA_VIDEO_IPHONE_EXPORT = 44
MM_DATA_EMOJI = 47
MM_DATA_LOCATION = 48
MM_DATA_APPMSG = 49
MM_DATA_VOIPMSG = 50
MM_DATA_STATUSNOTIFY = 51
MM_DATA_VOIPNOTIFY = 52
MM_DATA_VOIPINVITE = 53
MM_DATA_MICROVIDEO = 62
MM_DATA_SYSNOTICE = 9999
MM_DATA_SYS = 1e4
MM_DATA_RECALLED = 10002
MSGTYPE_TEXT = 1
MSGTYPE_IMAGE = 3
MSGTYPE_VOICE = 34
MSGTYPE_VIDEO = 43
MSGTYPE_MICROVIDEO = 62
MSGTYPE_EMOTICON = 47
MSGTYPE_APP = 49
MSGTYPE_VOIPMSG = 50
MSGTYPE_VOIPNOTIFY = 52
MSGTYPE_VOIPINVITE = 53
MSGTYPE_LOCATION = 48
MSGTYPE_STATUSNOTIFY = 51
MSGTYPE_SYSNOTICE = 9999
MSGTYPE_POSSIBLEFRIEND_MSG = 40
MSGTYPE_VERIFYMSG = 37
MSGTYPE_SHARECARD = 42
MSGTYPE_SYS = 1e4
MSGTYPE_RECALLED = 10002
MSG_SEND_STATUS_READY = 0
MSG_SEND_STATUS_SENDING = 1
MSG_SEND_STATUS_SUCC = 2
MSG_SEND_STATUS_FAIL = 5
APPMSGTYPE_TEXT = 1
APPMSGTYPE_IMG = 2
APPMSGTYPE_AUDIO = 3
APPMSGTYPE_VIDEO = 4
APPMSGTYPE_URL = 5
APPMSGTYPE_ATTACH = 6
APPMSGTYPE_OPEN = 7
APPMSGTYPE_EMOJI = 8
APPMSGTYPE_VOICE_REMIND = 9
APPMSGTYPE_SCAN_GOOD = 10
APPMSGTYPE_GOOD = 13
APPMSGTYPE_EMOTION = 15
APPMSGTYPE_CARD_TICKET = 16
APPMSGTYPE_REALTIME_SHARE_LOCATION = 17
APPMSGTYPE_TRANSFERS = 2e3
APPMSGTYPE_RED_ENVELOPES = 2001
APPMSGTYPE_READER_TYPE = 100001
UPLOAD_MEDIA_TYPE_IMAGE = 1
UPLOAD_MEDIA_TYPE_VIDEO = 2
UPLOAD_MEDIA_TYPE_AUDIO = 3
UPLOAD_MEDIA_TYPE_ATTACHMENT = 4
PROFILE_BITFLAG_NOCHANGE = 0
PROFILE_BITFLAG_CHANGE = 190
CHATROOM_NOTIFY_OPEN = 1
CHATROOM_NOTIFY_CLOSE = 0
StatusNotifyCode_READED = 1
StatusNotifyCode_ENTER_SESSION = 2
StatusNotifyCode_INITED = 3
StatusNotifyCode_SYNC_CONV = 4
StatusNotifyCode_QUIT_SESSION = 5
VERIFYUSER_OPCODE_ADDCONTACT = 1
VERIFYUSER_OPCODE_SENDREQUEST = 2
VERIFYUSER_OPCODE_VERIFYOK = 3
VERIFYUSER_OPCODE_VERIFYREJECT = 4
VERIFYUSER_OPCODE_SENDERREPLY = 5
VERIFYUSER_OPCODE_RECVERREPLY = 6
ADDSCENE_PF_QQ = 4
ADDSCENE_PF_EMAIL = 5
ADDSCENE_PF_CONTACT = 6
ADDSCENE_PF_WEIXIN = 7
ADDSCENE_PF_GROUP = 8
ADDSCENE_PF_UNKNOWN = 9
ADDSCENE_PF_MOBILE = 10
ADDSCENE_PF_WEB = 33
TIMEOUT_SYNC_CHECK = 0
EMOJI_FLAG_GIF = 2
KEYCODE_BACKSPACE = 8
KEYCODE_ENTER = 13
KEYCODE_SHIFT = 16
KEYCODE_ESC = 27
KEYCODE_DELETE = 34
KEYCODE_ARROW_LEFT = 37
KEYCODE_ARROW_UP = 38
KEYCODE_ARROW_RIGHT = 39
KEYCODE_ARROW_DOWN = 40
KEYCODE_NUM2 = 50
KEYCODE_AT = 64
KEYCODE_NUM_ADD = 107
KEYCODE_NUM_MINUS = 109
KEYCODE_ADD = 187
KEYCODE_MINUS = 189
MM_NOTIFY_CLOSE = 0
MM_NOTIFY_OPEN = 1
MM_SOUND_CLOSE = 0
MM_SOUND_OPEN = 1
MM_SEND_FILE_STATUS_QUEUED = 0
MM_SEND_FILE_STATUS_SENDING = 1
MM_SEND_FILE_STATUS_SUCCESS = 2
MM_SEND_FILE_STATUS_FAIL = 3
MM_SEND_FILE_STATUS_CANCEL = 4
MM_EMOTICON_WEB = "_web"


# -------------------------------------------------------------------------
API_checktimeout = 25.04
API_checknums = 5

from webot.common import init_path

YOUR_NAME = "张三"
API_conf_path = init_path("extra/")

API_log_path = init_path(f"{API_conf_path}/log/")  # 聊天记录 markdown
API_static_path = init_path(f"{API_conf_path}/static/")  # 生成的配置文件及实时记录
API_analysis_path = init_path(f"{API_conf_path}/analysis/")  # 各类分析结果及导出数据

API_media_path = init_path(f"{API_conf_path}/meidas/")  # 媒体数据
API_media_icon_path = init_path(f"{API_media_path}/icons/")  # 头像
API_meida_voice_path = init_path(f"{API_media_path}/voices/")  # 语音
API_meida_image_path = init_path(f"{API_media_path}/images/")  # 图片
API_meida_emoji_path = init_path(f"{API_media_path}/emoji/")  # 表情
API_meida_video_path = init_path(f"{API_media_path}/videos/")  # 视频

API_hotreload_file = f"{API_static_path}/wxbot.pkl"
API_qrcode_name = f"{API_static_path}/qrcode.jpg"

Webot_logger_format = "[%(asctime)s] >>> %(levelname)s  %(name)s: %(message)s"

MSG_TYPES = {
    1: "TEXT",
    3: "IMAGE",
    34: "VOICE",
    43: "VIDEO",
    62: "MICROVIDEO",
    47: "EMOTICON",
    49: "APP",
    50: "VOIPMSG",
    52: "VOIPNOTIFY",
    53: "VOIPINVITE",
    48: "LOCATION",
    51: "STATUSNOTIFY",
    9999: "SYSNOTICE",
    40: "POSSIBLEFRIEND_MSG",
    37: "VERIFYMSG",
    42: "SHARECARD",
    10000: "SYS",
    10002: "RECALLED",
}
