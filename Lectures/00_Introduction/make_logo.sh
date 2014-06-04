#First export the keynote as a m4v then run the following:
ffmpeg -i Python_and_NASA_logos.m4v -r 10 -f image2pipe -vcodec ppm - | convert -delay 10 -loop 0 - Python_and_NASA_logos.gif