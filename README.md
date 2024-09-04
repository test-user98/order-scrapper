# order-scrapper
Scrapping Amazon Order page and storing HTML and order insights

**Overview**
This project scrapes order details from the Amazon Orders page. It automates the process of extracting order information and saving it into JSON files for each order. The scraping is done using Selenium WebDriver and BeautifulSoup.

**Features**
_Login Automation_: Handles login to the Amazon account.
_Order Extraction_: Retrieves order details including date, summary link, shipping address, order price, product description, and delivery status.
_File Storage:_ Saves the extracted information in JSON files organized by order ID.
_Pagination Handling_: Navigates through multiple pages of orders.

**File Structure**
_main.py:_ Main script to start the scraping process.
_config.py:_ Configuration file with paths and constants.
_utils.py:_ Utility functions used across the project.
_scraper.py_: Contains functions to initialize the WebDriver and handle the scraping logic.
_data_extraction.py:_ Functions for parsing and extracting data from HTML.
