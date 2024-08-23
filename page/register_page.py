from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.locator import locator


class register_page:
    def __init__(self,driver):
        self.driver=driver
        self.continue_click_btn = locator.cnt_click_buttun_By_Xpath

        self.write_first_name = locator.txt_first_name_By_Name
        self.write_last_name = locator.txt_last_name_By_Name
        self.write_Email_name = locator.txt_Email_name_By_Name
        self.write_number_name = locator.txt_contact_no_name_By_Name
        self.write_Fax_name = locator.txt_Fax_no_name_By_Name

        self.write_company_name = locator.txt_It_company_name_By_Name
        self.write_first_address = locator.txt_first_address_name_By_Name
        self.write_second_address = locator.txt_second_address_name_By_Name
        self.write_city_name = locator.txt_area_name_By_Name
        self.write_state_name = locator.txt_state_name_By_Name
        self.write_pin_code = locator.txt_zip_code_name_By_Name
        self.write_country = locator.txt_country_name_By_Name

        self.write_loginname = locator.txt_login_name_By_Name
        self.write_password = locator.txt_login_pass_By_Name
        self.write_confirm_password = locator.txt_cnfm_pass_By_Name

        self.click_subc_no = locator.txt_click_check_box_By_Name
        self.click_agree_yes = locator.txt_click_agree_check_box_By_Name

        self.click_continue_btn = locator.continue_click_btn_By_Xpath


    def click_btn_continue(self):
        self.driver.find_element(By.XPATH, value=self.continue_click_btn).click()

    def enter_first_name(self,firstname):
        self.driver.find_element(By.NAME,value=self.write_first_name).send_keys(firstname)

    def enter_last_name(self,lastname):
        self.driver.find_element(By.NAME,value=self.write_last_name).send_keys(lastname)

    def enter_email(self,email):
        self.driver.find_element(By.NAME,value=self.write_Email_name).send_keys(email)

    def enter_number(self,number):
        self.driver.find_element(By.NAME,value=self.write_number_name).send_keys(number)

    def enter_fax(self,fax):
        self.driver.find_element(By.NAME,value=self.write_Fax_name).send_keys(fax)

    def enter_company_name(self,company):
        self.driver.find_element(By.NAME, value=self.write_company_name).send_keys(company)

    def enter_first_add(self,address):
        self.driver.find_element(By.NAME,value=self.write_first_address).send_keys(address)

    def enter_second_add(self,address):
        self.driver.find_element(By.NAME,value=self.write_second_address).send_keys(address)

    def enter_cityname(self,city):
        self.driver.find_element(By.NAME,value=self.write_city_name).send_keys(city)

    def enter_state(self, state):
        option = self.driver.find_element(By.NAME,value=self.write_state_name)#.select_by_visible_value(state)
        s = Select(option)
        variable = s.select_by_visible_text(state)

    def enter_pincode(self,pincode):
        self.driver.find_element(By.NAME,value=self.write_pin_code).send_keys(pincode)

    def enter_country_name(self,country):
        option = self.driver.find_element(By.NAME,value=self.write_country)
        s = Select(option)
        variable = s.select_by_visible_text(country)

    def enter_login_name(self,name):
        self.driver.find_element(By.NAME,value=self.write_loginname).send_keys(name)

    def enter_pass(self,password):
        self.driver.find_element(By.NAME,value=self.write_password).send_keys(password)

    def enter_cnfm_pass(self,conformpass):
        self.driver.find_element(By.NAME,value=self.write_confirm_password).send_keys(conformpass)

    def click_check_subc_no(self):
        self.driver.find_element(By.NAME,value=self.click_subc_no).click()

    def click_check_box_agree(self):
        self.driver.find_element(By.NAME,value=self.click_agree_yes).click()

    def click_cnt(self):
        self.driver.find_element(By.XPATH,value=self.click_continue_btn).click()