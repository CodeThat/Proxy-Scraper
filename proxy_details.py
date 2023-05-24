import requests
import pandas as pd
import json


def get_proxy_details():
    url = "https://api.proxyscrape.com/v2/?request=proxyinfo"
    response = requests.get(url)
    return response.text


# Get proxy details
proxy_details_json = get_proxy_details()

# Parse JSON string into a Python dictionary
proxy_details = json.loads(proxy_details_json)

# Define the expected headers
headers = ["proxy_count", "last_updated", "organizations", "ports", "countries"]

# Extract data from JSON response
data = [[proxy_details.get(header) for header in headers]]

# Convert data to DataFrame
df = pd.DataFrame(data, columns=headers)

# Output DataFrame to CSV file
df.to_csv("proxy_details.csv", index=False)
