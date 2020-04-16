import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueQiu:
    def setup(self):
        desird_cap = {}
        desird_cap['platformName'] = "Android"
        desird_cap['platformVersion'] = "6.0" #网易mumu是6.0
        desird_cap['deviceName'] = "127.0.0.1:7555"
        desird_cap['appPackage'] = "com.xueqiu.android"
        desird_cap['appActivity'] = "com.xueqiu.android.stockmodule.quotecenter.activity.QuoteCenterHotStockListActivity"
        #desird_cap['appActivity'] = "com.xueqiu.android.common.MainActivity"
        desird_cap['noReset'] = True
        #desird_cap['dontStopAppOnReset'] = 'true' 感觉这个参数不好用
        desird_cap['skipDeviceInitialization'] = True  #每次启动，跳过安装、权限设置等操作
        desird_cap['unicodeKeyboard'] = 'true'  #输入中文需要设置这个
        desird_cap['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desird_cap)
        self.driver.implicitly_wait(5)


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
        print(search_element.text)  #查看搜索框name属性值
        print(search_element.location)  #打印坐标

        '''
        上下滑动操作
        '''

    @pytest.mark.skip
    def test_touchOne(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_size() #获取屏幕尺寸
        print(type(window_rect)) # 字典对象
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height*1/5)  # y 坐标的起点是从底部开始，不是顶部
        y_end = int(height*4/5)
        action.press(x=x1,y=y_start).wait(2000).move_to(x=x1,y=y_end).release().perform()

        '''
        手势密码锁
        '''
    @pytest.mark.skip
    def test_touchTwo(self):
        action = TouchAction(self.driver)
        action.press(x=243,y=395).move_to(x=721,y=378).move_to(x=1190,y=364).move_to(x=1202,y=859)\
        .move_to(x=1195,y=1339).release().perform()


    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()