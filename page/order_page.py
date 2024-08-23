from selenium.webdriver.common.by import By
from config.locator import locator

class order_page:

    def __init__(self,driver):
        self.driver=driver
        self.order_confirm=locator.confirm_order_btn_By_Xpath
        #self.click_orderdetails=locator.click_order_details_By_Xpath

    def enter_order(self):
        driver=self.driver

        order=driver.find_element(By.XPATH,value=self.order_confirm)
        driver.excute_script("arguements[0].scrollIntoView();",order)


