# @Time : 2020-05-04 15:06
import json

import jsonpath as jsonpath
import requests
import yaml


class BaseApi:
    param = {}
    secret = ""

    @classmethod
    def format(cls, r):
        res = json.dumps(json.loads(r), indent=2, ensure_ascii=False)
        print(res)
        # return res

    @classmethod
    def jsonpath(cls, r, expr):
        return jsonpath.jsonpath(r, expr=expr)

    @classmethod
    def yaml_load(cls, path):
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    @classmethod
    def api_send(cls, req):
        # 参数替换
        raw = yaml.safe_dump(req)
        for k, v in cls.param.items():
            raw = raw.replace(f"${{{k}}}", v)
        req = yaml.safe_load(raw)
        res = requests.request(method=req["method"], url=req["url"], params=req["params"], json=req["json"])
        cls.format(res.text)
        return res.json()


if __name__ == '__main__':
    # BaseApi.format(
    # '{"errcode": 0, "errmsg": "搜索"}')
    print(BaseApi.yaml_load("corp_tag_step.yaml"))
