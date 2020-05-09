# @Time : 2020-05-05 9:50
from wework_test.api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    def test_get_tag_list(self):
        res = self.tag.get_tag_list()
        print(res)
        assert res["errmsg"] == "ok"

    def test_create_tag(self):
        res = self.tag.create_tag("重要", 1)
        print(res)
        assert res["errmsg"] == "created"

    def test_delete_tag(self):
        res = self.tag.delete_tag(1)
        print(res)
        assert res["errmsg"] == "deleted"

    def test_get_tag(self):
        res = self.tag.get_tag(1)
        print(res)

