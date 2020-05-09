# @Time : 2020-05-04 15:13
import requests


class WeWork:
    corpid = "ww9bc7cba253d718ce"

    @classmethod
    def get_token(cls, secret):
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params={
            "corpid": cls.corpid,
            "corpsecret": secret
        })
        return res.json()["access_token"]
