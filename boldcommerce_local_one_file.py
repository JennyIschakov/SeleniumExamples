from faker import Faker
import datetime
from time import sleep
import random

# please run on cmd the following command >> pip install prettytable
from prettytable import PrettyTable, prettytable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


# Local driver
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')


# =================================================== Variables
fake = Faker(locale='en_CA')
divider = '---------------------------------------------------------'

# URLs
home_page_url = 'https://boldcommerce.com/'

# Random fake variables for form
first_name = fake.first_name()
last_name = fake.last_name()

domain_list = ['gmail.com', 'yahoo.com']
email = f'{first_name}.{last_name}@{random.choice(domain_list)}'

phone = fake.phone_number()

company_name = fake.sentence(nb_words=1).replace(".", "")
url_ends = ['.com', '.ca']
company_web = f'{company_name}{random.choice(url_ends)}'


# =================================================== Methods


def set_up():
    sleep(2)
    # Navigating to the home page
    driver.get(home_page_url)
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
    open('log.log', 'a').write(text + '\n')


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
    driver.find_element(By.XPATH, '//input[starts-with(@id,"email")]').send_keys(email)
    # First name
    sleep(1)
    filled_first_name = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"firstname")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"firstname")]').send_keys(first_name)
        filled_first_name = first_name
    # Last name
    sleep(1)
    filled_last_name = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"lastname")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"lastname")]').send_keys(last_name)
        filled_last_name = last_name
    # Phone number
    sleep(1)
    filled_phone = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"phone")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"phone")]').send_keys(phone)
        filled_phone = phone
    # Company name
    sleep(1)
    filled_company_name = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"company")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"company")]').send_keys(company_name)
        filled_company_name = company_name
    # Website URL
    sleep(1)
    filled_company_web = '-'
    if driver.find_element(By.XPATH, '//input[starts-with(@id,"website")]').is_displayed():
        driver.find_element(By.XPATH, '//input[starts-with(@id,"website")]').send_keys(company_web)
        filled_company_web = company_web

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
        [f'Email: {email}'],
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

    # Write form to log file
    open('log.log', 'a').write(text_filled_form + '\n')
    with open('log.log', 'a') as w:
        w.write(str(table))
    open('log.log', 'a').write('\n')


# =================================================== Running tests

# ---------------------------------- Scenario_01
# Description: Contact Sales via button on right side

# Navigate to home page
set_up()
# Validate home page loading
check_page_url_title('Home page', home_page_url, 'Bold Commerce | Modular Commerce Solutions - Sell Anywhere')

print(divider)
print('Scenario_01 started')
# Navigate to contact sales form
driver.find_element(By.XPATH, '//a[text() = "Contact Sales" and contains(@class,"omninav-cta")]').click()
# Validate URL and title
check_page_url_title('Contact Sales', 'https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

# Contact sales - fill form
contact_sales_form()
# test  completed
test_completed('Scenario_01')

# ---------------------------------- Scenario_02
# Description: Contact Sales via second button on middle

# Navigating to the home page
driver.get(home_page_url)

sleep(1)
print(divider)
print('Scenario_02 started')
# Navigate to contact sales form
driver.find_element(By.XPATH, '//div[contains(@class, "hero__content")]/a[text() = "Contact Sales"]').click()
# Validate URL and title
check_page_url_title('Contact Sales', 'https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

# Contact sales - fill form
contact_sales_form()

# test  completed
test_completed('Scenario_02')


# ---------------------------------- Scenario_03
# Description: Contact Sales via third button almost in bottom

# Navigating to the home page
driver.get(home_page_url)

sleep(1)
print(divider)
print('Scenario_03 started')
# Navigate to contact sales form
driver.find_element(By.XPATH, '//div[contains(@class, "cta-block__actions")]/a[text() = "Contact Sales"]').click()
# Validate URL and title
check_page_url_title('Contact Sales', 'https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

# Contact sales - fill form
contact_sales_form()

# test  completed
test_completed('Scenario_03')


# ---------------------------------- Scenario_04
# Description: Contact Sales via fourth button in header

# Navigating to the home page
driver.get(home_page_url)

print(divider)
print('Scenario_04 started')
# Go down + a little bit up >> in order Contact Sales will appear in header
# Scroll down till bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# Go up to <h2>Bold insights for the future of ecommerce</h2>
element = driver.find_element(By.XPATH, '//h2[text() = "Bold insights for the future of ecommerce"]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()

sleep(1)
# Navigate to contact sales form
driver.find_element(By.XPATH, '//a[text() = "Contact Sales" and contains(@class,"btn-outline-light")]').click()

# Validate URL and title
check_page_url_title('Contact Sales','https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

# Contact sales - fill form
contact_sales_form()

# test  completed
test_completed('Scenario_04')


# ===================================================''
# Close browser
if driver is not None:
    driver.close()
