import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Function to browse and select the video file
def browse_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)

    # Function to browse and select the thumbnail image
def browse_thumbnail():
    thumbnail_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    thumbnail_entry.delete(0, tk.END)
    thumbnail_entry.insert(0, thumbnail_path)