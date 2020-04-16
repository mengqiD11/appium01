import time

from appium import webdriver

descri_cap = {

    "platformName" : "Android",
    "deviceName" : "127.0.0.1：7555",
    "appPackage" : "com.xueqiu.android",
    "appActivity" : ".view.WelcomeActivityAlias",
    # 为了使每次重新启用app不会清除app里面的数据，设置noreset  =  true
     "noReset" : True,
     "unicodeKeyboard": True,
     "resetKeyboard": True,
    #不停止app的情况下对app进行调试和运行
     #"dontStopAppOnReset" : True,
    #每次启动，跳过安装、权限设置等操作
    "skipDeviceInitialization": True

}

driver = webdriver.Remote('http://localhost:4723/wd/hub',descri_cap)

driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
time.sleep(10)
# driver.find_element_by_id("com.xueqiu.android:id/name").click()
driver.back()
driver.back()

driver.quit()