import argparse
import requests
import pandas as pd
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Proxy Scraper')
parser.add_argument('request', choices=['displayproxies', 'getproxies'], help="Specify the request type ("
                                                                              "displayproxies or getproxies")
parser.add_argument('--protocol', default='all', help='Specify the protocol (all, http, socks4, socks5')
parser.add_argument('--timeout', type=int, default=10000, help='Specify the timeout in milliseconds')
parser.add_argument('--country', default='all', help="Specify the country ('US', 'FI', 'DE', 'IR', 'CO', 'CN', 'IT', "
                                                     "'BR', 'FR', 'UA', 'RS', 'JP', 'EG', 'MN', 'GE', 'TW', 'CA', "
                                                     "'ZA', 'ID', 'PE', 'VE', 'GB', 'BD', 'VN', 'SG', 'AU', 'MY', "
                                                     "'IN', 'GH', 'NL', 'NG', 'RU', 'PL', 'CZ', 'PH', 'AZ', 'NP', "
                                                     "'KH', 'IQ', 'TH', 'AR', 'PT', 'MX', 'BO', 'EC', 'KR', 'TZ', "
                                                     "'BG', 'MZ', 'TR', 'HK', 'CR', 'PS', 'ES', 'UZ', 'NI', 'KE', "
                                                     "'PK', 'HU')")
parser.add_argument('--ssl', default='all', help='Specify the SSL option (all, yes, no)')
parser.add_argument('--anonymity', default='all',
                    help='Specify the anonymity level (all, anonymous, transparent, elite')
args = parser.parse_args()

# Construct the request URL
base_url = 'https://api.proxyscrape.com/v2/?request='
url = f'{base_url}{args.request}&protocol={args.protocol}&timeout={args.timeout}&country={args.country}' \
      f'&ssl={args.ssl}&anonymity={args.anonymity}'

# Make a request to the API
response = requests.get(url)

# Split the response into lines
lines = response.text.splitlines()

# Create a list of dictionaries for each proxy
proxies = []
for line in lines:
    proxy_data = line.split(":")
    proxy = {
        "IP": proxy_data[0],
        "Port": proxy_data[1]
    }
    proxies.append(proxy)

# Create a DataFrame from the list of proxies
df = pd.DataFrame(proxies)

# Save DataFrame to CSV file
df.to_csv("proxies.csv", index=False)

# Display usage message to the user
print(f"Proxies saved to 'proxies.csv'")
print("Example usage: python proxy_scraper.py displayproxies --protocol http --timeout 10000 --country all --ssl all "
      "--anonymity all")
