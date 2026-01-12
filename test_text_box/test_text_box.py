import unittest
from selenium import webdriver
import path_config
from demoqa_text_box.form import text_box_form as TB
from assertpy import assert_that, soft_assertions
from locator_text_box.locators_text_box import output_field_locators
from test_data import HAPPY_PATH_DATA, INVALID_EMAIL_DATA, BOUNDARY_DATA
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

class TB_form(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def capture_failure(self, test_name, error):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        path = f"screenshots/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        print(f"\n[FAILURE] {test_name}: Screenshot saved to {path}")
        print(f"Error details: {error}")

    def test_form_happy(self):
        try:
            submitform = TB(self.driver)
            submitform.go_to_page()
            submitform.happy_path(HAPPY_PATH_DATA["name"], 
                                  HAPPY_PATH_DATA["email"], 
                                  HAPPY_PATH_DATA["cur_addr"], 
                                  HAPPY_PATH_DATA["perm_addr"])
            
            with soft_assertions():
                assert_that(submitform.get_text(output_field_locators.name)).contains(HAPPY_PATH_DATA["name"])
                assert_that(submitform.get_text(output_field_locators.email)).contains(HAPPY_PATH_DATA["email"])
            
        except Exception as e:
            self.capture_failure("test_form_happy", e)
            raise e

    def test_wrong_email(self):
        try:
            submitform = TB(self.driver)
            submitform.go_to_page()
            submitform.unhappy_path(INVALID_EMAIL_DATA["name"],
                                    INVALID_EMAIL_DATA["email"], 
                                    INVALID_EMAIL_DATA["cur_addr"], 
                                    INVALID_EMAIL_DATA["perm_addr"])
            
            assert_that(submitform.get_email_field_classes()).contains("field-error")
            
        except Exception as e:
            self.capture_failure("test_wrong_email", e)
            raise e

    def test_boundary_exceeded(self):
        try:
            submitform = TB(self.driver)
            submitform.go_to_page()
            submitform.boundary_exceeded_test(BOUNDARY_DATA["name"],
                                              BOUNDARY_DATA["email"], 
                                              BOUNDARY_DATA["cur_addr"], 
                                              BOUNDARY_DATA["perm_addr"])
            
            actual_output = submitform.get_text(output_field_locators.c_address)
            assert_that(actual_output).contains(BOUNDARY_DATA["cur_addr"])
            
        except Exception as e:
            self.capture_failure("test_boundary_exceeded", e)
            raise e

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()