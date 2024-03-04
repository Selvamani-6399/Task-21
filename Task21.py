from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class LoginPage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def quit(self):
        self.driver.quit()

    def login(self):

        username_input = self.driver.find_element(by=By.NAME, value="user-name")   
        password_input = self.driver.find_element(by=By.NAME, value="password")

        username_input.send_keys("standard_user")           
        password_input.send_keys("secret_sauce")

        self.driver.find_element(by=By.TAG_NAME, value="button").click()
        
        sleep(5)

    def getTitle(self):
        return self.driver.title    

    def getURL(self):
        return self.driver.current_url

    def sourceCode(self):
        return self.driver.page_source
    
    def getCookies(self):
        return self.driver.get_cookies()



url = "https://www.saucedemo.com/inventory.html"
obj = LoginPage(url)
obj.boot()

print(obj.getCookies())
obj.login()
print(obj.getCookies())
obj.quit()  