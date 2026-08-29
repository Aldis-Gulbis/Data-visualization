import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import requests
import bs4

import time
from datetime import datetime, timedelta

from data import append

def get_values():
    countries = ["Austria", "Belgium",
                 "Bulgaria", "Croatia",
                 "Cyprus", "Czechia",
                 "Denmark", "Estonia",
                 "Finland", "France",
                 "Germany", "Greece",
                 "Hungary", "Ireland",
                 "Italy", "Latvia",
                 "Lithuania", "Luxembourg",
                 "Malta", "Netherlands",
                 "Poland", "Portugal",
                 "Romania", "Slovakia",
                 "Slovenia", "Spain",
                 "Sweden"]

    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = service, options = option)

    url = "https://www.fuel-prices.eu"
    driver.get(url)
    time.sleep(2)

    time.sleep(2)

    saturs = bs4.BeautifulSoup(driver.page_source, "html.parser")
    datumi = saturs.find_all("td", class_ = "date-cell")

    count = 0
    datums = datumi[0].text.strip()
    datums = datetime.strptime(datums, "%d %b %y")

    for j in range(10):
        nakamais_datums = datums - timedelta(days=j * 7)
        datums_value = nakamais_datums.strftime("%Y-%m-%d")

        izvele = Select(driver.find_element(By.ID, "dateA"))
        izvele.select_by_value(datums_value)
        time.sleep(3)

        count = 0

        saturs = bs4.BeautifulSoup(driver.page_source, "html.parser")
        cenas = saturs.find_all(class_="price-main")
        datumi = saturs.find_all("td", class_="date-cell")

        for i in range(0, len(cenas), 2):
            petrol_price = cenas[i].text.strip().replace("€", "")
            diesel_price = cenas[i + 1].text.strip().replace("€", "")
            date = datumi[count].text.strip()

            append(petrol_price, diesel_price, countries[count], date)

            count += 1