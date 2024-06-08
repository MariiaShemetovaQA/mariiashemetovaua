from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage(BasePage):
    URL = 'https://www.ns.nl/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(HomePage.URL)

    def find_route(self, start_point, end_point):
        btn_elem = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        btn_elem.click()

        from_elem = self.driver.find_element(By.ID, "location-input-FROM-POSITIONED")
        from_elem.send_keys(start_point)
        time.sleep(2)
        from_elem.send_keys(Keys.ARROW_DOWN)
        from_elem.send_keys(Keys.RETURN)

        to_elem = self.driver.find_element(By.ID, "location-input-TO-POSITIONED")
        to_elem.send_keys(end_point)
        to_elem.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        to_elem.send_keys(Keys.RETURN)  
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()

    def check_route_title(self, expected_title):
        actual_title = self.driver.title
        print(f"Actual title: {actual_title}")
        return self.driver.title == expected_title

    

    #def buy_ticket(self):
       # time.sleep(2)
       # btn_elem = self.driver.find_element(By.CSS_SELECTOR, "a[href*='/kaartjes/bestellen/kaartjes-kopen']")
       # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_elem)
       # time.sleep(1)
       # btn_elem.click()
    
   

    #def check_ticket_title(self, expected_title):
       # actual_title = self.driver.title
       # print(f"Actual title: {actual_title}")
       # return self.driver.title == expected_title