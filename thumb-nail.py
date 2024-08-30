from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Ensure this is the correct path to your video file
video_path = r"C:\Users\AUSTIN\thumbnail-movie-py\spidervswaspvideo.mp4"
thumbnail_path = r"C:\Users\AUSTIN\thumbnail-movie-py\spidervswasp.jpeg"

# Load the video and thumbnail using the correct paths
video = VideoFileClip(video_path)

thumbnail = (
    ImageClip(thumbnail_path)
    .set_duration(1)
    .resize(width=video.w)  # Resize thumbnail width to match the video
    .set_start(0)           # Start the thumbnail at the beginning of the video
)

# Combine the thumbnail and video
final_clip = CompositeVideoClip([thumbnail, video.set_start(thumbnail.duration)])

# Export the final video with the thumbnail
final_clip.write_videofile("output_video_with_thumbnail.mp4", codec="libx264")
