# order-scrapper
Scrapping Amazon Order page and storing HTML and order insights

Certainly! Here’s a README file formatted properly for clarity:

---

# Amazon Order Scraper

## Overview

This project scrapes order details from the Amazon Orders page. It automates the process of extracting order information and saving it into JSON files for each order. The scraping is done using Selenium WebDriver and BeautifulSoup.

## Features

- **Login Automation**: Handles login to the Amazon account.
- **Order Extraction**: Retrieves order details including date, summary link, shipping address, order price, product description, and delivery status.
- **File Storage**: Saves the extracted information in JSON files organized by order ID.
- **Pagination Handling**: Navigates through multiple pages of orders.

## File Structure

- `main.py`: Main script to start the scraping process.
- `config.py`: Configuration file with paths and constants.
- `utils.py`: Utility functions used across the project.
- `scraper.py`: Contains functions to initialize the WebDriver and handle the scraping logic.
- `data_extraction.py`: Functions for parsing and extracting data from HTML.

## Setup

1. **Install Dependencies**: Ensure you have the necessary Python packages. Install them using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download ChromeDriver**: Ensure you have the ChromeDriver executable downloaded and update the path in `config.py`.

3. **Configuration**: Update `config.py` with your ChromeDriver path and the directory where order details will be saved.

## Usage

1. **Run the Script**: Execute `main.py` to start the scraping process:
   ```bash
   python main.py
   ```

2. **Login**: Complete the sign-in process on the Amazon Orders page as prompted by the script.

3. **Scraping**: The script will navigate through the orders, extract details, and save them into JSON files in the specified directory.

## Flow

1. **Initialize WebDriver**: Set up ChromeDriver with specified options.

2. **Navigate to Orders Page**: Open the Amazon Orders page and wait for user login.

3. **Scrape Orders**: For each order on the page:
   - Open the order details in a new window.
   - Extract relevant information using BeautifulSoup.
   - Save the information to a JSON file.

4. **Pagination Handling**: Automatically navigate to the next page of orders until no more pages are available.

5. **Cleanup**: Close the WebDriver once all pages have been processed.

## Contributing

Feel free to submit issues or pull requests to enhance the functionality of the scraper.

## License

This project is licensed under the MIT License.

---

You can copy and paste this into your `README.md` file for clear and structured documentation.
