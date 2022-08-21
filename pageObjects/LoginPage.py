from selenium.webdriver.common.by import By


class LoginPage():
    #  Locators of all the elements
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_linkTest = "welcome"
    link_logout_linktest = "logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.textbox_password_id).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.textbox_password_id).click()


