from selenium import webdriver
from selenium.webdriver.common.by import By

class table_became_empty:

    def __call__(self, driver: webdriver.Chrome):    
        rows = driver.find_elements(By.CSS_SELECTOR, "#locations-table-tbody > tr")
        return len(rows) == 0