from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class Cart:
    def __init__(self, driver):
        self.driver = driver 
        self.item_path = (By.XPATH, '//*[@id="app"]/div[2]/div/ul/li[position()>1]')
        
    def total_items(self):
        
        try:
          products = WebDriverWait(self.driver, 10).until(
              EC.presence_of_all_elements_located(self.item_path)
          ) 
          return len(products)   
        
        except NoSuchElementException:
          return 0
      

      