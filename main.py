# -*- coding: utf-8 -*-
"""
@author: Birol Emekli
"""
from selenium import webdriver
from time import sleep
import sys
from concurrent.futures import ThreadPoolExecutor

import Control, Rota, DriverSetting , DriverGet, SeferKontrol

def driverSetting():
    return DriverSetting.DriverSetting().driverUP()

def driverGet(drivers):
    DriverGet.DriverGet(drivers).driverGet()

def rota(driver,first_location,last_location,date):
    Rota.Rota(driver, first_location, last_location, date).dataInput()

def control(driver,timee):
    response = Control.Control(driver,timee).sayfaKontrol()

def sefer(driver,timee):
    SeferKontrol.SeferKontrol(driver,timee).travelFinder()


def mainLoop(nereden, nereye, tarih, saat):
    while True:
        driver = driverSetting()
        driverGet(driver)
        rota(driver,nereden,nereye,tarih)
        sefer(driver,saat)
        # control(driver,saat)


if __name__ == "__main__":
    nereden = "Gebze"
    nereye = "Bilecik YHT"
    tarih = "25.06.2024"
    saat = "09:11"

    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(mainLoop, nereden, nereye, tarih, saat)