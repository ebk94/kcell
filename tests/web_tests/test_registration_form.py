import pytest
import sys
import os 

from pages.RegistrationPage import RegistrationPage
from pages.locators import FormsPageLocators
import time


baseURL = "https://demoqa.com/automation-practice-form"
file_path = os.getcwd() + '/data/qa-2-min.png'

@pytest.mark.smoke
def test_user_can_register(browser):
    registration_page = RegistrationPage(browser, baseURL)
    registration_page.open()
    registration_page.is_form_visible()
    registration_page.enter_firstname('Test')
    registration_page.enter_lastname('User')
    registration_page.enter_email('admin@admin.ad')
    registration_page.select_gender('Male')
    registration_page.enter_phone('7774577823')
    registration_page.scrollTo(FormsPageLocators.FORM_ADDRESS)
    registration_page.enter_subject('Maths')
    registration_page.check_hobbies('Reading')
    registration_page.upload_file(file_path=file_path)
    registration_page.enter_current_address('Baker Street 221b')
    registration_page.submit_form()

    modal_header = registration_page.wait_for(FormsPageLocators.MODAL_HEADER).text
    assert modal_header == 'Thanks for submitting the form', 'Error in submitting the form'

    registration_page.check_data_is_present('Test User')
    registration_page.check_data_is_present('admin@admin.ad')
    registration_page.check_data_is_present('Male')
    registration_page.check_data_is_present('7774577823')
    registration_page.check_data_is_present('Maths')
    registration_page.check_data_is_present('Reading')
    registration_page.check_data_is_present('qa-2-min.png')
    registration_page.check_data_is_present('Baker Street 221b')
    print('Test passed')
    # Из-за рекламы не получается закрыть модалку
    # registration_page.scrollTo(FormsPageLocators.MODAL_CLOSE_BUTTON)
    # registration_page.close_modal_dialog()

@pytest.mark.smoke
def test_user_can_not_register_with_empty_data(browser):
    registration_page = RegistrationPage(browser, baseURL)
    registration_page.open()
    registration_page.is_form_visible()
    registration_page.submit_form()
    expected_color_code_in_rgb = 'rgb(220, 53, 69)'
    expected_color_code_in_rgba = 'rgba(220, 53, 69, 1)'

    color_code_firstname_field = registration_page.check_css_styles(FormsPageLocators.FORM_FIRSTNAME, 'border-color')
    assert color_code_firstname_field == expected_color_code_in_rgb, 'Got different color code'
    
    color_code_lastname_field = registration_page.check_css_styles(FormsPageLocators.FORM_LASTNAME, 'border-color')
    assert color_code_lastname_field == expected_color_code_in_rgb, 'Got different color code'

    color_code_gender = registration_page.check_css_styles(FormsPageLocators.FORM_GENDER_M, 'color')
    assert color_code_gender == expected_color_code_in_rgba, 'Got different color code'
    
    color_code_phone_field = registration_page.check_css_styles(FormsPageLocators.FORM_FIRSTNAME, 'border-color')
    assert color_code_phone_field == expected_color_code_in_rgb, 'Got different color code'
    
    print('Test passed')   

@pytest.mark.smoke
def test_user_can_not_register_with_wrong_data(browser):
    registration_page = RegistrationPage(browser, baseURL)
    registration_page.open()
    registration_page.is_form_visible()
    registration_page.enter_firstname('John')
    registration_page.enter_lastname('Doe')
    registration_page.enter_email('7874478@784.')
    registration_page.select_gender('Other')
    registration_page.enter_phone('phone number')
    registration_page.scrollTo(FormsPageLocators.FORM_ADDRESS)
    registration_page.enter_subject('English')
    registration_page.check_hobbies('Reading')
    registration_page.check_hobbies('Music')
    registration_page.upload_file(file_path=file_path)
    registration_page.enter_current_address('Baker Street 221b')
    registration_page.submit_form()
    expected_color_code_in_rgb = 'rgb(220, 53, 69)'

    color_code_firstname_field = registration_page.check_css_styles(FormsPageLocators.FORM_EMAIL, 'border-color')
    assert color_code_firstname_field == expected_color_code_in_rgb, 'Got different color code'
    
    color_code_phone_field = registration_page.check_css_styles(FormsPageLocators.FORM_MOBILE_NUMBER, 'border-color')
    assert color_code_phone_field == expected_color_code_in_rgb, 'Got different color code'

    print('Test passed')
