from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverSetting:
    def driverUP(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1920,1080')
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            return driver
        except Exception as e:
            print(f"An error occurred: {e}")
            return None