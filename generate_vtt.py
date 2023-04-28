import os
import argparse
from PIL import Image


def generate_vtt_file(input_folder, output_file):
    with open(output_file, "w") as f:
        f.write("WEBVTT\n\n")
        width, height = 178, 100
        for i, filename in enumerate(sorted(os.listdir(input_folder))):
            if i == 0:
                with Image.open(os.path.join(input_folder, filename)) as img:
                    width, height = img.size
            start_time = i
            end_time = i + 1
            start_time_str = f"{start_time//3600:02d}:{(start_time//60)%60:02d}:{start_time%60:06.3f}"
            end_time_str = (
                f"{end_time//3600:02d}:{(end_time//60)%60:02d}:{end_time%60:06.3f}"
            )
            f.write(f"{i+1}\n")
            f.write(f"{start_time_str} --> {end_time_str}\n")
            f.write(f"{filename}#xywh=0,0,{width},{height}\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", type=str, help="Path to input folder of images")
    parser.add_argument("output_file", type=str, help="Path to output VTT file")
    args = parser.parse_args()

    generate_vtt_file(args.input_folder, args.output_file)
