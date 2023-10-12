# Facebook Downloader
A program for downloading videos from Facebook, given a video url

[![Upload Python Package](https://github.com/rly0nheart/facebook-downloader/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/facebook-downloader/actions/workflows/python-publish.yml)
[![CodeQL](https://github.com/rly0nheart/facebook-downloader/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/facebook-downloader/actions/workflows/codeql.yml)

# Installation
## Install from PyPI
```
pip install facebook-downloader
```
> You will need to have the FireFox browser installed and geckodriver properly set up.

## Building from source
**1.** Clone the repository
```
git clone https://github.com/bellingcat/facebook-downloader
```

**2.** Navigate to the cloned repository
```
cd facebook-downloader
```

### Building the Docker container
```
docker build --tty my-facebook-downloader .
```

### Building the facebook-downloader package
#### Linux
Find the `install.sh` script and run it
```
./install.sh
```
> This assumes the script was already made executable with the `chmod +x uninstall.sh` command.



#### Windows
**1.** Navigate to the facebook-downloader directory
Find the `install.ps1` script and run it
```
.\install.ps1
```
> The installation scripts will download and setup geckodriver, then install **facebook-downloader**.

# Usage
## Package
```
facebook_downloader <video-url>
```

## Docker
```
 docker run --tty --volume $PWD/downloads:/app/downloads my-facebook-downloader <facebook_video_url>
```


# Optional Arguments
| Flag | Description |
|---------|:-----------:|
| *-a/--audio* | download as audio |
| *-o/--output* | output file name |

# Donations
If you would like to donate, you could Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/_rly0nheart"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=_rly0nheart&button_colour=40DCA5&font_colour=ffffff&font_family=Comic&outline_colour=000000&coffee_colour=FFDD00" /></a>

Your support will be much appreciated!
