import pandas as pd
import yt_dlp

df = pd.DataFrame(columns=['Title', 'URL', 'Index', 'Duration'])

ydl_opts = {'skip_download':True,
            'format': 'bestaudio/best',
            'outtmpl': '\\Users\\petr\\documents\\funt_stuff\\youtube_app\\%(playlist)s\\data\\%(playlist_index)s_%(title)s',
            'ignoreerrors': True
            }
ydl = yt_dlp.YoutubeDL(ydl_opts)
video = ""
yt_url = "https://www.youtube.com/playlist?list=PLjsZNSbnATzryq95Get-q3WKNfLvn4bjC"

with ydl:
    result = ydl.extract_info(yt_url, download=False)

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries']

        #loops entries to grab each video_url
        for i, item in enumerate(video):
            print(i, item)
            if item == None:
                continue
            else:
                new_row = {'Title': result['entries'][i]['title'], 'URL': result['entries'][i]['webpage_url'],
                           'Index': result['entries'][i]['playlist_index'], 'Duration': result['entries'][i]['duration']}
                df = df.append(new_row, ignore_index=True)





df.to_csv('../most_recent_playlist_info.csv')

"""
An Example: 

import json

import yt_dlp
from yt_dlp.postprocessor.common import PostProcessor


class MyLogger:
    def debug(self, msg):
        # For compatability with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class MyCustomPP(PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.add_post_processor(MyCustomPP())
    info = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc')
    print(json.dumps(ydl.sanitize_info(info)))"""