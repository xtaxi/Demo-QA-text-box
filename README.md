DemoQA Text Box Automation Framework
A professional Python-based test automation framework for the DemoQA Text Box module. This project implements the Page Object Model (POM) pattern to ensure scalability, maintainability, and clean code.

Key Features

Page Object Model (POM): Complete separation of test logic from UI locators.

Automated Driver Management: Uses webdriver-manager to handle ChromeDriver versions automatically.

Automated Screenshots: Captures a time-stamped screenshot in the /screenshots folder whenever a test fails.

Data-Driven Testing: Test data is stored in a centralized test_data.py file for easy updates.

Soft Assertions: Uses assertpy for flexible and detailed validation reports.


Tech Stack

Language: Python 3.14

Browser Automation: Selenium WebDriver

Test Runner: Unittest

Assertions: Assertpy

Driver Management: Webdriver-manager

Prerequisites
Before running the tests, ensure you have Python installed and run the following command to install the required libraries:

pip install -r requirements.txt

How to Run the Tests
You can run all tests from the root directory using the following command:
python -m unittest discover test_text_box

Viewing Failure Evidence
If a test fails:

Check the terminal output for error details.

Navigate to the screenshots/ folder.

Open the .png file labeled with the test name and failure timestamp.

📂 Project Structure

DEMOQACOM/
├── demoqa_text_box/        # Page Objects (Actions)
├── locator_text_box/       # UI Locators
├── test_text_box/          # Test Cases (Unittest)
├── screenshots/            # Failure evidence (Git-ignored)
├── base_page.py            # Base wrapper for Selenium methods
├── test_data.py            # Externalized test data
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation