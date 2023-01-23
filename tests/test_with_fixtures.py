"""
Сделайте разные фикстуры для каждого теста
"""

from model.pages.github_page import *


def test_github_desktop(browser_config_desktop):
    open_page()
    click_button_sign_in()
    check_header_sign_in()


def test_github_mobile(browser_config_mobile):
    open_page()
    click_button_hamburger()
    click_button_sign_in()
    check_header_sign_in()