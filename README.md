# Facebook Downloader

A program for downloading videos from facebook, given a video url

# Installation
**Install from PyPI**
```
pip install facebook-downloader
```

### Note
> You will need to have the FireFox browser installed on your pc
>> The program is dependent on selenium, so in order to run it, you will have to download and properly setup geckodriver (setup instructions available below)

# Geckodriver setup
## Linux
**1. Go to the geckodriver [releases page](https://github.com/mozilla/geckodriver/releases/). Find the latest version of the driver for your platform and download it**

**2. Extract the downloaded file**
```
tar -xvzf geckodriver*
```
**3. Add geckodriver to your system path**
```
export PATH=$PATH:/path/to/downloaded/geckodriver
```

### Note
> If you encounter issues with the above commands, then you should run them as root


## Windows
**1. Go to the geckodriver [releases page](https://github.com/mozilla/geckodriver/releases/). Find the geckodriver.exe binary for your platform and download it**

**2. Move the downloaded executable to** *C:\Users\yourusername\AppData\Local\Programs\Python\Python310*

### Note
> The numbers on the directory 'Python310' will depend on the version of Python you have

## Mac OS
* [Set up Selenium & GeckoDriver (Mac)](https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac-b411dbfe61bc)


# Usage
```
facebook_downloader <video-url>
```

## Note
> The url format should be as follows; https://www.facebook.com/PageName/videos/VideoID


# Optional Arguments
| Flag | Description |
|---------|:-----------:|
| *-a/--audio* | download as audio |
| *-o/--output* | output file name |

# Donations
If you would like to donate, you could Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/189381184" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated!
