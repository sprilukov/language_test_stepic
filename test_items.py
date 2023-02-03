import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage1():

    def test_btn_add(self, browser):
        browser.get(link)
        time.sleep(30)
        x = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert x , 'Кнопка не найдена!'
        time.sleep(4)
