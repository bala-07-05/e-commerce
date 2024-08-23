from selenium.webdriver.common.by import By

from config.locator import locator

class login_page:
    def __init__(self,driver):
        self.driver=driver
        self.loginname = locator.loginname_By_Name
        self.password = locator.password_By_Name
        self.click_btn = locator.btn_click_buttun_By_Xpath

    def enter_loginname(self,loginname):
        self.driver.find_element(By.NAME,value=self.loginname).send_keys(loginname)

    def enter_password(self,password):
        self.driver.find_element(By.NAME,value=self.password).send_keys(password)

    def click_btn_button(self):
        self.driver.find_element(By.XPATH,value=self.click_btn).click()


