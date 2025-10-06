import pytest
from pages.page_checkout import Checkout
from file_data_loader import DataLoad
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.checkout
@pytest.mark.parametrize(
    "name, email",
    DataLoad().json_load_checkout("data/data_coffee.json")
)
def test_checkout(driver, name, email):
    checkout = Checkout(driver)
    
    driver.get("https://coffee-cart.app/")
    
    checkout.checkout(name, email)
    
    confirmation = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]'))
    )

    assert "Thanks for your purchase" in confirmation.text