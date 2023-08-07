# from appium.webdriver.common.appiumby import AppiumBy

# class LoginPageMobile:

#     LOGIN_LINK = (AppiumBy.ACCESSIBILITY_ID, 'Login')
#     EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'input-email')
#     PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'input-password')
#     LOGIN_BTN = (AppiumBy.ACCESSIBILITY_ID, 'button-LOGIN')

#     def __init__(self, appium_driver):
#         self.appium_driver = appium_driver

#     def open_login_page(self):
#         self.appium_driver.find_element(LOGIN_LINK).click()
    
#     def enter_email(self, email):
#         self.appium_driver.find_element(EMAIL_INPUT).send_keys(email)