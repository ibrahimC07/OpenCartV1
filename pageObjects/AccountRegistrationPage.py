import time

from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_xpath = "//input[@id='input-firstname']"
    txt_lastname_xpath = "//input[@id='input-lastname']"
    txt_email_xpath = "//input[@id='input-email']"
    # txt_telphone_name = "telephone"
    txt_password_xpath = "//input[@id='input-password']"
    # txt_confpassword_name = "confirm"
    chk_policy_css = "input[value='1'][name='agree']"
    btn_cont_css = "button[type='submit']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    # def setTelephone(self,tel):
    #    self.driver.find_element(By.NAME,self.txt_telphone_name).send_keys(tel)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    # def setConfirmPassword(self,cnfpwd):
    #     self.driver.find_element(By.NAME,self.txt_confpassword_name).send_keys(cnfpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.CSS_SELECTOR, self.chk_policy_css).click()

    def clickContinue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_cont_css).click()


    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None
