
=from scraper.driver_setup import initialize_driver
from scraper.order_processor import process_all_orders

def main():
    driver = initialize_driver()
    
    try:
        driver.get("https://www.amazon.in/your-orders/orders")
        print("Navigated to Amazon Orders page")

        input("Please complete the sign-in process and press Enter to continue...")

        process_all_orders(driver)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()
