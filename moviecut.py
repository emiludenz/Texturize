from moviepy.editor import *
import os, shutil
import csv




def read_marks():
    # Returns a dictionary holding title and start/stop time

    with open("clip_marks.txt") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        marks = dict()
        for row in readCSV:

            # format numbers from mm.ss to hh:mm:ss.ms
            title = row[2]
            start = row[0]
            stop = row[1]

            marks.update({str(title): [start, stop]})
    return marks


def cut_out(video_clip, clip_name, start, stop):
    clip = VideoFileClip(video_clip).subclip(start, stop)
    clip.write_videofile(clip_name)

def get_video_clip():
    content = os.listdir()
    for item in content:
        if ".mp4" in item:
            return item

def main():
    # Home dir - change it to something not static
    home = os.getcwd()
    # Clips folder
    folder = home + "\\clips"

    # Make dir if it does not exist
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    video_clip = get_video_clip()

    # Hardcoded checker
    # video_clip = "2017.11.16 - Godnatlæsning med Paludan Afsnit 14.mp4"

    marks = read_marks()
    for key, val in marks.items():
        start, stop = val[0], val[1]
        clip_name = key[2:-1] + ".mp4"
        cut_out(video_clip, clip_name, start, stop)
        shutil.move(home + "\\" + clip_name, folder + "\\" + clip_name)

if __name__ == "__main__":
    main()