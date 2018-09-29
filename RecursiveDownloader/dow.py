import requests
import shutil
import sys
import re
import pefile
import hashlib
import magic
import datetime

DPATH="/opt/uploads/%s"
SPATH="/opt/samples/"
import string 


def isHTML(text):
    blacklist = ["<html","<doctype","<link"]
    for word in blacklist:
        if word in text.lower():
            return True
    return False

def zipit(folder):
	import subprocess
	cmd = ['7z', '-pinfected', 'a', '%ssamples-%s.zip'%(SPATH,datetime.datetime.now()), '/opt/uploads/*', '-mx9']
	sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

def istext(filename):
	m = magic.from_file(filename, mime=True)
	if "text" in m:
		return True
	else:
		return False


def pChecksum(filename, block_size=65536):
	sha256 = hashlib.sha256()
	with open(filename, 'rb') as f:
        	for block in iter(lambda: f.read(block_size), b''):
            		sha256.update(block)
	return sha256.hexdigest()

def getURL(text):
    URLlist = set()
    urls = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    for item in urls.findall(text):
        URLlist.add(item)
    return URLlist

def ana(thisfile):
    if istext(thisfile):
        f = open(thisfile, 'r')
        data = f.read()
        if isHTML(data):
            print("Looks like HTML, maybe WGET does the trick!")
        else:
            urls = getURL(data)
            #print(urls)
            if len(urls) > 0:
                for item in urls:
                    downIt(item)
            else:
                print("Well thats it...")
    else:
        print("%s : %s" % (thisfile, pChecksum(thisfile)))	
		
    

def downIt(url):
    #try:
        r = requests.get(url, stream=True, timeout=1)
        if r.status_code == 200:
            FPATH =  DPATH % (url.split("/")[-1])
            with open(FPATH , 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)   
                ana(FPATH)
        else:
            print("Thats not working, %s" % (r.status_code))
    #except:
    #    print("No download possible via %s" % (url))
    #    exit(0)

    

downIt(sys.argv[1])
zipit(DPATH)
