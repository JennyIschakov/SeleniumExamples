# ----------------------  Import
from selenium import webdriver
from selenium.webdriver.common.by import By

import datetime
from time import sleep

# ----------------------  Variables:
divider = '-------------------------------------------'

# ----------------------  Locators:
homepage_url = 'https://www.demoblaze.com/'
homepage_title = 'STORE'


# ---------------------- open browser and maximize window
driver = webdriver.Chrome()


# ----------------------  Functions:


def set_up():
    driver.maximize_window()
    driver.get(homepage_url)


def tear_down():
    if driver is not None:
        print(divider)
        print(f'Test done at {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def validate_page_url_title(page_url, page_title):

    print(divider)
    print(f'URL: loaded <{driver.current_url}> >>> expected <{page_url}>')
    print(f'Title: loaded <{driver.title}> >>> expected <{page_title}>')

    if driver.current_url == page_url and driver.title == page_title:
        print(f'Page  loaded successfully. URL and Title as expected')
    else:
        print(f'!!! Page <{page_url}> >> not loaded. Check your code')


def search(product):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    print(divider)
    driver.find_element(By.LINK_TEXT, product).click()
    sleep(1)
    assert driver.find_element(By.XPATH, f'//h2[text() = "{product}"]').is_displayed()


def add_to_cart(product):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    sleep(2)
    driver.switch_to.alert.accept()
    print(f'--- Product <{product}>  added to cart')


def check_cart(product):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    sleep(0.25)

    # validate that on Place order page
    if driver.find_element(By.XPATH, '//button[contains(.,"Place Order" )]'):
        sleep(1)
        # validate added product on page
        if driver.find_element(By.XPATH, f'//*[@id = "tbodyid"]/*/td[contains(., "{product}")]'):
            print(f'--- Product <{product}>  found on cart')
        else:
            print(f'--- Product <{product}> not found on cart. Check code')
    else:
        print('--- Not on Place order page. Check code')


def delete_product_from_cart(product):
    sleep(1)
    # validate added product on page
    if driver.find_element(By.XPATH, f'//td[contains(., "{product}")]'):
        # Delete row of the product
        driver.find_element(By.XPATH, f'//td[contains(., "{product}")]/following::*/a[text() = "Delete"]').click()
        print(f'--- Product <{product}>  deleted')
    else:
        print(f'--- Product <{product}> not found on cart. Check code')

# ----------------------  Scenario_01
# Start
set_up()

# Go to main page
validate_page_url_title(homepage_url, homepage_title)

# Search and validate page product
search("Nexus 6")

# Add to cart
add_to_cart("Nexus 6")

# Check the cart
check_cart("Nexus 6")

# After check - delete product
delete_product_from_cart("Nexus 6")

# End
tear_down()


# ----------------------