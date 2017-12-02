# coding:utf-8

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib
import xmltodict
import time
import tornado.gen
import json
import os

from tornado.web import RequestHandler
from tornado.options import options, define
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

# 测试号
# WECHAT_TOKEN = "damon"
# WECHAT_APP_ID = "wx8cf20b7f73705559"
# WECHAT_APP_SECRET = "174ce3922b489a2ed68faf889ddb276e"


WECHAT_TOKEN = "damon"
WECHAT_APP_ID = "wx59e4657b59d640f6"
WECHAT_APP_SECRET = "fd677ca5c4d61482bae31bd0f8824fd4"

define("port", default=80, type=int, help="")

class AccessToken(object):
    """access_token辅助类"""
    _access_token = None
    _create_time = 0
    _expires_in = 0

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/cgi-bin/token?" \
        "grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APP_ID, WECHAT_APP_SECRET)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body)
        if "errcode" in dict_data:
            raise Exception("wechat server error")
        else:
            cls._access_token = dict_data["access_token"]
            cls._expires_in = dict_data["expires_in"]
            cls._create_time = time.time()


    @classmethod
    @tornado.gen.coroutine
    def get_access_token(cls):
        if time.time() - cls._create_time > (cls._expires_in - 200):
            # 向微信服务器请求access_token
            yield cls.update_access_token()
            raise tornado.gen.Return(cls._access_token)
        else:
            raise tornado.gen.Return(cls._access_token)


