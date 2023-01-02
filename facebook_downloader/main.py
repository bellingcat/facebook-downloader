from facebook_downloader.downloader import FacebookDownloader

def main():
    try:
        start = FacebookDownloader()
        start.download_video()
        
    except KeyboardInterrupt:
        print('[WARNING] Process interrupted with Ctrl+C.')

    except Exception as e:
        print('[ERROR]', e)
