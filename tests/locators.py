from selenium.webdriver.common.by import By

ZIP_INPUT = (By.CSS_SELECTOR, "[data-autotest-input-0]")
ZIP_SUBMIT = (By.CSS_SELECTOR, "[data-autotest-button-submit-0]")
CABINETS = (By.CSS_SELECTOR, "[data-autotest-checkbox-updates-cabinets] + label")
WORK_REPLACE_ALL = (By.CSS_SELECTOR, "[data-autotest-radio-worktype-replaceall] + label")
PROPERTY_SINGLE = (By.CSS_SELECTOR, "[data-autotest-radio-propertytype-single] + label")
MOBILE_HOME_NO = (By.CSS_SELECTOR, "[data-autotest-radio-internalmobilehome-no] + label")
OWNER_YES = (By.CSS_SELECTOR, "[data-autotest-radio-owner-yes] + label")
KITCHEN_SIZE = (By.CSS_SELECTOR, "[data-autotest-input-squarefeet-tel]")
BUDGET_10_30K = (
    By.XPATH,
    "//input[@name='budget']/following-sibling::label[normalize-space()='$10K to $30K']",
)
FULL_NAME = (By.CSS_SELECTOR, "[data-autotest-input-fullname-text]")
EMAIL = (By.CSS_SELECTOR, "[data-autotest-input-email-text]")
PHONE = (By.CSS_SELECTOR, "[data-autotest-input-phonenumber-tel]")
SUBMIT_REQUEST = (By.CSS_SELECTOR, "[data-autotest-button-submit-submit-my-request]")
PHONE_IS_CORRECT = (By.CSS_SELECTOR, "[data-autotest-button-submit-phone-number-is-correct]")
NEXT_BUTTON = (By.CSS_SELECTOR, "[data-autotest-button-button-next]")
NEXT_SUBMIT = (By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
