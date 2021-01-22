from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import pytest

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('--headless')
    return firefox_options

@pytest.fixture
def selenium(selenium):
    selenium.get("http://127.0.0.1:8787/")
    return selenium

def test_title(selenium):
    assert selenium.title == 'RStudio'

def test_version(selenium):
    console = WebDriverWait(selenium, timeout=30).until(rstudio_console_is_ready)
    assert console.text[10:15] == '3.6.3'

def rstudio_console_is_ready(webdriver):
    try:
        element = webdriver.find_element(By.XPATH, '//*[@id="rstudio_console_output"]')
        if element.text:
            return element
        else:
            return None
    except:
        return None
