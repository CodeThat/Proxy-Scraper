# Proxy Scraper

A script for scraping and saving proxies using the <href>ProxyScrape API</href>.

## Usage

```python proxy_scraper.py [request] [options]```

## Arguments
request: Specify the request type (displayproxies or getproxies)

Options
--protocol: Specify the protocol (all, http, socks4, socks5)
--timeout: Specify the timeout in milliseconds (default: 10000)
--country: Specify the country (e.g., US, FI, DE, ...)
--ssl: Specify the SSL option (all, yes, no)
--anonymity: Specify the anonymity level (all, anonymous, transparent, elite)

## Installation
1. Clone the repository:

```git clone https://github.com/your-username/proxy-scraper.git```

2. Navigate to the project directory:
```cd proxy-scraper```


3. Install the required dependencies:
```pip install -r requirements.txt```

Examples
- Scrape and save proxies with default options:
  shell
```python proxy_scraper.py displayproxies```
- Save and scrape proxies
```python proxy_scraper.py displayproxies --protocol http --timeout 10000 --country all --ssl all --anonymity all```




