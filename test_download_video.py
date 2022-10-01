from downloader import download_video
     
def test_download_video():
    # I find this video very interesting, enjoy! ;)
    url = 'https://www.facebook.com/VICE/videos/663211078474482'
    download_video(url, output='test_video_making-a-weed-smoothie')
