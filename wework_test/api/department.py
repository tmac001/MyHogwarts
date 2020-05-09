# @Time : 2020-05-04 15:33

import requests

from wework_test.api.wework import WeWork


class Department(WeWork):
    secret = "fxeE5d9DAb-JpGW3netzORcHdUf5OlW63fDvSOu9Ic0"

    def department_list(self):
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                           params={"access_token": self.get_token(self.secret)})
        return res.json()

    def create_department(self, name, parentid, **kwargs):
        body = {
            "name": name,
            "parentid": parentid,
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                            params={"access_token": WeWork.get_token(self.secret)}, json=body)
        return res.json()

    def update_department(self, id, **kwargs):
        body = {
            "id": id,
        }
        body.update(kwargs)
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                            params={"access_token": self.get_token(self.secret)}, json=body)
        return res.json()

    def delete_department(self, id, **kwargs):
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                            params={"access_token": self.get_token(self.secret),
                                    "id": id})
        return res.json()
