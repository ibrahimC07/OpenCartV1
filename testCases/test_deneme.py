import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setEposta(self.user)
        self.lp.setsifre(self.password)
        self.lp.clickgiris()
        time.sleep(3)

