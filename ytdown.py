import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import ssl
from pytube import YouTube

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Rest of the code...

def download_video():
    video_url = url_entry.get()
    quality = quality_var.get()

    try:
        yt = YouTube(video_url)

        if quality == 'High':
            video = yt.streams.get_highest_resolution()
        elif quality == 'Low':
            video = yt.streams.get_lowest_resolution()

        video.download()
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create a label and entry for the video URL
url_label = tk.Label(window, text="Video URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create radio buttons for quality selection
quality_label = tk.Label(window, text="Video Quality:")
quality_label.pack()

quality_var = tk.StringVar()
high_quality_radio = tk.Radiobutton(window, text="High", variable=quality_var, value="High")
high_quality_radio.pack()

low_quality_radio = tk.Radiobutton(window, text="Low", variable=quality_var, value="Low")
low_quality_radio.pack()

# Create a button to start the download
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# Start the GUI main loop
window.mainloop()
