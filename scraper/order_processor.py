import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .utils import extract_order_id
from .html_parser import save_order_details

def wait_for_orders_to_load(driver):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".order-card.js-order-card"))
    )
    time.sleep(2)  # Additional wait to ensure all orders are loaded

def process_orders_on_page(driver):
    wait_for_orders_to_load(driver)
    order_cards = driver.find_elements(By.CSS_SELECTOR, ".order-card.js-order-card")
    print(f"Found {len(order_cards)} order cards on this page")
    
    for index, order_card in enumerate(order_cards, start=1):
        try:
            order_links = order_card.find_elements(By.CSS_SELECTOR, "a[href*='order-details']")
            if not order_links:
                print(f"No order link found for order {index}")
                continue
            order_url = order_links[0].get_attribute("href")
            order_id = extract_order_id(order_url)
            print(f"Processing order {index} with ID {order_id}")
            save_order_details(driver, order_id, order_url)
        except Exception as e:
            print(f"Error processing order {index}: {str(e)}")

def process_all_orders(driver):
    page_number = 1
    while True:
        print(f"Processing page {page_number}")
        process_orders_on_page(driver)

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.a-pagination li.a-last:not(.a-disabled) a"))
            )
            next_button.click()
            print("Navigating to the next page")
            time.sleep(5)
            page_number += 1
        except Exception as e:
            print("No more pages or error navigating:", str(e))
            break

    print("All order details have been processed.")
