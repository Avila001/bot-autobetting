from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome(executable_path="C:\Python39\chromedriver.exe", options=chrome_options)

driver.maximize_window()