import requests
from bs4 import BeautifulSoup
import pandas as pd
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = "https://www.pnbindia.in/interst-rate-on-advances-linked-to-mclr.html"

r = requests.get(url, verify=False, headers=HEADERS)

soup=BeautifulSoup(r.text,"html.parser") 

div_table = soup.find_all('div',id="fa-tab1321")[0]
table = div_table.find("table")
# print(table)

heading = table.find_all("tr")[1]


list_header = []
data = []

for items in heading:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = table.find_all("tr")[2:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.to_csv('pnb.csv')