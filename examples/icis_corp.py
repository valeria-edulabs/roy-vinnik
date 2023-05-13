# ppb - Principal Place of Business
# oi - Officer Information
# di - Director Information
# auth - Authorization


import os
from io import BytesIO

from PIL import Image
from anticaptchaofficial.imagecaptcha import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Add your Anticaptcha Key here
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


def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver


def main():
    driver = get_driver()

    website = 'https://icis.corp.delaware.gov/ecorp/logintax.aspx?FilingType=FranchiseTax'
    company_number = '7893177'
    ppb_street_address = '1234 Rockville Pike'
    ppb_city = 'Rockville'
    ppb_state = 'MD'
    ppb_zip_code = '20852'
    ppb_country = 'USA'
    ppb_phone_ext = '01248508120482'
    ppb_email_address = 'info@vinnikcpa.com'

    number_of_directors = '2'

    oi_first_name = 'Jasper'
    oi_last_name = 'Foster'
    oi_title = 'Officer'
    oi_street_address = '99 Argyll Road'
    oi_city = 'Llanbedr'
    oi_state = 'Wales'
    oi_zip_code = 'LL45 0XS'
    oi_country = 'United Kingdom'

    di = {'di_first_name_1': 'Lee',
          'di_last_name_1': 'Ryan',
          'di_title_1': 'Officer',
          'di_street_address_1': '285 Lakewood Dr.',
          'di_city_1': 'Round Lake',
          'di_state_1': 'IL',
          'di_zip_code_1': '60073',
          'di_first_name_2': '7828',
          'di_last_name_2': 'Ryan',
          'di_title_2': 'Officer',
          'di_street_address_2': '7828 Carpenter Lane',
          'di_city_2': 'Morristown',
          'di_state_2': 'NJ',
          'di_zip_code_2': '07960',
          }

    auth_first_name = 'Rowan'
    auth_last_name = 'Barnes'
    auth_title = 'Officer'
    auth_street_address = '3861 Collins Avenue'
    auth_city = 'Worthington'
    auth_state = 'OH'
    auth_zip_code = '43085'

    driver.get(website)

    # Company Number
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@name="ctl00$ContentPlaceHolder1$txtPrimaryFileNo"]'))).send_keys(company_number)

    # Get Image URL and Solve Captcha
    image_url = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, 'ctl00_ContentPlaceHolder1_ctl03_RadCaptcha1_CaptchaImageUP'))).get_attribute('src')
    captcha_code = solve_image_captcha(image_url)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@name="ctl00$ContentPlaceHolder1$ctl03$rcTextBox1"]'))).send_keys(captcha_code)

    # Click on Submit
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))).click()
    time.sleep(2)

    if 'TO CONTINUE SEARCHING, PLEASE ENTER THE CODE FROM THE BELOW IMAGE.' in driver.page_source:
        print('Error in Captcha')
    else:
        # Click on File Amended Annual Report
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_lnkCurrentAR'))).click()
        time.sleep(3)

        # Insert street address in Principal Place of Business
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtStreetPrincipal'))).send_keys(
            ppb_street_address)

        # Insert City in Principal Place of Business
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtCityPrincipal'))).send_keys(ppb_city)

        # Insert State in Principal Place of Business
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_drpHidePrincipal'))).send_keys(
            ppb_state)

        # Insert Zip Code in Principal Place of Business
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtZipPrincipal'))).send_keys(
            ppb_zip_code)

        # Insert Phone/Ext in Principal Place of Business
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtPhonePrincipal1'))).send_keys(
            ppb_phone_ext)

        # Insert Email Address in Principal Place of Business
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtEmailPrincipal'))).send_keys(
            ppb_email_address)

        # Insert First Name in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtFirstOfficer'))).send_keys(
            oi_first_name)

        # Insert Last Name in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtLastOfficer'))).send_keys(
            oi_last_name)

        # Insert Title in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtTitleOfficer'))).send_keys(oi_title)

        # Checkbox Non-US Address
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_chkNonUSOfficer'))).click()

        # Insert Street Address in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtStreetOfficer'))).send_keys(
            oi_street_address)

        # Insert City in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtCityOfficer'))).send_keys(oi_city)

        # Insert State in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtDispOfficer'))).send_keys(oi_state)

        # Insert Zip Code in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtZipOfficer'))).send_keys(oi_zip_code)

        # Insert Country in Officer Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_drpOfficer'))).send_keys(oi_country)

        # Insert Total Number of Directors
        numofDirectors = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtTotalNumOfDirectors')))
        numofDirectors.clear()
        numofDirectors.send_keys(number_of_directors)

        # Click on Enter Directors Info
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnDisplayDirectorForm'))).click()

        for i in range(1, int(number_of_directors) + 1):
            # Insert First Name in Directors Information
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, f'txtDirectorName{i}'))).send_keys(
                di[f'di_first_name_{i}'])

            # Insert Last Name in Directors Information
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, f'txtLastName{i}'))).send_keys(
                di[f'di_last_name_{i}'])

            # Insert Street Address in Directors Information
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, f'txtDirectorAddress{i}'))).send_keys(
                di[f'di_street_address_{i}'])

            # Insert City in Directors Information
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, f'txtDirectorCity{i}'))).send_keys(
                di[f'di_city_{i}'])

            # Insert State in Directors Information
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, f'drpDirectorStates{i}'))).send_keys(di[f'di_state_{i}'])

            # Insert Zip Code in Directors Information
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, f'txtDirectorZip{i}'))).send_keys(
                di[f'di_zip_code_{i}'])

        # Checkbox Terms and Conditions
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_chkCertify'))).click()

        # Insert First Name in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtFirstAuthorization'))).send_keys(
            auth_first_name)

        # Insert Last Name in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtLastAuthorization'))).send_keys(
            auth_last_name)

        # Insert Title in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtTitleAuthorization'))).send_keys(
            auth_title)

        # Insert Street Address in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtStreetAuthorization'))).send_keys(
            auth_street_address)

        # Insert City in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtCityAuthorization'))).send_keys(
            auth_city)

        # Insert State in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_drpHideAuthor'))).send_keys(auth_state)

        # Insert Zip Code in Authorization
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtZipAuthorization'))).send_keys(
            auth_zip_code)

        # Click on Save and Exit
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btnSaveSession'))).click()
        time.sleep(10)


if __name__ == '__main__':
    main()
