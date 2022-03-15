from time import sleep
import datetime

import unittest

from selenium.webdriver.common.action_chains import ActionChains

import boldcommerce_methods as methods
import boldcommerce_locators as locators

divider = methods.divider
By = methods.By
driver = methods.driver

# =================================================== Running tests


class ContactSales(unittest.TestCase):

    # Navigate to home page
    methods.set_up()
    # Validate home page loading
    methods.check_page_url_title('Home page', locators.home_page_url,'Bold Commerce | Modular Commerce Solutions - Sell Anywhere')

    @staticmethod
    def test_contact_sales():

        # ---------------------------------- Scenario_01
        # Description: Contact Sales via button on right side

        print(divider)
        print(f'Scenario_01 started at {datetime.datetime.now()}')
        print('Description: Contact Sales via button on right side')
        # Navigate to contact sales form
        driver.find_element(By.XPATH, '//a[text() = "Contact Sales" and contains(@class,"omninav-cta")]').click()
        # Validate URL and title
        methods.check_page_url_title('Contact Sales', 'https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

        # Contact sales - fill form
        methods.contact_sales_form()
        # test  completed
        methods.test_completed('Scenario_01')

        # ---------------------------------- Scenario_02
        # Description: Contact Sales via second button on middle

        # Navigating to the home page
        driver.get(locators.home_page_url)

        sleep(1)
        print(divider)
        print(f'Scenario_02 started at {datetime.datetime.now()}')
        print('Description: Contact Sales via second button on middle')
        # Navigate to contact sales form
        methods.driver.find_element(By.XPATH, '//div[contains(@class, "hero__content")]/a[text() = "Contact Sales"]').click()
        # Validate URL and title
        methods.check_page_url_title('Contact Sales', 'https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

        # Contact sales - fill form
        methods.contact_sales_form()

        # test  completed
        methods.test_completed('Scenario_02')


        # ---------------------------------- Scenario_03
        # Description: Contact Sales via third button almost in bottom

        # Navigating to the home page
        driver.get(locators.home_page_url)

        sleep(1)
        print(divider)
        print(f'Scenario_03 started at {datetime.datetime.now()}')
        print('Description: Contact Sales via third button almost in bottom')
        # Navigate to contact sales form
        driver.find_element(By.XPATH, '//div[contains(@class, "cta-block__actions")]/a[text() = "Contact Sales"]').click()
        # Validate URL and title
        methods.check_page_url_title('Contact Sales', 'https://boldcommerce.com/contact/sales', 'Contact Sales | Bold Commerce')

        # Contact sales - fill form
        methods.contact_sales_form()

        # test  completed
        methods.test_completed('Scenario_03')


 


        # ===================================================''
        # Close browser
        if driver is not None:
            driver.close()
            driver.quit()
