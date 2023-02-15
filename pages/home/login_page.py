from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _email_filed = "mat-input-0"
    _password_filed = "mat-input-1"
    _click_login_button = '//button[@class="mat-focus-indicator login-submit mat-raised-button mat-button-base mat-primary"]'
    _click_user_button = "//div[@class='avatar-container']" #xpath
    _sign_out_button = "//a[contains(text(), 'Log out')]"  # xpath

    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_filed)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_filed)
    #
    # def getClickLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._click_login_button)

    def enterEmail(self, email):
        # self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_filed, locatorType="id")

    def enterPassword(self, password):
        # self.getPasswordField().send_keys(password)
        self.sendKeys(password, self._password_filed, locatorType="id")

    def clickLoginButton(self):
        # self.getClickLoginButton().click()
        self.elementClick(self._click_login_button, locatorType="xpath")

    def login(self, email, password):
        self.clearFields()
        # email_field = self.driver.find_element(By.ID, "mat-input-0")
        # email_field.send_keys(username)
        self.enterEmail(email)

        # password_field = self.driver.find_element(By.ID, "mat-input-1")
        # password_field.send_keys(password)
        self.enterPassword(password)

        # click_login_button = self.driver.find_element(By.XPATH,
        #                                          '//button[@class="mat-focus-indicator login-submit mat-raised-button mat-button-base mat-primary"]')
        # click_login_button.click()
        self.clickLoginButton()
        self.hold_wait()
        self.hold_wait()
        # self.screen_shot()

    def sign_out(self):
        self.hold_wait()
        # self.waitForElement(self._click_user_button, locatorType="xpath", timeout=20, pollFrequency=2)
        # self.isElementPresent(self._click_user_button, locatorType="xpath")
        # self.elementPresenceCheck(self._click_user_button, locatorType="xpath")
        # self.hold_wait()
        self.elementClick(self._click_user_button, locatorType="xpath")
        # self.hold_wait()
        self.elementClick(self._sign_out_button, locatorType="xpath")
        self.hold_wait()

    def verifyLoginSuccessful(self):
        pass

    _pop_failed = "//span[contains(text(),'Authorization error. Incorrect credentials.')]"
    def verifyLoginFailed(self):
        result = self.isElementPresent(self._pop_failed, locatorType="xpath")
        if result == True:
            print("Authorization error. Incorrect credentials.")

    def clearFields(self):
        email_field = self.getElement(locator=self._email_filed)
        email_field.clear()

        password_filed = self.getElement(locator=self._password_filed)
        password_filed.clear()

    def verifyTitle(self):
        if "Admin Dashboard" in self.getTitle():
            return True
        else:
            return False
