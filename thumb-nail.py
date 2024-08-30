from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

#import video and image for thumbnail
video = VideoFileClip("C:\Users\YourUsern\Documents\path_to_video.mp4")
thumbnail = ImageClip("")

##Set the thumbnail duration
thumbnail = thumbnail.set_duration(1)

thumbnail = thumbnail.resize(width=video.w) #aspect ratio
thumbnail = thumbnail.set_start(0)

final_clip = CompositeVideoClip([thumbnail, video.set_start(thumbnail.duration)]) #uses CompositeVideoClip()function that merges multiple clips (video and images) into a single video, layering them according to their start times

final_clip.write_videofile("output_video_with_thumbnail.mp4", codec="libx264") #writes the output into a file