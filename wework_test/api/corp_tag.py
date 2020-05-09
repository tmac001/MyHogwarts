# @Time : 2020-05-05 15:19
import requests

from wework_test.api.wework import WeWork


class CorpTag(WeWork):
    secret = "x85J2m6GNgIxrvWEKEOEGDxkHaVPIkykecKe0uCP9EM"

    def get_corp_tag_list(self):
        body = {
            "tag_id": []
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                            params={"access_token": self.get_token(self.secret)},
                            json=body)
        return res.json()

    def add_corp_tag(self, name):
        body = {
            'group_id': 'etriOXEQAAs5K82yxs0sGBXoHRc2N6lg',
            "tag": [{
                "name": name,
            },
            ]
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                            params={"access_token": self.get_token(self.secret)},
                            json=body)
        return res.json()

    def delete_corp_tag(self, tag_id=[], group_id=[]):
        body = {
            "tag_id": tag_id,
            "group_id": group_id
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                            params={"access_token": self.get_token(self.secret)},
                            json=body)
        return res.json()
