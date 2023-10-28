import os
import time

# get the time and calculate utc epoch of last midnight
t = time.localtime()
utc_int = int(time.mktime(t))
last_midnight = utc_int - (utc_int % 86400) + 25200

# clear out old files in the video dir
tmp_dir_list = os.listdir("video")
for f1 in tmp_dir_list:
    os.remove("video/{}".format(f1))

# move photos from yesterday into video folder
dir_list = os.listdir("photos")
for f2 in dir_list:
    timestamp = int(f2.split('.')[0])
    if timestamp < last_midnight:
        os.rename("photos/{}".format(f2), "video/{}".format(f2))

# process the video with ffmpeg
name = str(last_midnight)
command = """ffmpeg -framerate 24 -pattern_type glob -i "video/*.jpg" -c:v libx264 -crf 15 -pix_fmt yuv420p {}.mp4"""

if len(os.listdir("video")) > 0:
    os.system(command.format(name))
    print("finished")
else:
    print("no items to process")
