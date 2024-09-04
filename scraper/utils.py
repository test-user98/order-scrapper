from urllib.parse import parse_qs, urlparse

def extract_order_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('orderID', ['Unknown'])[0]
