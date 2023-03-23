import requests

url = 'https://www.valueresearchonline.com/downloads/amfi-performance-xls/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'X-Requested-With': 'XMLHttpRequest'
}
download_folder = "downloads"

dropdown1_options = ["1","2"]
dropdown2_options = ["SEQ","SDT"]
dropdown3_options = ["SEQ_LC", "SEQ_LMC"]
dropdown4_options = ["4","8799"]
date = "20-Mar-2023"

for dropdown1_value in dropdown1_options:
    for dropdown2_value in dropdown2_options:
        for dropdown3_value in dropdown3_options:
            for dropdown4_value in dropdown4_options:
                source_url = f'/amfi/fund-performance-data/?end-type={dropdown1_value}&primary-category={dropdown2_value}&category={dropdown3_value}&amc={dropdown4_value}&nav-date={date}'
                params = {'source_url': source_url}

                print(params)
                response = requests.get(url, headers=headers, params=params)
                
                filename = f"{download_folder}/file_{dropdown1_value}_{dropdown2_value}_{dropdown3_value}_{dropdown4_value}.xls"

                
                if response.status_code == 200:
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                        print("File downloaded successfully.")
                else:
                    print(f"Failed to download file. Status code: {response.status_code}")



