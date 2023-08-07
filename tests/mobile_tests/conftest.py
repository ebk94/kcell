import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def appium_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android",
        "appPackage": "com.wdiodemoapp",
        "appActivity": "com.wdiodemoapp.MainActivity",
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()