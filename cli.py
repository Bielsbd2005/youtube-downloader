import sys
from src.downloader import download_video

# Make sure the user provided a URL
if len(sys.argv) < 2:
    print("Usage: python cli.py <YouTube_URL>")
    sys.exit(1)

# Get the video URL from the command line
url = sys.argv[1]

# Start the download
download_video(url)
