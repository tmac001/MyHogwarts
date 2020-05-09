# @Time : 2020-05-05 9:38
import requests

from wework_test.api.wework import WeWork


class Tag(WeWork):
    secret = "x85J2m6GNgIxrvWEKEOEGDxkHaVPIkykecKe0uCP9EM"

    def get_tag_list(self):
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list",
                           params={"access_token": self.get_token(self.secret)})
        return res.json()

    def get_tag(self, tagid):
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/get",
                           params={"access_token": self.get_token(self.secret),
                                   "tagid": tagid})
        return res.json()

    def create_tag(self, tagname, tagid, **kwargs):
        body = {
            "tagname": tagname,
            "tagid": tagid
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create",
                            params={"access_token": self.get_token(self.secret)},
                            json=body)
        return res.json()

    def update_tag(self, tagid, tagname, **kwargs):
        body = {
            "tagname": tagname,
            "tagid": tagid
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/update",
                            params={"access_token": self.get_token(self.secret)},
                            json=body)
        return res.json()

    def delete_tag(self, tagid):
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
                           params={"access_token": self.get_token(self.secret),
                                   "tagid": tagid})
        return res.json()
