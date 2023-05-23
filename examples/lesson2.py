import os
from io import BytesIO
from telnetlib import EC

import requests
from PIL import Image
from anticaptchaofficial.imagecaptcha import imagecaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

anticaptcha_key = ''

def solve_image_captcha(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # Save the image to a local file
    img.save('captcha_image.png')

    # Solve the captcha using AntiCaptcha
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(anticaptcha_key)
    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution("captcha_image.png")
    if captcha_text != 0:
        print("captcha text " + captcha_text)
    else:
        print("task finished with error " + solver.error_code)

    os.remove('captcha_image.png')

    return captcha_text

website = 'https://icis.corp.delaware.gov/ecorp/logintax.aspx?FilingType=FranchiseTax'
driver = webdriver.Chrome()

driver.get(website)

# Company Number
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@name="ctl00$ContentPlaceHolder1$txtPrimaryFileNo"]'))).send_keys(company_number)

# Get Image URL and Solve Captcha
# image_url = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.ID, 'ctl00_ContentPlaceHolder1_ctl03_RadCaptcha1_CaptchaImageUP'))).get_attribute('src')

elem = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_ctl03_RadCaptcha1_CaptchaImageUP')
image_url = elem.get_attribute('src')
captcha_code = solve_image_captcha(image_url)
