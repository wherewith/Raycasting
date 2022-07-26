import os
import pathlib
import time
import zipfile
import easygui
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def zip_build():
    file_dir = pathlib.Path("./build/web")
    with zipfile.ZipFile("web-release.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=1) as archive:
        for file_path in file_dir.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(file_dir))
    os.replace("./web-release.zip", "./build/web-release.zip")


def upload(game_id):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://itch.io")
    driver.implicitly_wait(0.75)

    # ITCH LOGIN BUTTON
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@data-label = 'log_in']"))).click()
    # LOG IN W/ GITHUB BUTTON
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class = 'button outline github_login_btn']"))).click()
    # Prompt username and password and enter into fields
    # TODO replace easygui with pyautogui to reduce dependencies
    input = easygui.multpasswordbox("Enter username and password", "Enter username and password", ["Username", "Password"], ["", ""])
    github_username_field = driver.find_element(by=By.XPATH, value="//input[@id = 'login_field']")
    github_username_field.send_keys(input[0])
    github_password_field = driver.find_element(by=By.XPATH, value="//input[@id = 'password']")
    github_password_field.send_keys(input[1])
    # SIGN IN W/ GITHUB BUTTON
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@value = 'Sign in']"))).click()
    # EDIT FILE BUTTON
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//a[@href = '/game/edit/{game_id}']"))).click()
    # IF FILE EXISTS, DELETE IT
    try:
        del_button = driver.find_element(by=By.XPATH, value="//button[@class = 'delete_btn']")
        del_button.click()
        driver.implicitly_wait(0.2)
        driver.switch_to.alert.accept()
    except:
        print("Nothing to delete! ")
    # UPLOAD NEW FILE
    upload_present = EC.presence_of_element_located((By.XPATH, "//div[@class = 'button add_file_btn has_multi_upload']"))
    WebDriverWait(driver, 10).until(upload_present).click()
    time.sleep(1)
    pyautogui.write(os.getcwd() + "\\" + "build\web-release.zip", interval = .01)
    pyautogui.press('enter')
    time.sleep(2) #upload time
    # SAVE
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class = 'button save_btn']"))).click()


def main():
    zip_build()
    upload(1707593)

if __name__ == '__main__':
    main()