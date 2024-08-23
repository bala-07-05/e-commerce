from selenium.webdriver.common.by import By

from config.locator import locator

class home_page:
    def __init__(self,driver):
        self.driver=driver
        self.home_continue_btn=locator.hom_cnt_click_btn_By_Xpath
        self.books_click_btn=locator.click_book_btn_By_Xpath
        self.paperback_click_btn=locator.click_paperback_btn_By_Xpath

        self.add_cart_miracle_book_btn=locator.add_miracle_cart_click_btn_by_Xpath
        self.add_cart_paper_book_btn=locator.add_cart_papertown_click_btn_by_Xpath
        self.cart_manu_click_btn=locator.click_manu_cart_btn_By_Xpath
        self.enter_checout=locator.cart_check_out_btn_By_Id

        self.enter_localdelivary_btn=locator.click_localdel_checkbox_By_Id
        self.txt_cmd_add=locator.write_cmd_add_By_Name
        self.click_cmd_btn=locator.click_cmd_apply_btn_By_Xpath
        self.txt_coupon=locator.giv_couponcode_By_Name
        self.click_coupon_apply_btn=locator.click_coupon_apply_btn_By_Xpath



    def hom_continue_click_btn(self):
        self.driver.find_element(By.XPATH,value=self.home_continue_btn).click()

    def click_books_opt(self):
        self.driver.find_element(By.XPATH,value=self.books_click_btn).click()

    def click_paperback(self):
        self.driver.find_element(By.XPATH,value=self.paperback_click_btn).click()

    def click_miracle(self):
        self.driver.find_element(By.XPATH,value=self.add_cart_miracle_book_btn).click()

    def click_town_book(self):
        self.driver.find_element(By.XPATH,value=self.add_cart_paper_book_btn).click()

    def click_cart_menu(self):
        self.driver.find_element(By.XPATH,value=self.cart_manu_click_btn).click()

    def click_checkout(self):
        self.driver.find_element(By.ID,value=self.enter_checout).click()

    def enter_local_del(self):
        self.driver.find_element(By.ID,value=self.enter_localdelivary_btn).click()

    def write_cmd(self, good):
        self.driver.find_element(By.NAME, value=self.txt_cmd_add).send_keys(good)

    def enter_cmd_btn(self):
        self.driver.find_element(By.XPATH, value=self.click_cmd_btn).click()

    def write_coupon_cmd(self, RXUIM):
        self.driver.find_element(By.NAME, value=self.txt_coupon).send_keys(RXUIM)

    def enter_coupon_cmd(self):
        self.driver.find_element(By.XPATH, value=self.click_coupon_apply_btn).click()








