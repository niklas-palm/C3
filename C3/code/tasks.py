from __future__ import absolute_import, unicode_literals
import os
import json
import re
from .celery import app


@app.task
def wordCount():

    wantedWords = ['han', 'hon', 'hen', 'den', 'denna', 'denne']
    #root = '/data/data/'
    root = '/home/ubuntu/C3/data/'
    my_dict = {}

    for file in getFiles(root):
        with open(root + file) as f:

            for line in f:
                if (len(line) > 0 and not line == '\n'):
                    line = line.strip() #Remove trailing and starting spaces
		    parsedTweet = json.loads(line)
                    if not (parsedTweet["retweeted"]):

                        words = cleanTweet(parsedTweet)

                        for word in words:
                            if word in wantedWords: 
                                my_dict[word] = my_dict.get(word, 0) + 1

    return(my_dict)

def cleanTweet(parsedString):
    words = parsedString["text"]
    words = re.sub('[^a-zA-Z\s]', '', words.lower()).split()
    return words

def getFiles(root):
    print('getfiles')
    for root, dirs, files in os.walk(root):
        for file in files:
            yield file
