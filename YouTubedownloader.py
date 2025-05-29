import PySimpleGUI as sg
import yt_dlp
import os
import threading
import queue
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set theme and font
sg.theme('DarkBlue3')
sg.set_options(font=('Arial', 12))

def download_video(url, output_path, download_type, result_queue):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'progress_hooks': [lambda d: progress_hook(d, result_queue)],
            'ignoreerrors': True,  # Continue on errors for playlists
            'logger': logging.getLogger('yt_dlp'),
        }

        if download_type == '-VIDEO-':
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif download_type == '-AUDIO-':
            ydl_opts['format'] = 'bestaudio[ext=m4a]'
            ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}]
        elif download_type == '-PLAYLIST-':
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            ydl_opts['yes_playlist'] = True

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result_queue.put(('status', f"Starting download for: {url}"))
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown title')
            result_queue.put(('success', f"Download complete: {title}"))

    except Exception as e:
        result_queue.put(('error', f"Error: {str(e)}"))
        logging.error(f"Download failed for {url}: {str(e)}")

def progress_hook(d, result_queue):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        downloaded = d.get('downloaded_bytes', 0)
        if total > 0:
            progress = int((downloaded / total) * 100)
            result_queue.put(('progress', progress))
        else:
            result_queue.put(('progress', 0))  # Fallback for no progress data
        result_queue.put(('status', f"Downloading: {d.get('_default_template', 'Unknown')}"))
    elif d['status'] == 'finished':
        result_queue.put(('progress', 100))
        result_queue.put(('status', f"Finished downloading: {d.get('_default_template', 'Unknown')}"))
    elif d['status'] == 'error':
        result_queue.put(('error', f"Download error: {d.get('error', 'Unknown error')}"))

def create_main_window():
    layout = [
        [sg.Text("YouTube Downloader", font=('Arial', 18, 'bold'))],
        [sg.Text("Download videos or playlists from YouTube", font=('Arial', 12))],
        [sg.HorizontalSeparator()],
        [sg.Frame('Options', [
            [sg.Radio('Single Video', "DOWNLOAD_TYPE", key='-VIDEO-', default=True)],
            [sg.Radio('Playlist', "DOWNLOAD_TYPE", key='-PLAYLIST-')],
            [sg.Radio('Audio Only', "DOWNLOAD_TYPE", key='-AUDIO-')]
        ])],
        [sg.Text("YouTube URL:"), sg.Input(key='-URL-', size=(40,1))],
        [sg.Text("Save to:"), sg.Input(key='-PATH-', default_text=os.path.join(os.path.expanduser('~'), 'Downloads'), size=(40,1)), sg.FolderBrowse()],
        [sg.Button('Download'), sg.Button('About'), sg.Button('Exit')],
        [sg.Text("", size=(50,1), key='-STATUS-')],
        [sg.ProgressBar(100, orientation='h', size=(40, 20), key='-PROGRESS-', visible=False, bar_color=('green', 'white'))]
    ]
    return sg.Window("YouTube Downloader", layout, finalize=True)

def main():
    window = create_main_window()
    result_queue = queue.Queue()

    while True:
        event, values = window.read(timeout=100)  # Check for events and queue updates
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        if event == 'About':
            sg.popup(
                "It's simply tool to download from YouTube its developed by Sami Remili Pythonista",
                title='About YouTube Downloader',
                font=('Arial', 12)
            )

        # Process queue messages
        try:
            while not result_queue.empty():
                message_type, message = result_queue.get_nowait()
                if message_type == 'status':
                    window['-STATUS-'].update(message)
                elif message_type == 'progress':
                    window['-PROGRESS-'].update(visible=True, current_count=message)
                elif message_type == 'success':
                    window['-STATUS-'].update(message)
                    window['-PROGRESS-'].update(visible=False)
                    sg.popup_notify(message, title='Success')
                elif message_type == 'error':
                    window['-STATUS-'].update(message)
                    window['-PROGRESS-'].update(visible=False)
                    sg.popup_error(message, title='Download Failed')
        except queue.Empty:
            pass

        if event == 'Download':
            url = values['-URL-'].strip()
            path = values['-PATH-']
            download_type = '-VIDEO-' if values['-VIDEO-'] else '-PLAYLIST-' if values['-PLAYLIST-'] else '-AUDIO-'

            if not url:
                sg.popup_error("Please enter a YouTube URL")
                continue
            if not path or not os.path.exists(path):
                sg.popup_error("Please select a valid download folder")
                continue

            window['-STATUS-'].update("Starting download...")
            window['-PROGRESS-'].update(visible=True, current_count=0)
            threading.Thread(
                target=download_video,
                args=(url, path, download_type, result_queue),
                daemon=True
            ).start()

    window.close()

if __name__ == "__main__":
    main()
