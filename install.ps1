# Define URL for GeckoDriver
$geckoURL = "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip"

# Define target directories for installation
$geckoDir = "$env:USERPROFILE\facebook-downloader\GeckoDriver"

# Function to download a file
function DownloadFile([string]$url, [string]$path) {
    Invoke-WebRequest -Uri $url -OutFile $path
}

# Check if GeckoDriver directory exists, if not create and download
if (-Not (Test-Path $geckoDir)) {
    New-Item -Path $geckoDir -ItemType Directory
    Write-Host "Downloading GeckoDriver..."
    DownloadFile $geckoURL "$geckoDir\geckodriver.zip"

    # Unzipping the GeckoDriver
    Expand-Archive -Path "$geckoDir\geckodriver.zip" -DestinationPath $geckoDir
    Remove-Item "$geckoDir\geckodriver.zip"
}

# Add the geckodriver directory to PATH
[Environment]::SetEnvironmentVariable("PATH", [Environment]::GetEnvironmentVariable("PATH", [EnvironmentVariableTarget]::User) + ";$geckoDir", [EnvironmentVariableTarget]::User)

pip install .
Write-Host "Setup complete."
