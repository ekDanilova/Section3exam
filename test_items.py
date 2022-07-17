from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_find_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")

    assert button.is_displayed(), "Кнопка добавления товара в корзину отсутсвует"
    print ("Хорошего дня, коллега!")


