from selenium.webdriver.common.by import By


class LoginPage():
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_css = "button[type='submit']"
    msg_myaccount_xpath = "//h2[normalize-space()='My Account']"
    txt_eposta_xpath = "//input[@id='email']"
    txt_sifre_xpath = "//input[@id='password']"
    txt_giris_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btn_login_css).click()

    def setEposta(self, email):
        self.driver.find_element(By.XPATH,self.txt_eposta_xpath).send_keys(email)

    def setsifre(self, pwd):
        self.driver.find_element(By.XPATH,self.txt_sifre_xpath).send_keys(pwd)

    def clickgiris(self):
        self.driver.find_element(By.XPATH,self.txt_giris_xpath).click()


    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False

