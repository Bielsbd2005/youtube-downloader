# YouTube Downloader

Download YouTube videos in the highest available quality using `yt-dlp` and `ffmpeg`.


---

## ⚙️ Requirements
- Python 3.11+
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- [`ffmpeg`](https://ffmpeg.org/) available in your system PATH

---

## 📦 Installation
```bash
git clone https://github.com/Bielsbd2005/youtube-downloader.git
cd youtube-downloader
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Mac:
source .venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Usage
```bash
python cli.py "https://youtube.com/watch?v=xxxx"
```

Videos will be saved inside `downloads/` folder.

---

## 📄 License
This project is licensed under the MIT License.
