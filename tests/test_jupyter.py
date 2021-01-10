from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path

import pytest
import json

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('--headless')
    return firefox_options

def test_notebook_and_share_volume(selenium):
    selenium.get("http://127.0.0.1:8888/tree/share/")
    share_window = selenium.current_window_handle
    wait = WebDriverWait(selenium, timeout=30)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="new-buttons"]'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="kernel-python3"]'))).click()
    wait.until(ec.number_of_windows_to_be(2))

    for window_handle in selenium.window_handles:
        if window_handle != share_window:
            selenium.switch_to.window(window_handle)
            break

    test_msg = "Hello World"
    run_btn_locator = (By.XPATH, '//*[@id="run_int"]/button[1]')
    input_area_locator = (By.XPATH, '//*[@id="notebook-container"]/div/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]')
    notification_area_locator = (By.XPATH, '//*[@id="notification_notebook"]/span')
    save_btn_locator = (By.XPATH, '//*[@id="save-notbook"]/button')
    input_textarea_locator = (By.XPATH, '//*[@id="notebook-container"]/div/div[1]/div[2]/div[2]/div/div[1]/textarea')
    output_textarea_locator = (By.XPATH, '//*[@id="notebook-container"]/div[1]/div[2]/div[2]/div/div[3]/pre')

    run_btn = wait.until(ec.element_to_be_clickable(run_btn_locator))
    save_btn = wait.until(ec.element_to_be_clickable(save_btn_locator))
    notification_area = selenium.find_element(*notification_area_locator)

    input_area = wait.until(ec.element_to_be_clickable(input_area_locator))
    input_area.click()
    input_textarea = selenium.find_element(*input_textarea_locator)
    input_textarea.send_keys('print("' + test_msg + '")')
    run_btn.click()

    try:
        output_textarea = wait.until(ec.visibility_of_element_located(output_textarea_locator))
    except:
        input_area.click()
        run_btn.click()
        output_textarea = wait.until(ec.visibility_of_element_located(output_textarea_locator))

    save_btn.click()
    wait.until(ec.visibility_of(notification_area))
    assert output_textarea.text == test_msg

    p = Path('/tmp/share/Untitled.ipynb')
    assert p.is_file()
    result = json.loads(p.read_text())['cells'][0]['outputs'][0]['text'][0].strip()
    assert result == test_msg
