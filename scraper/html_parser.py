import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

template_dir = 'order_details_files_optimised'
if not os.path.exists(template_dir):
    os.makedirs(template_dir)

def save_order_details(driver, order_id, order_url):
    print(f"Attempting to extract details for order {order_id}")
    current_window = driver.current_window_handle
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(order_url)
    
    order_details = {
        "orderID": order_id,
        "orderDate": "",
        "orderSummaryLink": "",
        "shippingAddress": "",
        "orderPrice": "",
        "productDescription": "",
        "deliveryStatus": ""
    }
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "orderDetails"))
        )
        
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        order_date_invoice_div = soup.find('div', attrs={'data-component': 'orderDateInvoice'})
        if order_date_invoice_div:
            order_date_span = order_date_invoice_div.find('span', class_='order-date-invoice-item')
            if order_date_span:
                order_details["orderDate"] = order_date_span.get_text(strip=True)
            
            ul_elements = order_date_invoice_div.find_all('ul', class_='a-unordered-list a-vertical a-nowrap')
            if len(ul_elements) > 2:
                third_li = ul_elements[2].find('li')
                if third_li:
                    link = third_li.find('a')
                    if link and link.has_attr('href'):
                        order_summary_link = link['href']
                        order_details["orderSummaryLink"] = order_summary_link
                        parsed_url = urlparse(order_summary_link)
                        query_params = parse_qs(parsed_url.query)
                        order_details["orderID"] = query_params.get('orderID', [order_id])[0]

        payment_details_div = soup.find('div', attrs={'data-component': 'paymentDetails'})
        if payment_details_div:
            ul = payment_details_div.find('ul', class_='displayAddressUL')
            if ul:
                address_items = ul.find_all('li')
                order_details["shippingAddress"] = ' '.join([item.get_text(strip=True) for item in address_items])
            
            price_span = payment_details_div.find('span', class_='currencyINR')
            if not price_span:
                price_span = payment_details_div.find('span', class_='currencyINRFallback')
            if price_span:
                order_details["orderPrice"] = price_span.get_text(strip=True)

        shipments_div = soup.find('div', attrs={'data-component': 'shipments'})
        if shipments_div:
            shipment_top_row = shipments_div.find('div', class_='shipment-top-row')
            if shipment_top_row:
                delivery_status_span = shipment_top_row.find('span', class_='a-size-medium')
                if delivery_status_span:
                    order_details["deliveryStatus"] = delivery_status_span.get_text(strip=True)
            
            img_tag = shipments_div.find('img')
            if img_tag and img_tag.has_attr('title'):
                order_details["productDescription"] = img_tag['title']

        json_file_path = os.path.join(template_dir, f"{order_id}_details.json")
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(order_details, json_file, ensure_ascii=False, indent=4)
        print(f"Saved details for order {order_id}")
    
    except Exception as e:
        print(f"Error extracting details for order {order_id}: {str(e)}")
    
    finally:
        driver.close()
        driver.switch_to.window(current_window)
