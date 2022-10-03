import time
import logging
import argparse
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
 

option = webdriver.FirefoxOptions()
option.add_argument('--headless')
driver = webdriver.Firefox(options=option)
program_version_number = "2022.1.0.0"
downloading_url = "https://getfvid.com"
update_check_endpoint = "https://api.github.com/repos/rly0nheart/facebook-downloader/releases/latest"


def notice():
    notice_msg = f"""
facebook-downloader {program_version_number} Copyright (C) 2022  Richard Mwewa

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
    print(notice_msg)


def check_and_get_updates():
    notice()
    response = requests.get(update_check_endpoint).json()
    if response['tag_name'] == program_version_number:
        """Ignore if the program is up to date"""
        pass
    else:
        update_prompt = input(f"[?] A new release is available ({response['tag_name']}). Would you like to install it? (y/n) ")
        if update_prompt.lower() == "y":
            files_to_update = ['downloader.py', 'geckodriver.exe', 'README.md', 'requirements.txt']
            for file in tqdm(files_to_update, desc=f'Updating'):
                data = requests.get(f'https://raw.githubusercontent.com/rly0nheart/facebook-downloader/master/{file}')
                with open(file, "wb") as f:
                    f.write(data.content)
                    f.close()
            print("Updated: Re-run program.")
        else:
            pass
    
        
def download_video(url, output):
    driver.get(downloading_url) # Opening getfvid.com, a website that downloads facebook videos
    url_entry_field = driver.find_element(By.NAME, "url") # Find the url entry field
    url_entry_field.send_keys(url) # write facebook url in the entry field
    url_entry_field.send_keys(Keys.ENTER) # press enter
    print('Please standby (20 seconds)...')
    time.sleep(20) # Sleep for at least 20 seconds to wait for the next page to load
    driver.refresh
    
    """
    HD: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a"
    SD: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[2]/a"
    Audio: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[3]/a"
    """

    download_btn = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a'))) # Find the download button (this clicks the first button which returns a video in hd)
    download_url = download_btn.get_attribute('href')
    
    with requests.get(download_url, stream=True) as response:
        response.raise_for_status()
        with open(f'downloads/{output}.mp4', 'wb') as file:
            for chunk in tqdm(response.iter_content(chunk_size=8192), desc=f'Downloading: {output}.mp4'): 
                file.write(chunk)
        print(f'Downloaded: {file.name}')
    driver.close()


parser = argparse.ArgumentParser(description='facebook-downloader — by Richard Mwewa')
parser.add_argument('url', help='facebook video url (eg. https://www.facebook.com/PageName/videos/VideoID')
parser.add_argument('-A', '--audio', help=argparse.SUPPRESS, action='store_true')
parser.add_argument('-o', '--output', help='output filename')
parser.add_argument('-v', '--version', version='2022.1.0.0', action='version')
args = parser.parse_args()
url = args.url
output = args.output


if __name__ == "__main__":
    try:
        check_and_get_updates()
        download_video(url, output)

    except KeyboardInterrupt:
        print('Process interrupted with Ctrl+C.')

    except Exception as e:
        print('An error occured:', e)