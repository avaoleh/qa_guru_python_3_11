"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот) с помощью марки скип
"""
import pytest
from selene.support.shared import browser
from model.pages.github_page import *


@pytest.mark.parametrize("width, height", [pytest.param(1920, 1080, id='Browser size: 1920x1080'),
                                           pytest.param(375, 667, id='Browser size: 375x667')
                                           ])
def test_github_desktop(width, height):
    if width == 375:
        pytest.skip("Размер окна под мобильную версию!")
    browser.config.window_width = width
    browser.config.window_height = height
    open_page()
    click_button_sign_in()
    check_header_sign_in()


@pytest.mark.parametrize("width, height", [pytest.param(1920, 1080), pytest.param(375, 667)])
def test_github_mobile(width, height):
    if width == 1920:
        pytest.skip("Размер окна под десктопную версию!")
    browser.config.window_width = width
    browser.config.window_height = height
    open_page()
    click_button_hamburger()
    click_button_sign_in()
    check_header_sign_in()
