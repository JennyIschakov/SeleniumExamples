from faker import Faker
import datetime
from time import sleep
import random

# please run on cmd/shell the following command >> pip install prettytable
from prettytable import PrettyTable, prettytable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options

import boldcommerce_locators as locators
# ================================================= Driver

# driver - headless cloud running
# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1400,1500")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(options=options)

# driver - local running
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

action = ActionChains(driver)

divider = '---------------------------------------------------------'

# =================================================== Methods


def set_up():
    sleep(2)
    # Navigating to the home page
    driver.get(locators.home_page_url)
    # Make a full screen
    driver.maximize_window()
    # Accept necessary cookies
    driver.find_element(By.ID, 'hs-eu-cookie-settings-button').click()
    driver.find_element(By.ID, 'hs-modal-save-settings').click()


def test_completed(scenario_num):
    sleep(1)
    print(divider)
    text = f'{scenario_num} completed at {datetime.datetime.now()}'
    print(text)


def check_page_url_title(page_name, url, title):
    print(divider)
    sleep(1)
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == url and driver.title == title:
        print(f'{page_name} --- loaded successfully')
        print(f'<{url}> --- URL is correct')
        print(f'<{title}> --- title is correct')
    else:
        print(f'=== Page URL <{url}> --- not loaded successfully. Check your code ===')
        driver.close()
        driver.quit()


def select_random_dropdown(xpath):
    sleep(1)
    dropdown = driver.find_element(By.XPATH, xpath)
    dropdown.click()
    dropdown_options = Select(dropdown).options
    dropdown_list = []
    for option in dropdown_options:
        if option.text != 'Please Select':
            dropdown_list.append(option.text)

    random_choice = random.choice(dropdown_list)
    Select(dropdown).select_by_visible_text(random_choice)
    return random_choice


# This form is for any option Contact Sales
# On some pages the following variables are not appear:
# First name/Last name/Phone/Company name/Company url
# So them under if statement - fill field only if appear
def contact_sales_form(): # Contact Sales button - on right side
    sleep(1)

    # =================  Start to fill form =================
    sleep(1)
    # Email
    driver.find_element(By.XPATH, '//input[starts-with(@id,"email")]').send_keys(locators.email)
    # First name
    sleep(1)
    filled_first_name = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"firstname")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"firstname")]').send_keys(locators.first_name)
        filled_first_name = locators.first_name
    # Last name
    sleep(1)
    filled_last_name = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"lastname")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"lastname")]').send_keys(locators.last_name)
        filled_last_name = locators.last_name
    # Phone number
    sleep(1)
    filled_phone = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"phone")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"phone")]').send_keys(locators.phone)
        filled_phone = locators.phone
    # Company name
    sleep(1)
    filled_company_name = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"company")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"company")]').send_keys(locators.company_name)
        filled_company_name = locators.company_name
    # Website URL
    sleep(1)
    filled_company_web = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"website")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"website")]').send_keys(locators.company_web)
        filled_company_web = locators.company_web

    # Business type dropdown
    sleep(1)
    selected_business_type = select_random_dropdown('//select[starts-with(@id,"contact_type")]')

    if selected_business_type == 'Brand/Retailer':
        # eCommerce platform dropdown
        selected_ecommerce_platform = select_random_dropdown('//select[starts-with(@id,"ecommerce_platform")]')
        # Approximate annual revenue dropdown
        selected_annual_revenue = select_random_dropdown('//select[starts-with(@id,"annual_revenue")]')
    else:
        selected_ecommerce_platform = '-'
        selected_annual_revenue = '-'

    # =================  End to fill form =================

    # Accept I agree to receive communications from Bold Commerce
    driver.find_element(By.XPATH, '//input[starts-with(@id, "LEGAL_CONSENT.subscription")]').click()
    # Contact Bold Commerce button
    # without clicking, in order not to send request to the company
    assert driver.find_element(By.XPATH, '//input[contains(@value, "Contact Bold Commerce")]')

    # Summarize the form
    print(divider)
    text_filled_form = 'Contact Sales form filled successfully, with following details:'
    print(text_filled_form)

    table = PrettyTable()
    table.field_names = ['Field: Details']

    table.add_rows([
        [f'Email: {locators.email}'],
        [f'First name: {filled_first_name}'],
        [f'Last name: {filled_last_name}'],
        [f'Phone number: {filled_phone}'],
        [f'Company name: {filled_company_name}'],
        [f'Website URL: {filled_company_web}'],
        [f'Business type: {selected_business_type}'],
        [f'eCommerce platform: {selected_ecommerce_platform}'],
        [f'Approximate annual revenue: {selected_annual_revenue}'],
    ])

    table.vrules = prettytable.NONE
    table.align = 'l'
    # Print form to console
    print(table)