# -*- coding: utf-8 -*-
"""
@author: Birol Emekli
"""
import \
    time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException,UnexpectedAlertPresentException
from time import sleep
import sys



class SeferKontrol:
    def __init__(self,driver,time):
        self.driver=driver
        self.zaman=time


    def travelFinder(self):

        try:
            print("Sefer Kontrol Başladı")
            time.sleep(1)
            # Tablonun yüklenmesini bekle
            table = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="mainTabView:gidisSeferTablosu_data"]'))
            )
            time.sleep(1)
            # Tablodaki satırları bul
            rows = table.find_elements(By.TAG_NAME, 'tr')
            # Her bir satırı işleyelim
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                departure_date = cells[0].text.strip()
                departure_time = cells[0].find_element(By.CLASS_NAME, 'seferSorguTableBuyuk').text.strip()

                duration = cells[1].text.strip()
                arrival_date = cells[2].text.strip()
                arrival_time = cells[2].find_element(By.CLASS_NAME, 'seferSorguTableBuyuk').text.strip()

                route_info = cells[3].text.strip()

                # Ekonomi ve Business koltuk sayıları için seçenekleri bul
                select_element = cells[4].find_element(By.TAG_NAME, 'select')
                options = select_element.find_elements(By.TAG_NAME, 'option')

                economy_seat_count = ""
                business_seat_count = ""

                for option in options:
                    label = option.text
                    if "Ekonomi" in label:
                        economy_seat_count = label
                    elif "Business" in label:
                        business_seat_count = label

                price = cells[5].text.strip()

                print(f"Sefer Tarihi: {departure_date}, Saat: {departure_time}, Süre: {duration}, Varış Tarihi: {arrival_date}, Varış Saati: {arrival_time}, Güzergah: {route_info}, Ekonomi Koltuk Sayısı: {economy_seat_count}, Business Koltuk Sayısı: {business_seat_count}, Fiyat: {price}")

            sleep(10)
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

        finally:
            print("Sefer Kontrol Bitti")
            self.driver.quit()
            sys.exit()

