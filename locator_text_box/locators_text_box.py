from selenium.webdriver.common.by import By

class text_box_locators:
    full_name = (By.ID, "userName")
    email = (By.ID, "userEmail")
    current_address = (By.ID, "currentAddress")
    permanent_address = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")

class output_field_locators:
    name = (By.ID, "name")
    email = (By.ID, "email")
    c_address = (By.CSS_SELECTOR, "p#currentAddress")
    p_address = (By.CSS_SELECTOR, "p#permanentAddress")

    