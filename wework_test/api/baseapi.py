# @Time : 2020-05-04 15:06
import json

import jsonpath as jsonpath
import yaml


class BaseApi:
    @classmethod
    def format(cls, r):
        res = json.dumps(json.loads(r), indent=2, ensure_ascii=False)
        print(res)
        return res

    @classmethod
    def jsonpath(cls, r, expr):
        return jsonpath.jsonpath(r, expr=expr)

    @classmethod
    def yaml_load(cls, path) -> dict:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    # BaseApi.format(
    # '{"errcode": 0, "errmsg": "搜索"}')
    print(BaseApi.yaml_load(r"D:\workspace\MyHogwarts\wework_test\testcase\corp_data.yaml"))
