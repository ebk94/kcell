from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class CommonOps:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self._wait = WebDriverWait(self.browser, 10)
    
    def open(self):
        self.browser.get(self.url)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))
    
    def find(self, locator):
        return self.browser.find_element(*locator)
    
    def is_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))
    
    def is_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))
    
    def scrollTo(self, locator):
        element = self.browser.find_element(*locator)
        actions = ActionChains(self.browser)
        return actions.move_to_element(element).perform()
    
    def check_css_styles(self, locator, css_property):
        time.sleep(1)
        return self._wait.until(EC.visibility_of_element_located(locator)).value_of_css_property(css_property)