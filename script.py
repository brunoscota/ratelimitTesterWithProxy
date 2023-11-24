import requests
import time
import os

# Read proxy configuration from environment variables
proxy_user = os.getenv('PROXY_USER')
proxy_pass = os.getenv('PROXY_PASS')
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT', '1080')  # Default port 1080
proxy_url = f'socks5://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}'
tested_url = os.getenv('TESTED_URL')
rate_limit = int(os.getenv('RATE_LIMIT', 100))  # Convert RATE_LIMIT to integer
interval = float(os.getenv('INTERVAL', 60 / rate_limit))  # Convert INTERVAL to float

# Setting up the SOCKS5 Proxy
session = requests.Session()
session.proxies = {'http': proxy_url, 'https': proxy_url}

# Rest of your configuration
url = tested_url

# Function to send requests
def send_request():
    response = session.get(url)
    return response.status_code

# Main loop
for i in range(rate_limit):
    status = send_request()
    print(f"Request {i+1}, Status Code: {status}")
    time.sleep(interval)
