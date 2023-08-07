from selenium.webdriver.common.by import By

class FormsPageLocators:
    REGISTRATION_FORM = (By.ID, "userForm")
    FORM_FIRSTNAME = (By.ID, "firstName")
    FORM_LASTNAME = (By.ID, "lastName")
    FORM_EMAIL = (By.ID, "userEmail")
    FORM_GENDER_M = (By.XPATH, "//label[contains(., 'Male')]")
    FORM_GENDER_F = (By.XPATH, "//label[contains(., 'Female')]")
    FORM_GENDER_O = (By.XPATH, "//label[contains(., 'Other')]")
    FORM_MOBILE_NUMBER = (By.ID, "userNumber")
    FORM_SUBJECTS = (By.ID, "subjectsInput")
    FORM_FILE = (By.ID, "uploadPicture")
    FORM_ADDRESS = (By.ID, "currentAddress")
    FORM_STATE = (By.XPATH, "//div[@id='stateCity-wrapper']/div/div[contains(., 'Select State')]")
    MODAL_HEADER = (By.CLASS_NAME, "modal-header")
    MODAL_CLOSE_BUTTON = (By.ID, "closeLargeModal")