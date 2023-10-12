import os
import requests
import argparse
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from . import __version__, __author__


class FacebookDownloader:
    def __init__(self):
        self.__base_url = "https://getfvid.com"
        self.__update_check_endpoint = "https://api.github.com/repos/rly0nheart/facebook-downloader/releases/latest"
        self.__home_directory = os.path.expanduser("~")
        self.__downloads_directory = os.path.join(self.__home_directory, "facebook-downloader")

        __option = webdriver.FirefoxOptions()
        __option.add_argument('--headless')
        self.__driver = webdriver.Firefox(options=__option)

        parser = argparse.ArgumentParser(description=f'facebook-downloader — by {__author__}',
                                         epilog='Facebook video downloader.')
        parser.add_argument('url', help='facebook video url')
        parser.add_argument('-a', '--audio', help='download file as audio', action='store_true')
        parser.add_argument('-o', '--output', help='output filename', default="")
        parser.add_argument('-v', '--version', action='version', version=__version__)
        self.__args = parser.parse_args()

    @staticmethod
    def __format_output_filename(user_defined_name) -> str:
        """
        Formats the output file's name.

        :param user_defined_name: User-defined name for the file.
        :return: Formatted/Reconstructed name of the file.
        """
        from datetime import datetime

        dt_now = datetime.now()
        if os.name == "nt":
            output_name = dt_now.strftime(f"{user_defined_name}_%d-%m-%Y %I-%M-%S%p-facebook-downloader.mp4")
        else:
            output_name = dt_now.strftime(f"{user_defined_name}_%d-%m-%Y %I:%M:%S%p-facebook-downloader.mp4")

        return output_name

    def notice(self) -> str:
        """
        Returns the program's license notice and current version.

        :return: License notice.
        :rtype: str
        """
        return f"""
        facebook-downloader v{__version__} Copyright (C) 2022-2023  Richard Mwewa
        
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
        """

    def check_updates(self):
        """
        Checks if the program's version tag matches the tag of the latest release on GitHub.
        If the tags match, assume the program is up-to-date.
        """
        with requests.get(self.__update_check_endpoint) as response:
            remote_version = response.json().get('tag_name')
            if remote_version != __version__:
                print(f"* A new release is available -> facebook-downloader v{remote_version}.\n"
                      f"* Run 'pip install --upgrade facebook-downloader' to get the updates.\n")

    def __get_download_type_element(self) -> str:
        """
        Gets the web element according to the specified command-line arguments.
        

        ELements
        --------
        - HD: /html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a
        - SD: /html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[2]/a
        - Audio: /html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[3]/a

        :return: Web element
        """
        if self.__args.audio:
            download_type_element = "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[3]/a"
        else:
            download_type_element = "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a"

        return download_type_element

    def path_finder(self) -> None:
        """
        Creates the facebook-videos directory.

        :return: None
        """
        # Construct and create the directory if it doesn't already exist
        os.makedirs(os.path.join(self.__home_directory, "facebook-downloader"), exist_ok=True)

    def download_video(self):
        """
        Opens https://getfvid.com with selenium and uses the specified facebook video link as a query.
        """
        # Open the base url.
        self.__driver.get(self.__base_url)

        # Locate the facebook video url entry field.
        url_entry_field = self.__driver.find_element(By.NAME, "url")

        # Write the given facebook video url in the entry field.
        url_entry_field.send_keys(self.__args.url)

        # Press ENTER.
        url_entry_field.send_keys(Keys.ENTER)
        print("* Loading web resources... Please wait.")

        # Find the download button (this clicks the first button which returns a video in hd).
        download_btn = WebDriverWait(self.__driver, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH,
                                                             self.__get_download_type_element())))
        # Get the video download url from the download button.
        download_url = download_btn.get_attribute('href')

        # Open the download url and stream the content to a file.
        with requests.get(download_url, stream=True) as response:
            response.raise_for_status()
            with open(os.path.join(self.__downloads_directory,
                                   self.__format_output_filename(self.__args.output)), 'wb') as file:
                for chunk in tqdm(response.iter_content(chunk_size=8192),
                                  desc=f"* Downloading: {file.name}"):
                    file.write(chunk)
                print(f"* Downloaded: {file.name}")

        # Close driver.
        self.__driver.close()
