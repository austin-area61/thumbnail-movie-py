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

# Function to add the thumbnail to the video
def add_thumbnail():
    video_path = video_entry.get()
    thumbnail_path = thumbnail_entry.get()

    # Ensure the paths are valid
    if not video_path or not thumbnail_path:
        print("Please select both video and thumbnail files.")
        return

    # Load video and thumbnail
    video = VideoFileClip(video_path)
    thumbnail = ImageClip(thumbnail_path).set_duration(video.duration).resize(height=video.h).set_position(("center", "center"))
    
    # Composite the video with the thumbnail
    final_video = CompositeVideoClip([video, thumbnail])

    # Save the final video
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])
    final_video.write_videofile(output_path, codec="libx264", fps=24)

    print(f"Thumbnail added to video and saved as {output_path}")

# Create the main window
root = tk.Tk()
root.title("Thumbnail Adder")

# Video file selection
video_label = tk.Label(root, text="Select Video File:")
video_label.pack(pady=5)
video_entry = tk.Entry(root, width=50)
video_entry.pack(pady=5)
video_browse_button = tk.Button(root, text="Browse", command=browse_video)
video_browse_button.pack(pady=5)

# Thumbnail file selection
thumbnail_label = tk.Label(root, text="Select Thumbnail Image:")
thumbnail_label.pack(pady=5)
thumbnail_entry = tk.Entry(root, width=50)
thumbnail_entry.pack(pady=5)
thumbnail_browse_button = tk.Button(root, text="Browse", command=browse_thumbnail)
thumbnail_browse_button.pack(pady=5)

# Button to add the thumbnail
add_thumbnail_button = tk.Button(root, text="Add Thumbnail to Video", command=add_thumbnail)
add_thumbnail_button.pack(pady=20)

# Run the application
root.mainloop()
