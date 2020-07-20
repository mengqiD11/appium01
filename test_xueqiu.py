import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueQiu:
    def setup(self):
        desird_cap = {}
        desird_cap['platformName'] = "Android"
        desird_cap['platformVersion'] = "6.0"  # 网易mumu是6.0
        desird_cap['deviceName'] = "127.0.0.1:7555"
        desird_cap['appPackage'] = "com.xueqiu.android"
        desird_cap['appActivity'] = "com.xueqiu.android.common.MainActivity"
        # desird_cap['appActivity'] = "com.xueqiu.android.common.MainActivity"
        desird_cap['noReset'] = True
        # desird_cap['dontStopAppOnReset'] = 'true' 感觉这个参数不好用
        # desird_cap['skipDeviceInitialization'] = True  #每次启动，跳过安装、权限设置等操作
        desird_cap['unicodeKeyboard'] = 'true'  # 输入中文需要设置这个
        desird_cap['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desird_cap)
        self.driver.implicitly_wait(5)

    @pytest.mark.skip
    def test_searc(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='阿里巴巴']").click()
        current_price = float(
            self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)  # 取到的是文本值，需要转换下
        assert current_price > 190

    @pytest.mark.skip
    def test_attr(self):
        search_element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_element.is_enabled())  # 查看是否可用
        print(search_element.text)  # 查看搜索框name属性值
        print(search_element.location)  # 打印坐标


        '''
        上下滑动操作
        '''
    def test_touchOne(self):
        # 使用该方法，模拟器没有看出效果
# action = TouchAction(self.driver)
        window_rect = self.driver.get_window_size(windowHandle='current')  # 获取屏幕尺寸,# 字典对象
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)  # y 坐标的起点是从底部开始，不是顶部
        y_end = int(height * 1 / 5)
        # action.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()
        TouchAction(self.driver).long_press(x=x1, y=y_start)\
            .move_to(x=x1, y=y_end).wait(1000).release().perform()


        '''
        手势密码锁
        '''
    @pytest.mark.skip
    def test_touchTwo(self):
        action = TouchAction(self.driver)
        action.press(x=243, y=395).move_to(x=721, y=378).move_to(x=1190, y=364).move_to(x=1202, y=859) \
            .move_to(x=1195, y=1339).release().perform()

    '''
    使用uiSelector进行定位,因为是sdk自带的所以速度比较快，但是编写容易出错
    在首页点击【我的】
    点击登录进入到登录页面
    输入用户名、密码
    点击登录按钮
    '''
    @pytest.mark.skip
    def test_login(self):
        #还可以使用联合定位方式 如 （'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")'),还可以继续追加组合
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click() #使用text属性定位
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()


    #滚动查找
    @pytest.mark.skip
    def test_scrollSearch(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/title_text").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("古树长青").'
                                                        'instance(0));').click()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
