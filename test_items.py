import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        button.click()
        time.sleep(4)
