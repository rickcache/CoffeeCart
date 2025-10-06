from selenium.webdriver.common.by import By
from pages.page_add_coffee import Coffee
from pages.page_cart_total_items import Cart
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import logging


@pytest.mark.coffee

def test_coffee_to_cart(driver):
    coffee = Coffee(driver)
    cart   = Cart(driver)
    
    logging.info("Directing to the website")
    driver.get("https://coffee-cart.app/")
    
    
    logging.info("Adding Coffee")
    coffee.add_coffee()
    
    total_coffee = coffee.count_added()
    
    logging.info("Directing to the Cart Page")
    cart_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/ul/li[2]/a'))
    )
    cart_page.click()
    
    total_coffee_cart   = cart.total_items()
    
    logging.info("Testing the success of the Coffee Carting Test")
    assert total_coffee == total_coffee_cart, f"Expected {total_coffee}, found {total_coffee_cart}"
    
    logging.info(f"Cart contains all {total_coffee} coffee")
    
    