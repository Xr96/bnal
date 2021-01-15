from Utils.driver import Driver
from Utils.page import Page
import pytest
from Utils.data import Date
import logging
def value():
    lis = []
    bnal = Date.get_json_data("bnal.json")
    for i in bnal:
        lis.append((i.get("name"),i.get("passwd"),i.get("exp"),i.get("tag"),i.get("desc")))

    return lis

class TestBNAL:
    def setup_class(self):
        # 关闭更新
        Page.get_home().close_alert()

    def setup(self):
        # 点击我
        Page.get_home().goto_sign()
        # 点击已有账号
        Page.get_sign().goto_login()

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    @pytest.mark.parametrize("name, passwd, exp,tag,desc",value())
    def test_login(self, name, passwd, exp, tag,desc):
        logging.info(f"\t----当前执行用例：{desc}----")
        """

        :param name: 账号
        :param passwd: 密码
        :param exp: 预期结果
        :param tag: 有值 代表是预期失败用例
        :return:
        """
        # 登录操作
        Page.get_login().login(name, passwd)
        # 判断正向用例
        if not tag:
            # 断言用户名
            assert exp == Page.get_person().get_username()
            # 点击设置
            Page.get_person().setting_btn()
            # 退出
            Page.get_setting().logout()
        else:  # 逆向用例
            # 断言 toast消息
            assert Page.get_login().lh.toast_message(exp)

            # 关闭登陆页面
            Page.get_login().close_login()

