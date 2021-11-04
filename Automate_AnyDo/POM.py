##importing necessary libraries
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from login import Login
from create_task import CreatTask
from create_task import CreateList
from utils import Uitilities


#initiating browser executable path

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome("C:/Users/FoysalAhmed/Downloads/chromedriver.exe",options=options) 


##openning url
driver.get("https://desktop.any.do/")
time.sleep(5)

login=Login(driver)
login.email('s.ahmed01@northsouth.edu')
time.sleep(4)

login.password('P@sswordf0ranydo')
time.sleep(4)
login.login()

task=CreatTask(driver)
task.task()
task.write_task('My Friday Task')
task.write_note('Hang out with friends')
task.set_reminder()
task.add_task()
task.create_subTask()
task.write_subTask('Wake up early')

##########---creating list and adding items-----######
List=CreateList(driver)
List.create_list()
List.write_listName('My Shopping List')
List.add_listItem()
List.write_itemName('T-shirst')
List.write_itemName('Pant')
List.write_itemName('Mouse')
List.write_itemName('Keyboard')

#####-----------#######
Utility=Uitilities()
Utility.change_theme()
Utility.check_notification()
Utility.add_selection_feature()
Utility.create_tag()
Utility.sign_out()


