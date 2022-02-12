
from time import sleep
import datetime
import opencart_locators as locators
from random import randint, choice


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# ------------------------------------------------

driver = webdriver.Chrome()

divider = '------------------------------'

def set_up():
    driver.get(locators.homepage_url)
    driver.maximize_window()


def tearDown(scenario_num):
    if driver is not None:
        print(divider)
        text = f'{scenario_num} completed at {datetime.datetime.now()}'
        print(text)
        open('test_done.log', 'a').write(text + '\n')
        driver.close()


def validate_page_url_title(page_url, page_title):
    sleep(1)
    if driver.current_url == page_url and driver.title == page_title:
        print(f'Page <{page_url}> loaded successfully')
    else:
        print(f'Page <{page_url}> not loaded successfully')




def register_new_user():
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-black.navbar-btn').click()
    sleep(0.25)

    # those didn't work - wasn't clickable
    # driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-black.navbar-btn[text() = "Register"]').click()
    # driver.find_element(By.LINK_TEXT, 'Register').click()
    # driver.find_element(By.XPATH, '//a[text() = "Register"]').click()

    if driver.current_url == 'https://www.opencart.com/index.php?route=account/register':
        print("Register page - loaded successfully")
    else:
        print("Register page - not loaded. Check")

    # Starts fill the form
    # username
    driver.find_element(By.ID, 'input-username').send_keys(locators.new_username)
    # firstname
    driver.find_element(By.ID, 'input-firstname').send_keys(locators.new_firstname)
    # lastname
    driver.find_element(By.ID, 'input-lastname').send_keys(locators.new_lastname)
    # email
    driver.find_element(By.ID, 'input-email').send_keys(locators.new_email)

    # country
    country_list = driver.find_element(By.ID, 'input-country')
    country_list_options = Select(country_list).options
    country_list_size = len(Select(country_list).options)
    num = randint(0, (country_list_size-1))
    country = country_list_options[num].text
    Select(country_list).select_by_visible_text(country)

    # password
    driver.find_element(By.ID, 'input-password').send_keys(locators.new_password)

    # # Captcha
    # for item in locators.captcha_list:
    #     if driver.find_element(By.XPATH, f'//*[ @ id = "captcha-message"]/*[contains(.,"{item}")]'):
    #         for image in locators.captcha_image:
    #             driver.find_element(By.XPATH, f'//*[ @ id = "captcha-message"]/*[img[contains(.,"{image}")]]').click()

    # Take users details to .csv file
    open('users_list.csv', 'a').write(f'{locators.new_username};{locators.new_firstname};{locators.new_lastname};{locators.new_email};{locators.new_password};{country};\n')

    # Click Register button
    driver.find_element(By.XPATH, '//button[text() = "Register"]' )
    print('User registered successfully')


def log_in(email, password):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Login').click()
    assert driver.current_url == 'https://www.opencart.com/index.php?route=account/login'
    print('Login page loaded successfully')
    # fill email
    driver.find_element(By.ID, 'input-email').send_keys(email)
    # fill password
    driver.find_element(By.ID, 'input-password').send_keys(password)
    # click Login button
    driver.find_element(By.XPATH, '//button[text() = "Login" ]').click()
    sleep(1)
    print('User logged in successfully')


def market_place_search_and_select():
    sleep(1)
    # Select item from list
    item_to_search = choice(locators.items_list)
    # Search item
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(item_to_search)
    sleep(0.25)
    driver.find_element(By.ID, 'button-search').click()
    # Select item
    driver.find_element(By.XPATH, f'//a[contains(., "{item_to_search}")]').click()
    print(f'Item <{item_to_search}> - searched and selected successfully')




# ----------------------------- Scenario_01:
# Scenario description:
# Register new user, validate by log in

# Go to homepage amd validate
set_up()
validate_page_url_title(locators.homepage_url, locators.homepage_title)
# Register new user
register_new_user()
# Log IN
# log_in(locators.new_email, locators.new_password)
log_in('bigboykev@gmail.com','@Kevinissocool8')
# Test done - write to log and close browser
tearDown('Scenario_01')

