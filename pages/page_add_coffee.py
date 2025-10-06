from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Coffee:
    def __init__(self, driver):
        self.driver = driver
        self.coffee_path = (By.XPATH, '//*[@id="app"]/div[2]/ul/li/div')
        self.added_count = 0

    def handle_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[2]/button[2]'))
            )
            close_button.click()
            print("Popup appeared and closed!")
            self.added_count += 1  
        except TimeoutException:
            self.added_count += 1  

    def add_coffee(self):
        self.added_count = 0
        for i in range(1, 10):
            coffee = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="app"]/div[2]/ul/li[{i}]/div'))
            )
            coffee.click()
            self.handle_popup()  

    def count_added(self):
        return self.added_count


    
              
    
        