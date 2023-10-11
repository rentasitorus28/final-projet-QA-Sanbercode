import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import baselogin

class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_success_login(self): #TestCase1
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # PIM 
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(2) 
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/button[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
        time.sleep(2) 

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()