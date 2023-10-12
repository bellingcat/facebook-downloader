# Facebook Downloader
A program for downloading videos from Facebook, given a video url

[![Upload Python Package](https://github.com/rly0nheart/facebook-downloader/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/facebook-downloader/actions/workflows/python-publish.yml)
[![CodeQL](https://github.com/rly0nheart/facebook-downloader/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/facebook-downloader/actions/workflows/codeql.yml)

# Installation
## Install from PyPI
```
pip install facebook-downloader
```

### Note
> You will need to have the FireFox browser installed on your pc.

# Docker
## Build the container
```
docker build -t my-facebook-downloader .
```

# Geckodriver setup
> This assumes you've cloned the repository with `git clone https://github.com/bellingcat/facebook-downloader`
## Linux
**1.** Navigate to the facebook-downloader directory
```
cd facebook-downloader
```

**2.** Find the `install.sh` script and run it
```
./install.sh
```
> This assumes the script was already made executable with the `chmod +x uninstall.sh` command.



## Windows
**1.** Navigate to the facebook-downloader directory
```
cd facebook-downloader
```

**2.** Find the `install.ps1` script and run it
```
.\install.ps1
```
> The installation scripts will download and setup geckodriver, then install **facebook-downloader**.

# Usage
```
facebook_downloader <video-url>
```

# Docker
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
