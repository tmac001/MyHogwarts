# @Time : 2020-02-15 0:48
from selenium_test.page.import_contacts_page import ImportContactsPage


class TestContacts:
    def setup_method(self):
        self.import_contacts_page = ImportContactsPage(reuse=True)

    def test_import_contacts(self):
        path = r"D:\workspace\MyHogwarts\selenium_test\testcase\通讯录批量导入模板.xlsx"
        self.import_contacts_page.import_contacts(path)
