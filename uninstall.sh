#!/bin/bash

# Remove the geckodriver binary from /usr/bin
sudo rm /usr/bin/geckodriver -v

# Uninstall facebook-downloader
pip3 uninstall facebook-downloader -y -v
echo "Cleanup complete."
