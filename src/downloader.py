import os
from yt_dlp import YoutubeDL

# This function shows the download progress in the console
def show_progress(data):
    if data.get("status") == "downloading":
        downloaded = data.get("downloaded_bytes", 0)
        total = data.get("total_bytes", 0)
        if total > 0:
            percent = downloaded / total * 100
            print(f"\rDownloading: {percent:.1f}%", end="")
    elif data.get("status") == "finished":
        print("\nDownload complete! Merging video and audio...")

# This function downloads a YouTube video in the best quality available
def download_video(url):
    # Create the "downloads" folder if it doesn't exist
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # yt-dlp options
    options = {
        "format": "bv*+ba/best",                   # best video + best audio
        "outtmpl": "downloads/%(title)s.%(ext)s",  # file name and output folder
        "merge_output_format": "mp4",              # final format
        "progress_hooks": [show_progress]          # show download progress
    }

    # Download the video
    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Video saved inside the 'downloads' folder.")
    except Exception as e:
        print("Error downloading video:", e)
