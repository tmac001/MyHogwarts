# @Time : 2020-05-05 15:24
import pytest
from wework_test.api.baseapi import BaseApi
from wework_test.api.corp_tag import CorpTag


class TestCropTag:
    file = BaseApi.yaml_load("../../wework_test/testcase/corp_data.yaml")
    step = BaseApi.yaml_load("../../wework_test/testcase/test_corp_tag_step.yaml")
    @classmethod
    def setup_class(cls):
        cls.corp_tag = CorpTag()
        cls.reset()

    def test_get_corp_tag_list(self):
        res = self.corp_tag.get_corp_tag_list()
        print(res)
        # assert res["errmsg"] == "ok"

    def test_get_corp_tag_list_by_yaml(self):
        self.corp_tag.steps_run(self.step["test_get_corp_tag_list"])
    # def test_get_corp_tag_list(self):
    #     res = self.corp_tag.get_corp_tag_list()
    #     print(res)
    #     assert res["errmsg"] == "ok"
    #     # print(BaseApi.jsonpath(res, "$..tag[?(@.name == 'demo1')]"))

    # @pytest.mark.parametrize("name", file["test_add_corp_tag"])
    # def test_add_corp_tag(self, name):
    #     res = self.corp_tag.add_corp_tag(name)
    #     print(res)
    #     assert res["errmsg"] == "ok"
    #     if res["errmsg"] == "ok":
    #         self.corp_tag.delete_corp_tag(name)

    @pytest.mark.parametrize("name", file["test_add_corp_tag"])
    def test_add_corp_tag(self, name):
        res = self.corp_tag.add_corp_tag(name)
        assert res["errmsg"] == "ok"

    @pytest.mark.parametrize("name", file["test_delete_corp_tag"])
    def test_delete_corp_tag(self, name):
        res = self.corp_tag.add_corp_tag(name)
        assert res["errmsg"] == "ok"
        res = self.corp_tag.get_corp_tag_list()
        res = BaseApi.jsonpath(res, f"$..tag[?(@.name == '{name}')]")
        res = self.corp_tag.delete_corp_tag([res[0]['id']])
        print(res)
        assert res["errmsg"] == "ok"

    @classmethod
    def reset(cls):
        if len(cls.corp_tag.get_corp_tag_list()["tag_group"][0]["tag"])>3:
            for name in cls.file["test_add_corp_tag"]:
                res = BaseApi.jsonpath(cls.corp_tag.get_corp_tag_list(), f"$..tag[?(@.name == '{name}')]")
                print(res)
                cls.corp_tag.delete_corp_tag([res[0]['id']])
