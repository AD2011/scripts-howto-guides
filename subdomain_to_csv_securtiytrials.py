import requests
import pandas as pd
import json

apikey = input("Enter your SecurityTrials API Key:")
domain = input('Enter your domain:')

url = f'https://api.securitytrails.com/v1/domain/{domain}/subdomains?children_only=false&include_inactive=false'

headers = {
    "accept": "application/json",
    "APIKEY": apikey
}

response = requests.get(url, headers=headers)
results1 = json.loads(response.text)
subd = results1["subdomains"]
subdomains=[]
for item in (subd):
    subdomains.append(item+'.'+domain)


# Create a DataFrame from the subdomains list
df = pd.DataFrame(subdomains, columns=['Subdomain'])

# Save the DataFrame as a CSV file
filename = f"{domain}_subdomains.csv"
df.to_csv(filename, index=False)

print("File Saved")