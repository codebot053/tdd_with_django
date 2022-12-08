from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# 3.0 방식
browser = webdriver.Chrome('./chromedriver')
# 4.0 방식
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('http://localhost:8000')