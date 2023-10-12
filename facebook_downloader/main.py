from facebook_downloader.downloader import FacebookDownloader


def start_downloader():
    try:
        # Initialise the FaceBookDownloader instance.
        program = FacebookDownloader()

        # Create directory where downloaded videos will be stored.
        program.path_finder()

        # Print program's license notice.
        print(program.notice())

        # Check for latest releases.
        program.check_updates()

        # Start video download.
        program.download_video()

    except KeyboardInterrupt:
        print("Process interrupted with Ctrl+C.")

    except Exception as e:
        print(f"An error occurred: {e}")
