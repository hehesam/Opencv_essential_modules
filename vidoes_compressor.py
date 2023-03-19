from moviepy.editor import VideoFileClip

def resize_video_with_audio(input_file, output_file, scale_percent):
    # Load the input video
    input_video = VideoFileClip(input_file)

    # Calculate the new dimensions
    new_width = int(input_video.size[0] * scale_percent / 100)
    new_height = int(input_video.size[1] * scale_percent / 100)

    # Resize the video
    resized_video = input_video.resize((new_width, new_height))

    # Save the resized video
    resized_video.write_videofile(output_file, codec='libx264')

input_file = "rayan.mp4"
output_file = "me2.mp4"
scale_percent = 50  # Scale the video to 50% of its original size

resize_video_with_audio(input_file, output_file, scale_percent)
