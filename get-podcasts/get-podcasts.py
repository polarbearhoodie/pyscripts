import os
import re
import requests
from xml.etree.ElementTree import parse


# Takes a folder and removes all contents
def clearFolder(path):
    for file in os.listdir(path):
        os.remove("{}/{}".format(path, file))


# Save a given RSS feed
def loadRSS(url):
    # load the file:

    ###TODO
    # hash the file and check for duplicates


    tmp_name = "no_title.xml"
    response = requests.get(url)
    with open(tmp_name, 'wb') as file:
        file.write(response.content)

    tree = parse(tmp_name)
    root = tree.getroot()
    title = root[0][0].text

    

    os.rename(tmp_name, "XML/{}.xml".format(title))


# Parse the XML file; Download the first mp3
def xml2mp3(xml_name):
    tree = parse("XMl/{}".format(xml_name))
    root = tree.getroot()
    root = root[0]

    # the first item is the title
    title_loc = 0

    # get the location of the first podcast
    podcast_loc = 0
    for i in range (50):
        if root[i].tag == 'item':
            podcast_loc = i
            break

    # get the location of the first enclosure, which contains the URL
    enclosure_loc = 0
    for i in range(50):
        if root[podcast_loc][i].tag == "enclosure":
            enclosure_loc = i
            break

    # parse the title and URL
    title = root[podcast_loc][title_loc].text
    title = re.sub("[^a-zA-Z0-9 ,]", '', title) # no special characters in title
    media = root[podcast_loc][enclosure_loc].attrib['url']


    # prepare the formatted title and path
    mp3_name = "{}.mp3".format(title)
    mp3_path = "MP3/{}".format(mp3_name)
    # full_path = "{}/{}".format(mp3_path, mp3_name)

    response = requests.get(media)
    with open(mp3_path, 'wb') as file:
        file.write(response.content)


def getFeeds():
    clearFolder("XML")
    for line in open("podcast-feeds.txt", "r"):
        loadRSS(str(line).strip())


def getAudio():
    clearFolder("MP3")
    for file in os.listdir("XML"):
        xml2mp3(file)


# ensure that mp3's and xml's are not redownloaded
# only download if the xml hash does not match an existing eml in a db (SQL)
# store a hash of xml


# determine f an xml is identical:
# same name:
# same hash -> do not download


# -> determine


getFeeds()
getAudio()
