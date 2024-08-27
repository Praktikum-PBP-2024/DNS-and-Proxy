import os
import requests
import csv
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Cloudflare API credentials from environment variables
api_token = os.getenv('CLOUDFLARE_API_TOKEN')
zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
ip_address = os.getenv('IP_ADDRESS') 

# Headers for the API request
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# API endpoint to create a DNS record
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'



with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # DNS record details
        record_type = 'A'  # Can be A, AAAA, CNAME, etc.
        record_name = f'{row[0]}.shariyl.cloud'
        record_content = ip_address  # The IP address or value for the DNS record
        ttl = 1  # Time to live, set auto
        proxied = False  # Whether the record is proxied through Cloudflare

        # The data for the DNS record
        data = {
            'type': record_type,
            'name': record_name,
            'content': record_content,
            'ttl': ttl,
            'proxied': proxied
        }

        # Make the API request to create the record
        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            print("DNS record created successfully.")
            print(response.json())
        else:
            print("Failed to create DNS record.")
            print(f"Status Code: {response.status_code}")
            print(response.json())
