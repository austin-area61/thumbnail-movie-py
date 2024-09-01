import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Function to select video file
def select_video():
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("MP4 Files", "*.mp4"), ("All Files", "*.*")]
    )
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)