import requests

url = 'https://www.valueresearchonline.com/downloads/amfi-performance-xls/'
params = {
    'source_url': '/amfi/fund-performance-data/?end-type=1&primary-category=SEQ&category=SEQ_LC&amc=ALL&nav-date=21-Mar-2023'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'X-Requested-With': 'XMLHttpRequest'
}

print(url)

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    with open('amfi.xls', 'wb') as f:
        f.write(response.content)
        print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")