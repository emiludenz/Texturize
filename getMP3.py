from moviepy.editor import *
import os


def main():
    home = os.getcwd()
    home += "\\clips"
    os.chdir(home)
    for item in os.listdir(home):
        sound = AudioFileClip(item)
        name = item[:-3]+"mp3"
        sound.write_audiofile(name)
    return 0

if __name__ == "__main__":
    main()