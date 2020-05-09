# @Time : 2020-05-05 15:24
import pytest
from wework_test.api.baseapi import BaseApi
from wework_test.api.corp_tag import CorpTag


class TestCropTag:
    file = BaseApi.yaml_load("../../wework_test/testcase/corp_data.yaml")

    @classmethod
    def setup_class(cls):
        cls.corp_tag = CorpTag()

    def test_get_corp_tag_list(self):
        res = self.corp_tag.get_corp_tag_list()
        print(res)
        assert res["errmsg"] == "ok"
        # print(BaseApi.jsonpath(res, "$..tag[?(@.name == 'demo1')]"))

    @pytest.mark.parametrize("name", file["test_add_corp_tag"])
    def test_add_corp_tag(self, name):
        res = self.corp_tag.add_corp_tag(name)
        print(res)
        assert res["errmsg"] == "ok"
        # 断言通过删除添加数据
        if res["errmsg"] == "ok":
            self.corp_tag.delete_corp_tag(name)

    @pytest.mark.parametrize("name", file["test_delete_corp_tag"])
    def test_delete_corp_tag(self, name):
        res = self.corp_tag.add_corp_tag(name)
        assert res["errmsg"] == "ok"
        res = self.corp_tag.get_corp_tag_list()
        res = BaseApi.jsonpath(res, f"$..tag[?(@.name == '{name}')]")
        res = self.corp_tag.delete_corp_tag([res[0]['id']])
        print(res)
        assert res["errmsg"] == "ok"
