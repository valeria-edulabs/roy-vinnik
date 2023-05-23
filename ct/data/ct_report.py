from csv import DictReader
from pprint import pprint

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TaxReporter:

    def __init__(self, intake_file, website_url, steps_file):
        self.website_url = website_url
        self.intake_file = intake_file
        self.steps_file = steps_file
        self.driver: WebDriver | None = None
        self.steps = self._load_steps()
        # pprint(self.steps)

    def _load_steps(self):
        with open(self.steps_file) as f:
            return list(DictReader(f))

    def _connect_driver(self):
        if not self.driver:
            print('Connecting to Chrome driver...')
            self.driver = webdriver.Chrome()

    def _disconnect_driver(self):
        if self.driver:
            self.driver.close()
        print('Driver disconnected')

    def _load_intake_data(self):
        with open(self.intake_file) as f:
            return list(DictReader(f))

    def _process_step(self, step, intake_entry):
        print('Running step:', step['comment'])

        if step['action'] == 'click':
            condition = expected_conditions.element_to_be_clickable
        else:
            condition = expected_conditions.visibility_of_element_located

        try:
            element: WebElement = WebDriverWait(self.driver, 5).until(
                condition((By.XPATH, step['xpath'])))
        except TimeoutException:
            element: WebElement = self.driver.find_element(By.XPATH, step['xpath'])

        if step['action'] == 'click':
            element.click()
        elif step['action'] == 'send_keys':
            element.clear()
            element.send_keys(intake_entry[step['content_field']])

    def _report_single(self, intake_entry):
        self.driver.get(self.website_url)

        for step in self.steps:
            self._process_step(step, intake_entry)

        print(f'Completed report for {intake_entry["username"]}')

    def submit(self):
        intake_data = self._load_intake_data()

        self._connect_driver()

        for intake_entry in intake_data:
            self._report_single(intake_entry)

        self._disconnect_driver()
