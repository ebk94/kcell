from .common import CommonOps
from .locators import FormsPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class RegistrationPage(CommonOps):

    def is_form_visible(self):
        self.is_visible(FormsPageLocators.REGISTRATION_FORM)

    def enter_firstname(self, firstname):
        self.wait_for(FormsPageLocators.FORM_FIRSTNAME).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.wait_for(FormsPageLocators.FORM_LASTNAME).send_keys(lastname)

    def enter_email(self, email):
        self.wait_for(FormsPageLocators.FORM_EMAIL).send_keys(email)

    def enter_phone(self, phone):
        self.wait_for(FormsPageLocators.FORM_MOBILE_NUMBER).send_keys(phone)
    
    def select_gender(self, gender):
        match gender:
            case 'Male':
                self.find(FormsPageLocators.FORM_GENDER_M).click()
            case 'Female':
                self.find(FormsPageLocators.FORM_GENDER_F).click()
            case 'Other':
                self.find(FormsPageLocators.FORM_GENDER_O).click()

    def select_date(self):
        pass

    def enter_subject(self, subject):
        self.wait_for(FormsPageLocators.FORM_SUBJECTS).send_keys(subject)
        self.wait_for(FormsPageLocators.FORM_SUBJECTS).send_keys(Keys.ENTER)
    
    def check_hobbies(self, hobby):
        self.wait_for((By.XPATH, f"//label[contains(., '{hobby}')]")).click()
    
    def upload_file(self, file_path):
        self.find(FormsPageLocators.FORM_FILE).send_keys(file_path)

    def enter_current_address(self, address):
        self.wait_for(FormsPageLocators.FORM_ADDRESS).send_keys(address)

    def submit_form(self):
        self.wait_for(FormsPageLocators.FORM_SUBJECTS).send_keys(Keys.ENTER)
    
    def enter_state(self, state):
        self.wait_for(FormsPageLocators.FORM_STATE).send_keys(state)
        self.wait_for(FormsPageLocators.FORM_STATE).send_keys(Keys.ENTER)

    def check_data_is_present(self, data):
        try:
            self.find((By.XPATH, f"//td[contains(., '{data}')]"))
            print("The element exists.")
        except NoSuchElementException:
            print("The element does not exist.")
    
    def close_modal_dialog(self):
        self.find(FormsPageLocators.MODAL_CLOSE_BUTTON).click()