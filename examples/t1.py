from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ids = ["id1", "id2", "id3"]
data = ["roy", "vinnik", "NY"]

def foo(driver, ids, data):
    for ids_one, data_one in zip(ids, data):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, ids_one))).send_keys(data_one)

driver = webdriver.Chrome()
driver.get("https://www.mypath.pa.gov/_/")
foo(driver)

