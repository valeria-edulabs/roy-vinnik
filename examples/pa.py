from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("https://www.mypath.pa.gov/_/")
    print(driver)

    username = "GigaspacesPA"
    password = "5tgb4rfV54321@"

    elem = driver.find_element(By.NAME, "Dd-5")
    elem.send_keys(username)

    print("")

    # assert "Python" in driver.title
    # elem = driver.find_element(By.NAME, "q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    driver.close()