from locator_text_box.locators_text_box import text_box_locators
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage
from locator_text_box.locators_text_box import text_box_locators



class text_box_form(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def go_to_page(self):
         self.driver.get("https://demoqa.com/text-box")
         self.driver.maximize_window()

    def happy_path(self, name, email, c_addr, p_addr):
        self.fill_and_submit_form(name, email, c_addr, p_addr)

    def unhappy_path(self, name, email, c_addr, p_addr):
        self.fill_and_submit_form(name, email, c_addr, p_addr)
    
    def boundary_exceeded_test(self, name, email, c_addr, p_addr):
        self.fill_and_submit_form(name, email, c_addr, p_addr)

    def get_email_field_classes(self):
        return self.find(text_box_locators.email).get_attribute("class")
    