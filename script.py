import json
import urllib
import re, urlparse
import os.path


from pprint import pprint


def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

def sanitize(name):
    return "".join([c for c in name if c.isalpha() or c.isdigit() or c==' ']).rstrip()


json_data=open('s.txt')

counter = 1
for jsonobject in json.load(json_data):
    testfile = urllib.URLopener()
    name = str(counter) + '. ' + sanitize(jsonobject['autor']) + " - " + sanitize(jsonobject['title']) + '.mp3'
    name = './vk/' + name

    if not os.path.isfile(name):
        try:
            testfile.retrieve(iriToUri(jsonobject['href']), name)
        except:
            print 'Oops! Error!'
        print name

    counter += 1

json_data.close()