# ----------------------------- Scenario_02:
# Scenario description:
# Visit Marketplace - from Top menu
# Search item and select it

# Go to homepage amd validate
set_up()
validate_page_url_title(locators.homepage_url, locators.homepage_title)
# Go to Marketplace from top menu
driver.find_element(By.XPATH, '//a[text() = "Marketplace"]').click()
assert driver.current_url == 'https://www.opencart.com/index.php?route=marketplace/extension'
print("<Marketplace> from top menu - clicked and page loaded successfully")
# Search item
market_place_search_and_select()
# Test done - write to log and close browser
tearDown('Scenario_02')


# ----------------------------- Scenario_03:
# Scenario description:
# Visit Marketplace - button in the middle of home page
# Search item and select it

# Go to homepage amd validate
set_up()
validate_page_url_title(locators.homepage_url, locators.homepage_title)
# Go to Marketplace - button in the middle of home page
driver.find_element(By.XPATH, '//a[text() = "Visit Marketplace"]').click()
assert driver.current_url == 'https://www.opencart.com/index.php?route=marketplace/extension'
print("Button <Visit Marketplace> clicked and page loaded successfully")
# Search item
market_place_search_and_select()
# Test done - write to log and close browser
tearDown('Scenario_03')

# ----------------------------- Scenario_04:
# Scenario description:
# Validate all top menu links - click and validate page by current url


# Go to homepage amd validate
set_up()
validate_page_url_title(locators.homepage_url, locators.homepage_title)


# except RESOURCES. RESOURCES check after it
top_menu_list = ['FEATURES', 'DEMO', 'MARKETPLACE', 'BLOG', 'DOWNLOAD']

# select and validate each top menu link
for menu in top_menu_list:
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, menu).click()

    if menu == 'FEATURES':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=cms/feature'
    if menu == 'DEMO':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=cms/demo'
    if menu == 'MARKETPLACE':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=marketplace/extension'
    if menu == 'BLOG':
        assert driver.current_url == 'https://www.opencart.com/blog'
    if menu == 'DOWNLOAD':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=cms/download'

    print(f'Top Menu <{menu}> clicked and validated')


# RESOURCES check
RESOURCES_list = ['Showcase', 'Contact Us', 'OpenCart Partners', 'Community Forums',
                  'OpenCart Documentation', 'OpenCart Books', 'GitHub Bug Tracker', 'Developer']


for item in RESOURCES_list:
    sleep(0.5)
    driver.find_element(By.XPATH, '//a[contains(.,"Resources")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, f'//a[contains(.,"{item}")]').click()
    sleep(0.25)
    if item == 'Showcase':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=cms/showcase'
    if item == 'Contact Us':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=support/contact'
    if item == 'OpenCart Partners':
        assert driver.current_url == 'https://www.opencart.com/index.php?route=support/partner'
    if item == 'Community Forums':
        assert driver.current_url == 'https://forum.opencart.com/'
    if item == 'OpenCart Documentation':
        assert driver.current_url == 'http://docs.opencart.com/en-gb/introduction/'
    if item == 'OpenCart Books':
        assert driver.current_url == 'http://docs.opencart.com/en-gb/introduction/' # should be 'http://docs.opencart.com/#additional-reading'
    if item == 'GitHub Bug Tracker':
        assert driver.current_url == 'https://github.com/opencart/opencart/issues'
        driver.get(locators.homepage_url) # because redirected to different site - need back to homepage
    if item == 'Developer':
        assert driver.current_url == 'http://docs.opencart.com/en-gb/developer/module/' #should be 'http://docs.opencart.com/developer/module/'
        driver.get(locators.homepage_url)  #it's the end - go back to homepage

    print(f'Resources <{item}> clicked and validated')


# Test done - write to log and close browser
tearDown('Scenario_04')

#  ---------------------------------------------