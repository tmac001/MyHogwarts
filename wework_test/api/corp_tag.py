# @Time : 2020-05-05 15:19
import requests

from wework_test.api.wework import WeWork


class CorpTag(WeWork):
    secret = "x85J2m6GNgIxrvWEKEOEGDxkHaVPIkykecKe0uCP9EM"

    def __init__(self):
        self.data = self.yaml_load("../../wework_test/api/corp_tag_step.yaml")

    def get_corp_tag_list(self, **kwargs):
        self.param["access_token"] = self.get_token(self.secret)
        req = self.data["get_corp_tag_list"]
        return self.api_send(req)

    def add_corp_tag(self, name):
        self.param["access_token"] = self.get_token(self.secret)
        self.param["name"] = name
        req = self.data["add_corp_tag"]

        return self.api_send(req)

    def delete_corp_tag(self, tag_id=[], group_id=[]):
        body = {
            "tag_id": tag_id,
            "group_id": group_id
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                            params={"access_token": self.get_token(self.secret)},
                            json=body)
        return res.json()
