import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from page.login_page import login_page

from page.register_page import register_page

from page.home_page import home_page

from page.order_page import order_page


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\P Ashwini\\OneDrive\\Desktop\\chrome webdriver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.get("https://demo.abantecart.com/index.php?rt=account/login/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        objlog = login_page(driver)
        objlog.enter_loginname("balaji")
        objlog.enter_password("bala")
        objlog.click_btn_button()

        objreg = register_page(driver)
        objreg.click_btn_continue()
        objreg.enter_first_name("bala")
        objreg.enter_last_name("ji")
        objreg.enter_email("baljhjdy796@gmail.com")
        objreg.enter_number(4567)
        objreg.enter_fax("fgh")

        objreg.enter_company_name("Tcs")
        objreg.enter_first_add("chennai")
        objreg.enter_second_add("bangalore")
        objreg.enter_cityname("majastic")
        objreg.enter_state("California")
        objreg.enter_pincode(234567)
        objreg.enter_country_name("United States")

        objreg.enter_login_name("bjafdjii")
        objreg.enter_pass("strbalaji")
        objreg.enter_cnfm_pass("strbalaji")
        objreg.click_check_subc_no()
        objreg.click_check_box_agree()
        objreg.click_cnt()

        objhom = home_page(driver)
        objhom.hom_continue_click_btn()

        objhom.click_books_opt()
        objhom.click_paperback()
        objhom.click_miracle()
        objhom.click_town_book()
        objhom.click_cart_menu()
        objhom.click_checkout()
        objhom.enter_local_del()
        objhom.write_cmd("GOOD")
        objhom.enter_cmd_btn()
        objhom.write_coupon_cmd("CUROW")
        objhom.enter_coupon_cmd()

        objord=order_page(driver)




        time.sleep(10000)




if __name__ == '__main__':
    unittest.main()