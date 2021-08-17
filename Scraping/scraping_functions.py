from bs4 import BeautifulSoup
import requests
import re
import youtube_dl

test_link = 'https://www.youtube.com/watch?v=V037zkkQAOI&list=LL&index=1'

def return_features_1(link):
    """ Returns a list of the following attributes in string form:
        Views, title, date published, category, description, duration (in seconds)"""
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    # Get video title
    titleSoupMeta = soup.find("meta", property="og:title")
    videoTitle = titleSoupMeta["content"] if titleSoupMeta else "NotFound"

    # Video views
    # MAKE SURE TO CHECK in other videos that the interaction count == views

    videoViews = soup.find(attrs={"itemprop": "interactionCount"}).attrs['content']

    # Other features

    videoPublished = soup.find(attrs={"itemprop": "uploadDate"}).attrs['content']
    videoCategory = soup.find(attrs={"itemprop": "genre"}).attrs['content']
    description = soup.find(attrs={"itemprop": "description"}).attrs['content']
    duration = soup.find(attrs={"itemprop": "duration"}).attrs['content']
    minutes = re.findall('[0-9]+', duration)[0]
    seconds = re.findall('[0-9]+', duration)[1]
    duration_secs = str(int(minutes)*60 + int(seconds))
    return {"views": videoViews, "title": videoTitle, 'date_pub': videoPublished, 'category': videoCategory,
            'description': description, 'duration_secs': duration_secs}
