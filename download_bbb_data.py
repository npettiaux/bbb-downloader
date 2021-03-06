#!/usr/bin/env python3
# coding: utf-8

import sys
import os
import bbb
import requests

if __name__ == '__main__' :
    url=sys.argv[1]

    extractor = bbb.BigBlueButtonExtractor()
    extractor._real_extract(url)

    website=getattr(extractor, "website")
    meeting_id=getattr(extractor, "id")

    # download slides in Slides
    print("Downloading Slides")
    i=1
    os.makedirs("Slides", exist_ok=True)
    for slide in extractor.slides:
        print("["+str(i)+"/"+str(len(extractor.slides))+"]  "+slide)
        i=i+1

        slide_url=website + "/presentation/"+meeting_id+"/"+slide
        slide_name="Slides/"+slide.split('/')[-1]

        r = requests.get(slide_url)
        open(slide_name , 'wb').write(r.content)

    # download thummbnails in Thumbnails
    print("Downloading Thumbnails")
    i=1
    os.makedirs("Thumbnails", exist_ok=True)
    for thumbnail in extractor.thumbnails:
        print("["+str(i)+"/"+str(len(extractor.thumbnails))+"]  "+thumbnail['url'])
        i=i+1

        thumbnail_name="Thumbnails/"+thumbnail['url'].split('/')[-1]
        r = requests.get(thumbnail['url'])
        open(thumbnail_name , 'wb').write(r.content)

    # download videos in Videos
    print("Downloading Videos")
    i=1
    os.makedirs("Videos", exist_ok=True)
    for formats in extractor.formats:
        print("["+str(i)+"/"+str(len(extractor.formats))+"]  "+formats['format_id']+ " ("+formats['url']+")")
        i=i+1

        video_name="Videos/"+formats['url'].split('/')[-1]
        r = requests.get(formats['url'])
        open(video_name , 'wb').write(r.content)
