import requests
from time import sleep
from unidecode import unidecode
from bs4 import BeautifulSoup
import webbrowser
import os
from sys import argv, exit

def print_help():
    print "Usage: python {} url_to_fetch".format(__file__)

if len(argv) != 2:
    print_help()
    exit(0)

if argv[1] == '--help' or argv[1] == '-h':
    print_help()
    exit(0)

url = argv[1]

def get_html(url):
    r = None
    try:
        r = requests.get(url)
    except:
        return get_html(url)
    if r.status_code != 200:
        sleep(2)
        return get_html(url)
    else:
        return r.text

html = get_html(url)

bs = BeautifulSoup(html)

fp = open('{}.html'.format(url[url.rfind('/') + 1 : ]), "w+")

all_a = bs.find_all('a')

elements = []

for a in all_a:
    link = a.get('data-href')
    name = a.text
    se = a.get('href')
    if link != None and (se != '#' or se != None):
        elements.append((se, unidecode(name), "http://ororo.tv" + link))

print "All links OK"

fp.write('<code>')

for element in elements:
    
    s = element[0].replace('#', ' ')
    s = s.replace('-', ' ')
    s = s.replace('-', ' ')
    s = s.strip()
    s = s.split(' ')
    
    print "Currently parsing " + element[1] + " (S" + s[0] + "E" + s[1] + ")"

    
    fp.write("Season " + str(s[0]) + " Episode " + str(s[1]) + ": " + element[1] + " ")
    
    bs = BeautifulSoup(get_html(element[2]))
    
    cur = bs.find_all('source')
    

    for x in cur:
        if x.get('type')[-4:] == 'webm':
            fp.write(" <a href='{}?video=true'>WebM</a>".format(x.get('src')))
        elif x.get('type')[-3:] == 'mp4':
            fp.write(" <a href='{}?video=true'>MP4</a>".format(x.get('src')))
    
    cur = bs.find_all('track')
    
    for x in cur:
        if x.get('label') == 'en':
            fp.write(" <a href='{}'>Subtitle</a>".format("http://ororo.tv" + x.get('src')))
    
    fp.write("<br /><br />")

fp.write('</code>')
fp.close()

webbrowser.open("file://" + os.path.realpath("{}.html".format(url[url.rfind('/') + 1 : ])))