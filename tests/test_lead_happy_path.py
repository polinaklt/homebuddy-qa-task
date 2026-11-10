import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators as loc

BASE_URL = "https://hb-test.stage.sirenltd.dev/"
API_URL = "https://api-test.stage.sirenltd.dev/v1/public/leads"
TIMEOUT = 15

TEST_DATA = {
    "zip": "10001",
    "first_name": "Polina",
    "full_name": "Polina Test",
    "email": f"polina.test+{int(time.time())}@example.com",
    "phone": "3125550111",
    "kitchen_size": "200",
}


def click(wait, locator):
    wait.until(EC.element_to_be_clickable(locator)).click()


def type_text(wait, locator, text):
    field = wait.until(EC.element_to_be_clickable(locator))
    field.clear()
    field.send_keys(text)


@pytest.fixture(scope="module")
def driver():
    drv = webdriver.Chrome()
    drv.set_window_size(1440, 900)
    yield drv
    drv.quit()


@pytest.fixture(scope="module")
def submitted_lead(driver):
    wait = WebDriverWait(driver, TIMEOUT)
    driver.get(BASE_URL)

    type_text(wait, loc.ZIP_INPUT, TEST_DATA["zip"])
    click(wait, loc.ZIP_SUBMIT)

    click(wait, loc.CABINETS)
    lead_id = driver.execute_script("return window.leadResponse.uuid")
    click(wait, loc.NEXT_BUTTON)

    click(wait, loc.WORK_REPLACE_ALL)
    click(wait, loc.NEXT_SUBMIT)

    click(wait, loc.PROPERTY_SINGLE)
    click(wait, loc.NEXT_SUBMIT)

    click(wait, loc.MOBILE_HOME_NO)
    click(wait, loc.NEXT_SUBMIT)

    click(wait, loc.OWNER_YES)
    click(wait, loc.NEXT_BUTTON)

    type_text(wait, loc.KITCHEN_SIZE, TEST_DATA["kitchen_size"])
    click(wait, loc.NEXT_SUBMIT)

    click(wait, loc.BUDGET_10_30K)
    click(wait, loc.NEXT_SUBMIT)

    type_text(wait, loc.FULL_NAME, TEST_DATA["full_name"])
    type_text(wait, loc.EMAIL, TEST_DATA["email"])
    click(wait, loc.NEXT_SUBMIT)

    type_text(wait, loc.PHONE, TEST_DATA["phone"])
    click(wait, loc.SUBMIT_REQUEST)

    click(wait, loc.PHONE_IS_CORRECT)

    wait.until(EC.url_contains("/thank-you"))
    return driver, lead_id


def test_thank_you_page_is_shown(submitted_lead):
    driver, _ = submitted_lead
    body = driver.find_element(By.TAG_NAME, "body").text
    assert "/thank-you" in driver.current_url
    assert "Thank you" in body


@pytest.mark.xfail(reason="DEF-05: thank-you page shows 'Andrew' instead of the entered name")
def test_thank_you_page_shows_entered_name(submitted_lead):
    driver, _ = submitted_lead
    body = driver.find_element(By.TAG_NAME, "body").text
    assert f"Thank you {TEST_DATA['first_name']}" in body


@pytest.mark.xfail(reason="DEF-01: thank-you page is shown, but the lead status is FAILED")
def test_lead_status_is_submitted(submitted_lead):
    _, lead_id = submitted_lead
    lead = requests.get(f"{API_URL}/{lead_id}").json()
    assert lead["leadStatus"] == "SUBMITTED"
