from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(input_file, output_file, fps=None):
    # Load the input video
    input_video = VideoFileClip(input_file)

    # Set the desired frame rate if specified
    if fps is not None:
        input_video = input_video.set_fps(fps)

    # Save the video as a GIF
    input_video.write_gif(output_file, fps=fps, program='ffmpeg')

input_file = "me.mp4"
output_file = "meme.gif"
fps = 25  # Set the frame rate of the GIF (optional)

convert_mp4_to_gif(input_file, output_file, fps)