class WechatHandler(RequestHandler):
    """对接微信服务器"""
    def prepare(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp = "".join(tmp)
        real_signature = hashlib.sha1(tmp).hexdigest()
        if signature != real_signature:
            self.send_error(403)

    def get(self):
        echostr = self.get_argument("echostr")
        self.write(echostr)

    def post(self):
        xml_data = self.request.body
        dict_data = xmltodict.parse(xml_data)
        msg_type = dict_data["xml"]["MsgType"]
        if msg_type == "text":
            content = dict_data["xml"]["Content"]
            """
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>12345678</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[你好]]></Content>
</xml>
"""
            resp_data = {
                "xml":{
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": content,
                    #"Content": "收到的是u文字图片",
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == 'image':
            PicUrl = dict_data["xml"]["PicUrl"]
            MediaId= dict_data["xml"]["MediaId"]
            """
<xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName>
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[image]]></MsgType>
 <PicUrl><![CDATA[this is a url]]></PicUrl>
 <MediaId><![CDATA[media_id]]></MediaId>
 <MsgId>1234567890123456</MsgId>
 </xml>
"""
            resp_data = {
                "xml": {
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "image",
                    "PicUrl": "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=1&spn=0&di=53170758850&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=49366202%2C632101467&os=3303681949%2C3335890514&simid=3365052636%2C338127663&adpicid=0&lpn=0&ln=1942&fr=&fmq=1512195470962_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic4.nipic.com%2F20091217%2F3885730_124701000519_2.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bgtrtv_z%26e3Bv54AzdH3Ffi5oAzdH3FnAzdH3F8alAzdH3Fnlwnldjwlwuw8j0k_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0",
                    "MediaId": MediaId,
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == 'voice':
            MediaId = dict_data["xml"]["MediaId"]
            Format = dict_data["xml"]["Format"]
            '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[voice]]></MsgType>
<MediaId><![CDATA[media_id]]></MediaId>
<Format><![CDATA[Format]]></Format>
<MsgId>1234567890123456</MsgId>
</xml>
            '''
            resp_data = {
                "xml": {
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "image",
                    "MediaId": MediaId,
                    "Format" : Format,
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == 'video':
            MediaId = dict_data["xml"]["MediaId"]
            ThumbMediaId = dict_data["xml"]["ThumbMediaId"]
            '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[video]]></MsgType>
<MediaId><![CDATA[media_id]]></MediaId>
<ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
<MsgId>1234567890123456</MsgId>
</xml
            '''
            resp_data = {
                "xml": {
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "image",
                    "MediaId": MediaId,
                    "ThumbMediaId": ThumbMediaId,
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == 'location':
            MediaId = dict_data["xml"]["MediaId"]
            ThumbMediaId = dict_data["xml"]["ThumbMediaId"]
            '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[location]]></MsgType>
<Location_X>23.134521</Location_X>
<Location_Y>113.358803</Location_Y>
<Scale>20</Scale>
<Label><![CDATA[位置信息]]></Label>
<MsgId>1234567890123456</MsgId>
</xml>
            '''
            resp_data = {
                "xml": {
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "image",
                    "MediaId": MediaId,
                    "ThumbMediaId": ThumbMediaId,
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == "event":
            if dict_data["xml"]["Event"] == "subscribe":
                """用户关注的事件"""
                resp_data = {
                    "xml": {
                        "ToUserName": dict_data["xml"]["FromUserName"],
                        "FromUserName": dict_data["xml"]["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": u"您来啦，笑而不语",
                    }
                }
                if "EventKey" in dict_data["xml"]:
                    event_key = dict_data["xml"]["EventKey"]
                    scene_id = event_key[8:]
                    resp_data["xml"]["Content"] = u"您来啦，笑而不语%s次" % scene_id
                self.write(xmltodict.unparse(resp_data))
            elif dict_data["xml"]["Event"] == "SCAN":
               scene_id = dict_data["xml"]["EventKey"]
               resp_data = {
                   "xml": {
                       "ToUserName": dict_data["xml"]["FromUserName"],
                       "FromUserName": dict_data["xml"]["ToUserName"],
                       "CreateTime": int(time.time()),
                       "MsgType": "text",
                       "Content": u"您扫描的是%s" % scene_id,
                   }
               }
               self.write(xmltodict.unparse(resp_data))
        else:
            resp_data = {
                "xml": {
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "I love itcast",
                }
            }
            self.write(xmltodict.unparse(resp_data))


class QrcodeHandler(RequestHandler):
    """请求微信服务器生成带参数二维码返回给客户"""
    @tornado.gen.coroutine
    def get(self):
        scene_id = self.get_argument("sid")
        try:
            access_token = yield AccessToken.get_access_token()
        except Exception as e:
            self.write("errmsg: %s" % e)
        else:
            client = AsyncHTTPClient()
            url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
            req_data = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": scene_id}}}
            req = HTTPRequest(
                url=url,
                method="POST",
                body=json.dumps(req_data)
            )
            resp = yield client.fetch(req)
            dict_data = json.loads(resp.body)
            if "errcode" in dict_data:
                self.write("errmsg: get qrcode failed")
            else:
                ticket = dict_data["ticket"]
                qrcode_url = dict_data["url"]
                self.write('<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s"><br/>' % ticket)
                self.write('<p>%s</p>' % qrcode_url)


class ProfileHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        code = self.get_argument("code")
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
                "appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (WECHAT_APP_ID, WECHAT_APP_SECRET, code)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body)
        if "errcode" in dict_data:
            self.write("error occur")
        else:
            access_toke = dict_data["access_token"]
            open_id = dict_data["openid"]
            url = "https://api.weixin.qq.com/sns/userinfo?" \
                  "access_token=%s&openid=%s&lang=zh_CN" % (access_toke, open_id)
            resp = yield client.fetch(url)
            user_data = json.loads(resp.body)
            if "errcode" in user_data:
                self.write("error occur again")
            else:
                self.render("index.html", user=user_data)

"""
用户最终访问的URL
https://open.weixin.qq.com/connect/oauth2/authorize?
appid=wx36766f74dbfeef15&redirect_uri=http%3A//www.idehai.com/wechat8000/profile&response_type=code&scope=snsapi_userinfo
&state=1#wechat_redirect
"""


class MenuHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        try:
            access_token = yield AccessToken.get_access_token()
        except Exception as e:
            self.write("errmsg: %s" % e)
        else:
            client = AsyncHTTPClient()
            url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token
            menu = {
                "button": [
                    {
                        "type": "view",
                        "name": "我的主页",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx36766f74dbfeef15&redirect_uri=http%3A//www.idehai.com/root/profile&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect"
                    }
                ]
            }
            req = HTTPRequest(
                url=url,
                method="POST",
                body=json.dumps(menu, ensure_ascii=False)
            )
            resp = yield client.fetch(req)
            dict_data = json.loads(resp.body)
            if dict_data["errcode"] == 0:
                self.write("OK")
            else:
                self.write("failed")


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/root", WechatHandler),
            (r"/root/qrcode", QrcodeHandler),
            (r"/root/profile", ProfileHandler),
            (r"/menu", MenuHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "template")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()