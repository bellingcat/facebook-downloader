import time
import logging
import argparse
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 

class FacebookDownloader:

    def __init__(self, args):
        self.option = webdriver.FirefoxOptions()
        self.option.add_argument('--headless')
        self.driver = webdriver.Firefox(options=self.option)
        self.program_version_number = "2022.1.0.0"
        self.downloading_url = "https://getfvid.com"
        self.update_check_endpoint = "https://api.github.com/repos/rly0nheart/Facebook-Downloader/releases/latest"


    def notice(self):
        notice_msg = f"""
    Facebook-Downloader {self.program_version_number} Copyright (C) 2022  Richard Mwewa

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    """
        return notice_msg


    def check_and_get_updates(self):
        print(self.notice())
        response = requests.get(self.update_check_endpoint).json()
        if response['tag_name'] == self.program_version_number:
            """Ignore if the program is up to date"""
            pass
        else:
            update_prompt = input(f"[?] A new release is available ({response['tag_name']}). Would you like to install it? (y/n) ")
            if update_prompt.lower() == "y":
                files_to_update = ['downloader.py', 'geckodriver.exe', 'README.md', 'requirements.txt']
                for file in tqdm(files_to_update, desc=f'Updating'):
                    data = requests.get(f'https://raw.githubusercontent.com/rly0nheart/Facebook-Downloader/master/{file}')
                    with open(file, "wb") as f:
                        f.write(data.content)
                        f.close()
                exit(f"Updated: Re-run program.")
            else:
                pass
        
        
    def download_video(self):
        self.check_and_get_updates()
        self.driver.get(self.downloading_url) # Opening getfvid.com, a website that downloads facebook videos
        url_entry_field = self.driver.find_element(By.NAME, "url") # Find the url entry field
        url_entry_field.send_keys(args.url) # write facebook url in the entry field
        url_entry_field.send_keys(Keys.ENTER) # press enter
        time.sleep(20) # Sleep for at least 20 seconds to wait for the next page to load
        self.driver.refresh
        
        """
        HD: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a"
        SD: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[2]/a"
        Audio: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[3]/a"
        """

        download_btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a') # Find the download button (this clicks the first button which returns a video in hd)
        download_url = download_btn.get_attribute('href')
        
        with requests.get(download_url, stream=True) as response:
            response.raise_for_status()
            with open(f'downloads/{args.output}.mp4', 'wb') as file:
                for chunk in tqdm(response.iter_content(chunk_size=8192), desc=f'Downloading: {args.output}.mp4'): 
                    file.write(chunk)
            print(f'Downloaded: {file.name}')
        self.driver.close()


parser = argparse.ArgumentParser(description='Facebook-Downloader — by Richard Mwewa')
parser.add_argument('url', help='facebook video url (eg. https://www.facebook.com/PageName/videos/VideoID')
parser.add_argument('-A', '--audio', help=argparse.SUPPRESS, action='store_true')
parser.add_argument('-o', '--output', help='output filename')
args = parser.parse_args()
logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%I:%M:%S%p', level='NOTSET')

if __name__ == "__main__":
    try:
        FacebookDownloader(args).download_video()

    except KeyboardInterrupt:
        logging.warning('Process interrupted with Ctrl+C.')

    except Exception as e:
        logging.error(e)