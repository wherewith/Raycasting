import os
import pathlib
import zipfile

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


def upload():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://itch.io")
    driver.implicitly_wait(0.5)

    #Xpath=//tagname[@attribute='value']

    login_field = driver.find_element(by=By.XPATH, value="//a[@data-label = 'log_in']")
    login_field.click()
    driver.implicitly_wait(0.5)

    github_login_field = driver.find_element(by=By.XPATH, value="//button[@class = 'button outline github_login_btn']")
    github_login_field.click()
    driver.implicitly_wait(0.25)
    print(UN)


def main():
    # zip_build()
    upload()

if __name__ == '__main__':
    main()