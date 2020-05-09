# @Time : 2020-05-04 15:25
from wework_test.api.wework import WeWork


class TestWework:
    def setup(self):
        self.wework = WeWork()

    def test_get_token(self):
        res = self.wework.get_token("X3Ti-6RHEf53owDZx18OP75wXpXoIrflvJEvzfKlPrc")
        print(res)
        assert len(res) != 0
