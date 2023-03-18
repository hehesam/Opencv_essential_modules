import cv2
from PIL import Image, ImageSequence
import io
import numpy as np


def resize_frame(frame, scale_percent):
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)



def resize_gif(input_file, output_file, scale_percent):
    # Read the GIF file
    input_gif = Image.open(input_file)
    
    # Process the frames
    output_frames = []
    for frame in ImageSequence.Iterator(input_gif):
        # Convert the PIL image to an OpenCV image (BGR format)
        frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        # Resize the frame
        resized_frame_cv = resize_frame(frame_cv, scale_percent)

        # Convert the resized frame back to a PIL image (RGB format)
        resized_frame = Image.fromarray(cv2.cvtColor(resized_frame_cv, cv2.COLOR_BGR2RGB))

        # Save the resized frame to the output buffer
        output_frames.append(resized_frame)

    # Save the resized frames as a new GIF file
    output_frames[0].save(
        output_file,
        save_all=True,
        append_images=output_frames[1:],
        duration=input_gif.info["duration"],
        loop=input_gif.info["loop"],
    )


def resize_and_compress_gif(input_file, output_file, scale_percent, quality=80):
    # Read the GIF file
    input_gif = Image.open(input_file)

    # Process the frames
    output_frames = []
    for frame in ImageSequence.Iterator(input_gif):
        # Convert the PIL image to an OpenCV image (BGR format)
        frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        # Resize the frame
        resized_frame_cv = resize_frame(frame_cv, scale_percent)

        # Convert the resized frame back to a PIL image (RGB format)
        resized_frame = Image.fromarray(cv2.cvtColor(resized_frame_cv, cv2.COLOR_BGR2RGB))

        # Save the resized frame to the output buffer
        output_frames.append(resized_frame)

    # Save the resized frames as a new GIF file
    output_frames[0].save(
        output_file,
        format="GIF",
        save_all=True,
        append_images=output_frames[1:],
        duration=input_gif.info["duration"],
        loop=input_gif.info["loop"],
        optimize=True,
        quality=quality,
    )



input_file = "input.gif"
output_file = "output.gif"
scale_percent = 30  # Scale the image to 50% of its original size
quality = 50
# resize_gif(input_file, output_file, scale_percent)
resize_and_compress_gif(input_file, output_file, scale_percent, quality)

