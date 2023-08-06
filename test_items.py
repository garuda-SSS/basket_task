import pytest
from selenium.webdriver.common.by import By
import time


def test_abs1(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert len(browser.find_elements(By.CSS_SELECTOR,'.btn-add-to-basket'))>0, "Кнопка отсуствует"
