from selenium import webdriver
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert 'Ajouter au panier' == button.text, 'Текст не соответсвует'


