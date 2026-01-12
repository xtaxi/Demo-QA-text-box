from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator_text_box.locators_text_box import text_box_locators, output_field_locators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_field(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def get_email_field_classes(self):
        element = self.wait.until(EC.visibility_of_element_located((output_field_locators.email)))
        return element.get_attribute("class")
    
    def fill_and_submit_form(self, name, email, c_addr, p_addr):
        self.fill_field(text_box_locators.full_name, name)
        self.fill_field(text_box_locators.email, email)
        self.fill_field(text_box_locators.current_address, c_addr)
        self.fill_field(text_box_locators.permanent_address, p_addr)

        self.click_element(text_box_locators.submit_button)
