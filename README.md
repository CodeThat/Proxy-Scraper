# Proxy Scraper

A script for scraping and saving proxies using the ProxyScrape API.

## Usage

```shell
'''python proxy_scraper.py [request] [options]'''

## Arguments
request: Specify the request type (displayproxies or getproxies)

Options
--protocol: Specify the protocol (all, http, socks4, socks5)
--timeout: Specify the timeout in milliseconds (default: 10000)
--country: Specify the country (e.g., US, FI, DE, ...)
--ssl: Specify the SSL option (all, yes, no)
--anonymity: Specify the anonymity level (all, anonymous, transparent, elite)

## Installation
Clone the repository:

'''git clone https://github.com/your-username/proxy-scraper.git'''

Navigate to the project directory:
'''cd proxy-scraper'''


Install the required dependencies:

Examples
- Scrape and save proxies with default options:
  shell
'''python proxy_scraper.py displayproxies'''



