import pytest
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.usefixtures("appium_driver")
def test_app_launch(appium_driver):
    login_link = appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Login')
    assert login_link.is_displayed()
    login_link.click()
    
    email_input = appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'input-email')
    email_input.send_keys('admin@admin.ad')

    password_input = appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'input-password')
    password_input.send_keys('admin1234')

    login_btn = appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'button-LOGIN')
    login_btn.click()

    alert_message = appium_driver.find_element(AppiumBy.ID, 'android:id/message')
    alert_title = appium_driver.find_element(AppiumBy.ID,"android:id/alertTitle")
    content_view = appium_driver.find_element(AppiumBy.ID,"android:id/content")

    assert content_view.is_displayed()
    assert alert_title.text == 'Success'
    assert alert_message.text == 'You are logged in!'

