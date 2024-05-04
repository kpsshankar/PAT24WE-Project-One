#Editing a existing employee in PIM module

#Successfull employee login to OrangeHRM portal
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class Form:

   
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait.until(ec.url_to_be(self.url))
       
   def quit(self):
       self.driver.quit()


   
   def login(self):
       self.boot()
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"))).send_keys("Admin")
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"))).send_keys("admin123")
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"))).send_keys("Sankar narayanan Paramasivan")
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input"))).send_keys("P")
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"))).send_keys("")
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"))).click()
       sleep(10)
       
            
       
obj = Form("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.login()
obj.quit()