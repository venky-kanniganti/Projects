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
#Variable so that xpath doesnt need to be written out every time
count = 3
#Variable for counting choice  number
lastChoice = 0
#Variable for counting choice ID number
lastChoiceID = 0
#method for dropdowns
def dropDown(xpathDrop, xpathAns):
    Drop = driver.find_element(by = By.XPATH, value = xpathDrop)
    Drop.click()
    Ans = driver.find_element(by = By.XPATH, value = xpathAns)
    Ans.click()
    Ans.send_keys(Keys.ENTER)
#method for filling textbox (Default Answer assumed to be 0)
def textFiller(text = '0'):
    global count
    textBox = driver.find_element(by = By.XPATH, value = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{}]/div/div/div[2]/div/div[1]/div/div[1]/input'.format(count))
    textBox.send_keys(text + Keys.ENTER)
    count+= 1
#method for multiple choice (Default Answer assumed to be No)
def choice():
    global count
    global lastChoice
    global lastChoiceID
    if lastChoice == 0:
        choiceCount = 24
    else:
        choiceCount = lastChoiceID + 4*(count - lastChoice) + 6
    Answer = driver.find_element(by = By.XPATH, value = '//*[@id="i{}"]/div[3]/div'.format(choiceCount))
    Answer.click()
    lastChoiceID = choiceCount
    lastChoice = count
    count+= 1
#Building Manager
dropDown('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[31]')
#Time of Round

#TableTennis
textFiller()
#SquashCourt 6
textFiller()
#PE Follow up
choice()
#SquashCourt 5
textFiller()
#PE Follow up
choice()
#Racquetball Court 4
textFiller()
#PE Follow up
choice()
#Batting Court 3
textFiller()
#Cycling Court 2
textFiller()
#PE Follow up
choice()
#Rowing Court 1
textFiller()
#Indoor Track
textFiller()
#Varsity Athlete? Follow up
choice()
#Blue 1
textFiller()
#Blue 2
textFiller()
#Blue 3
textFiller()
#Blue 4
textFiller()
#VanHorn Count
textFiller()
#Rec users VanHorn
textFiller()
#IceRink
textFiller()
#MPR
textFiller()
#MPR Follow up
choice()
#Captain Lounge
textFiller()
#Conference Room
textFiller()
#Cardio Room
textFiller()
#Cardio Room Follow up
choice()
#Horsburgh
textFiller()
#Racquetball Court 12
textFiller()
#PE Follow up
choice()
#Racquetball Court 11
textFiller()
#PE Follow up
choice()
#RockWall Court 10
textFiller()
#Racquetball Court 9
textFiller()
#PE Follow up
choice()
#Racquetball Court 8
textFiller()
#PE Follow up
choice()
#Racquetball Court 7
textFiller()
#PE Follow up
choice()
#Main Lobby and Del Rosa
textFiller()
#Hall of Fame Room
textFiller()
#All-American Hallway
textFiller()
#Natatorium
textFiller()
#Donnell
textFiller()
#Main Weight Room
textFiller()
#PE Follow up
choice()
#Rack Room
textFiller()
#PE Follow up
choice()
#Hammer Room
textFiller()
#PE Follow up
choice()
# WR 104
textFiller()
# Adelbert
textFiller()
# Adelbert Follow up
choice()
