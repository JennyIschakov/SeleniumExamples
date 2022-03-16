from faker import Faker
import datetime
from time import sleep
import random

from prettytable import PrettyTable, prettytable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()



# =================================================== Variables
fake = Faker(locale='en_CA')
divider = '---------------------------------------------------------'

# URLs
home_page_url = 'https://www.farmersedge.ca/'
home_page_title = 'Digital Farming Solutions | Precision Farming | Farmers Edge'

# Random fake variables for form
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'

domain_list = ['gmail.com', 'yahoo.com']
email = f'{first_name}.{last_name}@{random.choice(domain_list)}'

phone = fake.phone_number()

country = fake.country()

# How can we help you today? text box
message = fake.sentence(nb_words=random.randint(1, 30))


# =================================================== Methods


def set_up(scenario_num):
    sleep(2)
    # Navigating to the home page
    driver.get(home_page_url)
    # Make a full screen
    driver.maximize_window()
    # Test started date-time
    print(divider)
    text = f'{scenario_num} started at {datetime.datetime.now()}'
    print(text)
    # Write to log file
    open('log.log', 'a').write(text + '\n')


def test_completed(scenario_num):
    sleep(1)
    # Test completed date-time
    print(divider)
    text = f'{scenario_num} completed at {datetime.datetime.now()}'
    print(text)
    # Write to log file
    open('log.log', 'a').write(text + '\n')
    print(divider)


def check_page_url_title(page_name, url, title):
    print(divider)
    sleep(1)
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == url and driver.title == title:
        print(f'{page_name} --- loaded successfully')
        print(f' <{url}> --- URL is correct')
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
    for option in dropdown_options[1::]: # without first option that shows text to user
        dropdown_list.append(option.text)

    random_choice = random.choice(dropdown_list)
    Select(dropdown).select_by_visible_text(random_choice)
    return random_choice


def contact_us_form():
    sleep(1)
    # =================  Start to fill form =================
    # First & Last Name
    driver.find_element(By.XPATH, '//input[@name="full-name"]').send_keys(full_name)
    # Phone
    driver.find_element(By.XPATH, '//input[@name="phone-number"]').send_keys(phone)
    # Email
    driver.find_element(By.XPATH, '//input[@name="email-address"]').send_keys(email)
    # Country
    driver.find_element(By.XPATH, '//input[@name="country"]').send_keys(country)
    # -- Preferred method of contact -- dropdown
    preferred_contact_method = select_random_dropdown('//select[@name="preferred-time"]')
    # How can we help you today? text box
    driver.find_element(By.XPATH, '//textarea[@name="message"]').send_keys(message)
    # Submit button - without clicking in order not to send for to company
    driver.find_element(By.XPATH, '//input[@value="Submit"]')
    # =================  End to fill form =================

    # Summarize the form
    print(divider)
    text_filled_form = 'Contact US form filled successfully, with following details:'
    print(text_filled_form)
    table = PrettyTable()

    table.field_names = ['Field: Details']
    table.add_rows([
        [f'Full name: {full_name}'],
        [f'Phone number: {phone}'],
        [f'Email: {email}'],
        [f'Country: {country}'],
        [f'Preferred method of contact: {preferred_contact_method}'],
        [f'Message: {message}'],
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
# Description: Contact us via link in header

# Navigate to home page
set_up('Scenario_01')
# Validate home page loading
check_page_url_title('Home page', home_page_url, home_page_title)

# Navigate to Contact Us page
# move mouse to Contact Us menu
ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//a[text() = "Contact Us"]')).perform()
# Click on Contact Us link
driver.find_element(By.XPATH, '//*[@id="menu-item-40865"]/a[text() = "Contact Us"]').click()
# Validate URL and title
check_page_url_title('Contact Us', 'https://www.farmersedge.ca/contact/', 'Contact Us - Farmers Edge')

# Contact US  - fill form
contact_us_form()

# test  completed
test_completed('Scenario_01')

# ===================================================''
# Close browser
if driver is not None:
    driver.close()
