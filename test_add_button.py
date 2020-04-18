from selenium import webdriver
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    basket = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert basket == "btn btn-lg btn-primary btn-add-to-basket", "Element not found!!!"


