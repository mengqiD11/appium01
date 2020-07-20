import pytest
import yaml
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWork:
    '''
    为了添加多个用户时，不用每次都重新启动app，可以在setup_class中初始化driver
    '''
    def setup_class(self):
        desird_caps = {}
        desird_caps['platformName'] = 'Android'
        desird_caps['platformVersion'] = '6.0'
        desird_caps['deviceName'] = '127.0.0.1：7555'
        desird_caps['appPackage'] = 'com.tencent.wework'
        desird_caps['appActivity'] = '.launch.WwMainActivity'
        # desird_caps['automationName'] = 'Uiautomator2' 如果要获取toast信息，需要使用Uiautomator2引擎，默认是这个所以不用写
        desird_caps['noReset'] = 'true'
        # desird_caps['skipDeviceInitialization'] = 'true'
        desird_caps['unicodeKeyboard'] = 'true'  # 输入中文需要设置这个
        desird_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)
        self.driver.implicitly_wait(15)

    '''
    由于每次添加完，都需要返回通讯录页面，才能开始添加操作，所以需要在teardown中为每个方法添加返回操作，除了teardown外
    还可以使用fixture中的yield中实现
    '''
    @pytest.fixture()
    def add_fixture(self):
        yield
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gpp").click()


    # 添加成员
    @pytest.mark.parametrize("name,gender,mobileNum",[("测试027","女","13400000019")])
    def test_addNmus(self,add_fixture,name,gender,mobileNum):
        # 点击通讯录，这里可以使用MobileBy,也可以使用By，因为mobileBy继承了By，并进行了扩展
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 如果通讯录列表比较长，需要滚动查找
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        # 点击手动输入按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c56").click()
        locator = (MobileBy.XPATH, "//*[contains(@text,'姓名')]")
        # 显示等待姓名tab页签能够显示时，才往下执行，每隔0.5秒对条件进行检查，如果超过10秒则抛出异常
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(name)
        # 选择性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@resource-id='com.tencent.wework:id/ate']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/b84']/android.widget.RelativeLayout[1]").click()
        else:
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/b84']/android.widget.RelativeLayout[2]").click()
        # 输入手机号码
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(mobileNum)
        # 点击保存按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        # while True:
        #     print(self.driver.page_source)
        #     time.sleep(0.5)
        # 打印pagesource，获取toast信息
        time.sleep(2)
        print(self.driver.page_source)
        time.sleep(2)
        toast_loc = '//*[contains(@text,"添加成功")]'
        try:
            WebDriverWait(self.driver, 5, 0.01).until(
                expected_conditions.visibility_of_element_located(MobileBy.XPATH, toast_loc))
            print(self.driver.find_element_by_xpath(toast_loc).text)
        except:
            print('没有获取到toast信息')

    #循环删除通讯录成员
    @pytest.mark.parametrize("name", ["测试001", "测试002", "测试003", "测试004", "测试005", "测试006", "测试007",
                                      "测试008", "测试009", "测试010", "测试011", "测试012", "测试013", "测试014",
                                      "测试015", "测试016", "测试017", "测试018", "测试023", "测试020", "测试021",
                                      "测试022", "测试024", "测试025"])
    @pytest.mark.skip
    def test_delNum(self,name):
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 点击要删除的人员
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']").click()
        # 点击右上角的三个点
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq0").click()
        # 点击编辑成员
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/axr").click()
        # 点击删除按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/drk").click()
        # 确定删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b89").click()
        time.sleep(2)

        member_elem = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        assert len(member_elem) == 0

    #删除通讯录所有成员
    @pytest.mark.parametrize("name",["测试001","测试002","测试003","测试004","测试005","测试006","测试007",
                                     "测试008","测试009","测试010","测试011","测试012","测试013","测试014",
                                     "测试015","测试016","测试017","测试018","测试023","测试020","测试021",
                                     "测试022","测试024","测试025"])
    @pytest.mark.skip
    def test_delAll(self,name):
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 获取通讯录列表
        # elems = self.driver.find_elements(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ayd']/android.widget.RelativeLayout")
        # print(len(elems))
        # for i in range(1,len(elems),1):
        #     print()
        #点击要删除的人员
        self.driver.find_element(MobileBy.XPATH,f"//*[@text='{name}']").click()
        #点击右上角的三个点
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gq0").click()
        #点击编辑成员
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/axr").click()
        #点击删除按钮
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/drk").click()
        #确定删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b89").click()

        member_elem = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        assert len(member_elem) == 0



    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
