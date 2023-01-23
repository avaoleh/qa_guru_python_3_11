"""
Переопределите параметр с помощью indirect
Добавить параметры в фикстуру сторон браузера и запускать тесты в зависимости от сторон
"""

import pytest
from selene.support.shared import browser
from model.pages.github_page import *


@pytest.fixture(params=["desktop", "mobile"])
def browser_configuration(request):
    if request.param == "desktop":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == "mobile":
        browser.config.window_width = 375
        browser.config.window_height = 667


@pytest.mark.parametrize("browser_configuration", ["desktop"], indirect=True)
def test_github_desktop(browser_configuration):
    open_page()
    click_button_sign_in()
    check_header_sign_in()
    browser.close()


@pytest.mark.parametrize("browser_configuration", ["mobile"], indirect=True)
def test_github_mobile(browser_configuration):
    open_page()
    click_button_hamburger()
    click_button_sign_in()
    check_header_sign_in()
