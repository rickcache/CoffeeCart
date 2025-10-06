from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WB

class Checkout:

    def __init__(self, driver):
        self.driver = driver
        self.coffee_path = (By.XPATH, '//*[@id="app"]/div[2]/ul/li/div')
        self.checkout_path = (By.XPATH, '//*[@id="app"]/div[2]/div[1]')
        self.name_box    = (By.XPATH, '//*[@id="name"]')
        self.email_box   = (By.XPATH, '//*[@id="email"]')
        self.check_box   = (By.XPATH, '//*[@id="promotion"]')
        self.submit      = (By.XPATH, '//*[@id="submit-payment"]')
        
        
    def checkout(self, name, email):
        
        #add products
        for i in range(1, 3):
            product = WB(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="app"]/div[2]/ul/li[{i}]/div'))
        )
            product.click()
        
        #checkout initailize    
        checkout_btn = WB(self.driver, 10).until(
            EC.element_to_be_clickable((self.checkout_path))
        )   
        checkout_btn.click()
        
        #forms fill up
        names_input = WB(self.driver, 10).until(
            EC.presence_of_element_located((self.name_box))
        )
        names_input.send_keys(name)
        
        email_input = WB(self.driver, 10).until(
            EC.presence_of_element_located((self.email_box))
        )
        email_input.send_keys(email)
        
        check =  WB(self.driver, 10).until(
            EC.element_to_be_clickable((self.check_box))
        )
        check.click()
        
        submit = WB(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit)
        )
        submit.click()  
                                  
                                                    
            