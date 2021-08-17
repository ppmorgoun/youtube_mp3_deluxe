from scraping_functions import return_features_1
import pycurl
from pathlib import Path

link = "https://www.youtube.com/watch?v=ugBSdrSDZTU"

cookie = Path('../yt_cookies.txt')

C = pycurl.Curl
C.setopt(pycurl.COOKIEFILE, cookie)
pycurl_link = C.setopt(C.URL, link)
dog_features = return_features_1(pycurl_link)



print(dog_features)