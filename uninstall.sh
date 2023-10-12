#!/bin/bash

# Remove the geckodriver binary from /usr/bin
sudo rm /usr/bin/geckodriver -v

# Uninstall tor2tor
pip3 uninstall facebook-downloader -y -v
echo "Cleanup complete."