# Youtube_Downloader_GUI
YouTube Downloader  A simple GUI application to download 

![Untitled](https://github.com/user-attachments/assets/b40c473e-eccd-4b6b-8d9e-f94112975702)



markdown

Copy
# YouTube Downloader

A simple GUI application to download YouTube videos, playlists, or audio (MP3) using `yt-dlp`. Features a green progress bar and an "About" page. Developed by Sami Remili Pythonista.

## Features
- Download single YouTube videos, playlists, or audio-only (MP3).
- User-friendly GUI with a green progress bar to track download progress.
- Supports MP4 video and MP3 audio formats.
- "About" page: "It's simply tool to download from YouTube its developed by Sami Remili Pythonista."

## Prerequisites
- **Python 3.10 or later**: Ensure Python is installed. Download from [python.org](https://www.python.org/downloads/).
- **pip**: Python package manager (usually included with Python).
- **ffmpeg**: Required for merging video/audio streams and converting to MP3.
- A stable internet connection to download YouTube content.

## Installation
Follow these steps to set up the script on your system.

### 1. Clone the Repository
Clone or download this repository to your local machine:
```bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
2. Install Python Dependencies
Install the required Python libraries (PySimpleGUI and yt-dlp):

bash

Copy
python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
python -m pip install --upgrade yt-dlp
Note: PySimpleGUI is hosted on a private PyPI server. If you encounter issues, uninstall and reinstall:

bash

Copy
python -m pip uninstall PySimpleGUI
python -m pip cache purge
python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
3. Install ffmpeg
ffmpeg is required for video/audio merging and MP3 conversion. Install it based on your operating system:

Windows
Option 1: Manual Installation
Download ffmpeg-release-essentials.zip from gyan.dev.
Extract to a folder (e.g., C:\ffmpeg).
Add C:\ffmpeg\bin to your system PATH:
Right-click "This PC" → "Properties" → "Advanced system settings" → "Environment Variables."
Under "System variables," edit Path and add C:\ffmpeg\bin.
Verify: Open a command prompt and run ffmpeg -version.
Option 2: Chocolatey
Install Chocolatey (run in an admin PowerShell):
bash

Copy
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
Install ffmpeg:
bash

Copy
choco install ffmpeg
Run as admin if you encounter permission errors (e.g., Access to the path 'C:\ProgramData\chocolatey\lib-bad' is denied).
Mac
bash

Copy
brew install ffmpeg
Install Homebrew first if needed: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)".

Linux
bash

Copy
sudo apt-get install ffmpeg  # Debian/Ubuntu
sudo yum install ffmpeg     # CentOS/RHEL
sudo dnf install ffmpeg     # Fedora
Verify: ffmpeg -version

4. Register PySimpleGUI (Free for Non-Commercial Use)
PySimpleGUI displays a 30-day trial message ("Trial Period ends in 31 days. Register now") unless registered. For free, non-commercial use:

Visit PySimpleGUI’s website and register with your email to get a free license key.
Add the license key to the script:
Open YouTubedownloader.py.
Replace YOUR_PYSIMPLEGUI_LICENSE_KEY with your key in:
python

Copy
sg.LicenseKey('YOUR_PYSIMPLEGUI_LICENSE_KEY')
Alternatively, set the environment variable:
bash

Copy
setx PYSIMPLEGUI_LICENSE_KEY "Your_License_Key"  # Windows
export PYSIMPLEGUI_LICENSE_KEY="Your_License_Key"  # Mac/Linux
Usage
Run the script:
bash

Copy
python YouTubedownloader.py
Or, if Python 3 is required:
bash

Copy
python3 YouTubedownloader.py
In the GUI:
Select a download type: Single Video, Playlist, or Audio Only.
Enter a YouTube URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ).
Choose a download folder (defaults to ~/Downloads).
Click "Download" to start. The green progress bar will show progress.
Click "About" to view developer info.
Click "Exit" to close the app.
Check the output folder for downloaded files (MP4 for videos, MP3 for audio).
Example URLs
Single Video: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Playlist: https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC
Audio Only: Any video URL with "Audio Only" selected.
Troubleshooting
PySimpleGUI Trial Message:
Register for a free license key at PySimpleGUI to remove the "Trial Period ends in 31 days" message.
ffmpeg Not Found:
Ensure ffmpeg is installed and in PATH (ffmpeg -version). Reinstall if needed.
Download Errors:
If a video fails (e.g., "The downloaded file is empty"), check:
The URL is valid and accessible in your browser (not geo-restricted or DRM-protected).
Console logs for yt-dlp errors (logged to the terminal).
Test with a different URL to rule out video-specific issues.
Progress Bar Empty:
If the green progress bar doesn’t move, the download likely failed. Check console logs or the GUI error popup.
Permission Errors:
Ensure the output folder is writable.
Run Chocolatey as admin for Windows installations.
Contributing
Contributions are welcome! Please submit a pull request or open an issue on GitHub.

License
This project is licensed under the MIT License. PySimpleGUI requires a free license for non-commercial use. yt-dlp and ffmpeg are open-source under their respective licenses.

About
Developed by Sami Remili Pythonista. This tool is a hobbyist project to simplify downloading YouTube content for personal use.
