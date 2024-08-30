from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

#import video and image for thumbnail
video = VideoFileClip("")
thumbnail = ImageClip("")

##Set the thumbnail duration
thumbnail = thumbnail.set_duration(1)

thumbnail = thumbnail.resize(width=video.w)