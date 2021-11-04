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
