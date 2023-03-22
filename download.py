import os
import requests

url = "https://www.valueresearchonline.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

download_folder = "downloads"

dropdown1_options = ["1","2"]
dropdown2_options = ["SEQ","SDT","SHY"]
dropdown3_options = ["SEQ_LC", "SEQ_LMC", "SEQ_MC"]
dropdown4_options = ["4","8799","298","332"]
date = "20-Mar-2023"

for dropdown1_value in dropdown1_options:
    for dropdown2_value in dropdown2_options:
        for dropdown3_value in dropdown3_options:
            download_url = f"{url}/downloads/amfi-performance-xls/?source_url=/amfi/fund-performance-data/?end-type={dropdown1_value}&primary-category={dropdown2_value}&category={dropdown3_value}&amc={dropdown3_value}&nav-date={date}"
            response = requests.get(download_url, headers=headers)
            
            filename = f"file_{dropdown1_value}_{dropdown2_value}_{dropdown3_value}.xlsx"
            
            with open(filename, 'wb') as f:
                f.write(response.content)
                
            print(f"Downloaded file: {filename}")

    