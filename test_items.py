from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    basket_class = browser.find_element_by_css_selector("#add_to_basket_form > button")
    basket = basket_class.get_attribute("class")
    assert basket == "btn btn-lg btn-primary btn-add-to-basket", "Button does not found!"
    basket_button = WebDriverWait(browser, 3).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "Button doesn't exist")
