import os
import pathlib
import zipfile
import easygui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def zip_build():
    file_dir = pathlib.Path("./build/web")
    with zipfile.ZipFile("web-release.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=1) as archive:
        for file_path in file_dir.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(file_dir))
    os.replace("./web-release.zip", "./build/web-release.zip")


def upload(game_id):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://itch.io")
    driver.implicitly_wait(0.5)
    
    #Xpath=//tagname[@attribute='value']

    login_button = driver.find_element(by=By.XPATH, value="//a[@data-label = 'log_in']")
    login_button.click()
    driver.implicitly_wait(0.5)

    github_login_button = driver.find_element(by=By.XPATH, value="//button[@class = 'button outline github_login_btn']")
    github_login_button.click()
    driver.implicitly_wait(0.25)

    input = easygui.multpasswordbox("Enter username and password", "Enter username and password", ["Username", "Password"], ["", ""])

    github_username_field = driver.find_element(by=By.XPATH, value="//input[@id = 'login_field']")
    github_username_field.send_keys(input[0])

    github_password_field = driver.find_element(by=By.XPATH, value="//input[@id = 'password']")
    github_password_field.send_keys(input[1])
    driver.implicitly_wait(1)

    github_signin_button = driver.find_element(by=By.XPATH, value="//input[@value = 'Sign in']")
    github_signin_button.click()
    driver.implicitly_wait(5)

    edit_button = driver.find_element(by=By.XPATH, value=f"//a[@href = '/game/edit/{game_id}']")
    edit_button.click()
    driver.implicitly_wait(1)

    try:
        del_button = driver.find_element(by=By.XPATH, value="//button[@class = 'delete_btn']")
        del_button.click()
        driver.implicitly_wait(0.2)
        driver.switch_to.alert.accept()
    except:
        print("Nothing to delete! ")

    upload_button = driver.find_element(by=By.XPATH, value="//div[@class = 'button add_file_btn has_multi_upload']")


def main():
    # zip_build()
    upload(1707593)

if __name__ == '__main__':
    main()