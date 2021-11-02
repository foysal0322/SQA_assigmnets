class Login(object):


    def __init__(self,driver):
        self.driver=driver

    def email(self,email_name):
        import time
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]').click()
        time.sleep(2)
        self.driver.find_element_by_tag_name('input').send_keys(email_name)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/button').click() #email submit btn
        

    def password(self,pass_name):
        import time
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input').send_keys(pass_name)
     

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/button[2]').click()


class CreatTask(object):
    def __init__(self,driver):
        self.driver=driver
    
    def task(self):
        '''clcik on create task button'''
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/div[2]/div/button/span[2]').click()

    def write_task(self,task_name):
        '''write task name'''
        import time
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[1]/div/div/div/textarea').send_keys(task_name)
        time.sleep(2) 

    def write_note(self,note_name):
        '''write note's name'''
        import time
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[2]/div[2]/div/div/textarea').click().send_keys(note_name)
        time.sleep(2) 

    def set_reminder(self):
        '''sets reminder on next week'''
        import time
        self.driver.find_element_by_xpath('//button[contains(text(), "Next")]').click()
        time.sleep(2)

    def add_task(self):
        ''''clicks on add task button'''
        import time
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button/strong').click()
        time.sleep(2)

    def create_subTask(self):
        '''selecting created task'''
        import time
        select_task=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/section/div/article[1]/div/div[2]/article/div/div/div/div/div/div[1]/div[1]/div[1]')
        select_task.click()
        time.sleep(2)

        click_subtask=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/button/div')
        click_subtask.click()
        time.sleep(2)

    def write_subTask(self,subTask_name):
        '''write sub task name'''
        import time
        try:
            write_subtask=self.driver.find_element_by_class_name('SubTaskItem__mainContent')
            write_subtask.send_keys(subTask_name)
        except:
            pass
        close_subtask_Window=self.driver.find_element_by_class_name('BackdropModal')
        close_subtask_Window.click()

class CreateList(object):
    def __init__(self,driver):
        self.driver=driver

    def create_list(self):
        '''clicks on list plus(+) icon'''
        import time
        click_listIcon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[1]/div[2]/div/button[2]')
        click_listIcon.click()
        time.sleep(2)

    def write_listName(self,list_name):
        '''write list's name'''
        import time
        write_listName=self.driver.find_element_by_tag_name('textarea')
        write_listName.click()
        write_listName.send_keys(list_name)
        time.sleep(2)
        save_listName=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button[2]')
        save_listName.click()
        time.sleep(2)

    def add_listItem(self):
        '''click newly create list name to add items'''
        import time
        click_toAdd_listItem=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul/li[4]/a/div[2]')
        click_toAdd_listItem.click()
        time.sleep(2)
    def write_itemName(self,item_name):
        '''write list's item name'''
        import time
        from selenium.webdriver.common.keys import Keys
        write_itemName=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/section/article/form/div/div/div/input[1]')
        write_itemName.click()
        write_itemName.send_keys(item_name)
        write_itemName.send_keys(Keys.RETURN)
        time.sleep(2)  


class Uitilities(object):
    def change_theme(self):
        '''change the theme into dark'''
        import time
        click_settings_icon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div/div/div[3]/button')
        click_settings_icon.click()
        time.sleep(2)

        click_theme=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[5]/div[1]')
        click_theme.click()
        time.sleep(2)

        select_theme=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[4]/div/div/div/form/div[3]/div[1]/label')
        select_theme.click()
        time.sleep(2)
        click_settings_icon.click()
        time.sleep(2)

    def check_notification(self):
        '''checks updates notification'''
        import time
        click_notification_icon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div/div/button[2]')
        click_notification_icon.click()
        time.sleep(1)
        click_notification_update=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/ul/li[1]/button')
        click_notification_update.click()
        time.sleep(2)
        click_notification_icon.click()
        time.sleep(2)

    def add_selection_feature(self):
        '''clicks on multiple selection icon and dismiss thw window later'''
        import time
        click_more_Option=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div/div/div/div[2]/div[2]/button[3]')
        click_more_Option.click()
        time.sleep(1)
        click_multiple_selection=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button')
        click_multiple_selection.click()
        time.sleep(1)
        close_selection_window=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[2]/div/button[5]')
        close_selection_window.click()
        time.sleep(4)
    

    def create_tag(self):
        '''clicks on tag's plus(+) icon and NO, THANKS ltaer'''
        import time
        click_tag=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[4]/div[1]/div[2]/button[2]')
        click_tag.click()
        time.sleep(1)
        click_noThanks=self.driver.find_element_by_xpath('//button[contains(text(), "No")]')
        click_noThanks.click()
        time.sleep(2)
    
    def sign_out(self):
        '''signing out'''
        import time
        click_settings_icon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div/div/div[3]/button')
        click_settings_icon.click()
        time.sleep(1)
        
        my_profile=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[1]')
        my_profile.click()
        time.sleep(1)
        sign_out=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[8]/div/div/div/button[3]')
        sign_out.click()
