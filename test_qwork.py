import pytest
import yaml
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestWork:
    def setup(self):
        desird_caps = {}
        desird_caps['platformName'] = 'Android'
        desird_caps['platformVersion'] = '6.0'
        desird_caps['deviceName'] = '127.0.0.1：7555'
        desird_caps['appPackage'] = 'com.tencent.wework'
        desird_caps['appActivity'] = '.launch.WwMainActivity'
        desird_caps['noReset'] = 'true'
        # desird_caps['skipDeviceInitialization'] = 'true'
        desird_caps['unicodeKeyboard'] = 'true'  # 输入中文需要设置这个
        desird_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)
        self.driver.implicitly_wait(15)

    '''
    使用yaml 加载文件时，报错 
    "UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 
    in position 17: illegal multibyte sequence"
    需要在open方法中指定编码方式
    '''
    # @pytest.mark.parametrize(("content"), yaml.safe_load(open('./qwork.yaml', encoding='UTF-8')))
    # def test_work(self, content):
    #     # 通过id和text定位到元素
    #     self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dnj' and @text='通讯录']").click()
    #     self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
    #     self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys("zcp")
    #     # 先定位到父元素，然后查找父元素下面的子元素。使用desktop ispector 进行定位
    #     self.driver.find_element_by_xpath(
    #         "//*[@resource-id='com.tencent.wework:id/fh7']/android.widget.RelativeLayout[2]").click()
    #     self.driver.find_element_by_id("com.tencent.wework:id/aaj").click()
    #     try:
    #         self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys(content)
    #         self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()
    #     except NoSuchElementException:
    #         print("输入的内容不能为空！")
    #     time.sleep(3)

    def test_work(self):
        # 通过id和text定位到元素
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dnj' and @text='通讯录']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys("zcp")
        # 先定位到父元素，然后查找父元素下面的子元素。使用desktop ispector 进行定位
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/fh7']/android.widget.RelativeLayout[2]").click()
        self.driver.find_element_by_id("com.tencent.wework:id/aaj").click()
        with open("./qworkdatas.txt", "r",encoding='UTF-8') as f:
            for i in f.readlines():   #readlines 是一个列表
                try:
                    self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys(i)
                    self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()
                except NoSuchElementException:
                    print("输入的内容不能为空！")


        # try:
        #     with open("./qworkdatas.txt","r") as f:
        #         str = f.read()
        #     self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys()
        #     self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()
        # except NoSuchElementException:
        #     print("输入的内容不能为空！")
        time.sleep(3)
    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
