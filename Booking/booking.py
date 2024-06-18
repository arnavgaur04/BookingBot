from types import TracebackType
from typing import Type
import time
import Booking.constants as cons
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        # This helps in Chrome.
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        super(Booking, self).__init__(options=options)
        self.implicitly_wait (10)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def landing_page(self):
        self.get(cons.BASE_URL)
    
    def dismiss_popup(self):
        try:
            popup = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]')
            popup.click()
        except:
            print("Not present.")

    def destination(self):
        place_to_go = input("Enter place you wanna go: ")
        dest = self.find_element(By.CSS_SELECTOR, 'input[aria-label="Where are you going?"]')
        dest.clear()
        dest.send_keys(f'{place_to_go}')
        time.sleep(2)
        first_result = self.find_element(By.ID, 'autocomplete-result-0')
        first_result.click()
        
    def date(self):
        from_date = input("Enter from date (DD MonthName Year): ")
        to_date = input("Enter to date (DD MonthName Year): ")
        fro = self.find_element(By.CSS_SELECTOR, f'span[aria-label="{from_date}"]')
        to = self.find_element(By.CSS_SELECTOR, f'span[aria-label="{to_date}"]')
        fro.click()
        to.click()

    def submit_button(self):
        submit_btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()

    def getData(self):
        hotels = self.find_elements(By.CSS_SELECTOR, 'div[aria-label="Property"]')
        for hotel in hotels:
            title = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
            try:
                rating = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]')
                rating = rating.text.split(' ')[0].splitlines()[0]
            except:
                rating = "New"
            price = hotel.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]')
            print(f'Hotel Name: {title.text}')
            print(f'Rating: {rating}')
            print(f'Price: {price.text}')
            print()
