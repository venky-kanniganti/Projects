from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Default')
service = ChromeService(executable_path='/Users/venky/Downloads/chromedriver')


driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)
patronForm = driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdHxHZtzaKhjs_SGN6-eOQE5LX2h-dqlx8C5Z2cPhpyhHk09w/viewform")

#Building Manager
bmDropdown = driver.find_element(by = By.XPATH, value = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]')
bmDropdown.click()
bmAnswer = driver.find_element(by = By.XPATH, value = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[31]')
bmAnswer.click()
bmAnswer.send_keys(Keys.ENTER)
#TableTennis
test = driver.find_element(by = By.XPATH, value ='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
test.send_keys('0'+Keys.ENTER)
