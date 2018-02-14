from selenium import webdriver
import sys
from time import sleep
sys.path.append("..")
from seleniumExample.pages.GooglePage import GooglePage

firefox = webdriver.Firefox()

newpage = GooglePage(firefox, "http://www.google.com")

newpage.search("Cats")

sleep(10)

firefox.close()
quit()