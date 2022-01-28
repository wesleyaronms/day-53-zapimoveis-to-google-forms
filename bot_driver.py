from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from get_data import GetData
import time
import os


DRIVER_PATH = os.getenv("WEB_DRIVER_PATH")
LINK_FORM_SHORT = "https://forms.gle/Tir8FqdRwDb5FcDj7"


class BotDriver:

    def __init__(self):
        service = Service(executable_path=DRIVER_PATH)
        self.driver = WebDriver(service=service)

    def fill_forms(self):
        """Preenche o formulário com os dados presentes no objeto criado a partir da classe GetData"""
        data = GetData()
        self.driver.get(LINK_FORM_SHORT)
        time.sleep(5)
        for index in range(len(data.prices)):
            forms = self.driver.find_elements(By.CLASS_NAME, "quantumWizTextinputPaperinputInput")
            time.sleep(1)
            forms[0].send_keys(data.address[index])
            forms[1].send_keys(data.prices[index])
            forms[2].send_keys(data.links[index])
            forms[3].send_keys(data.details[index])
            self.driver.find_element(By.CLASS_NAME, "appsMaterialWizButtonEl").click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "a").click()
        self.driver.quit()


# Depois, é só passar as repostas do formulário para o Google Sheets.
