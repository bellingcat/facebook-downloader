# Facebook-Downloader
A program for downloading Facebook videos

# Installation
**1. Clone the project**
```
git clone https://github.com/rly0nheart/Facebook-Downloader.git
```

**2. Move to Facebook-Downloader directory**
```
cd Facebook-Downloader
```

**3. Install dependencies**
## Note
> *This will install tqdm, selenium, and requests*
> > *You will need to have Firefox installed to run the program*
> > > *For user convenience, the program will come with a geckodriver.exe binary*
```
pip install -r requirements.txt
```

# Usage
```
python downloader.py <facebook-url>
```

> *Alternatively, you could grant execution permission to the downloader and run it as shown below*

**1. Grant execution permission**
```
chmod +x downloader.py
```

**2. Run downloader**
```
./downloader.py <facebook-url>
```

## Example
```
python downloader.py https://www.facebook.com/PageName/videos/VideoID
```

## Note
> Upon run, the downloader will first check for updates. If found, users will be prompted to download the updates


# Optional Arguments
| Flag | Description |
|---------|:-----------:|
| *-A/--audio* | download audio only (coming soon) |
| *-o/--output*   | output filename |
| *-v/--version*   | show program's version number and exit |

# Donations
If you would like to donate, you could Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/189381184" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated!
