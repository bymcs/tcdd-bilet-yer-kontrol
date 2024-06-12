from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class DriverGet:
    def __init__(self, driver, url="https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf"):
        self.url = url
        self.driver = driver

    def driverGet(self):
        try:
            self.driver.get(self.url)
            print("Navigated to URL.")

            element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, "#biletAramaForm > div:nth-child(3) > p:nth-child(4)"))
            WebDriverWait(self.driver, 10).until(element_present)

            print("Sayfa yüklendi")
        except TimeoutException:
            print("Loading took too much time! The element was not found.")
        except NoSuchElementException:
            print("The specified element was not found on the page.")
        except Exception as e:
            print(f"An error occurred: {e}")
