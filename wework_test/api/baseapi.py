# @Time : 2020-05-04 15:06
import json
import jsonpath
import requests
import yaml


class BaseApi:
    # 需要替换的参数
    param = {}
    # 每个应用独立的密钥，通过子类赋值
    secret = ""

    @classmethod
    def format(cls, r):
        res = json.dumps(json.loads(r), indent=2, ensure_ascii=False)
        print(res)

    @classmethod
    def jsonpath(cls, r, expr):
        return jsonpath.jsonpath(r, expr=expr)

    @classmethod
    def yaml_load(cls, path):
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    # 业务逻辑驱动
    @classmethod
    def api_send(cls, req):
        # 参数替换
        raw = yaml.safe_dump(req)
        for k, v in cls.param.items():
            raw = raw.replace(f"${{{k}}}", v)
        req = yaml.safe_load(raw)

        # 发起请求
        res = requests.request(method=req["method"], url=req["url"], params=req["params"], json=req["json"])
        cls.format(res.text)
        return res.json()

    #  测试用例步骤驱动
    def steps_run(self, req: list):
        res = None
        for r in req:
            if isinstance(r, dict):
                if "method" in r.keys():
                    res = getattr(self, r.get("method"))()
                if "assertion" in r.keys():
                    assert res[r.get("assertion")[0]] == r.get("assertion")[1]
                # todo 复杂用例，以及需要参数替换的用例的驱动封装


if __name__ == '__main__':
    # BaseApi.format(
    # '{"errcode": 0, "errmsg": "搜索"}')
    print(json.dumps(BaseApi.yaml_load("corp_tag_step.yaml")))
