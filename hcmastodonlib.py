#!/usr/bin/env python
import time
import json
import os
import errno
import urllib
import traceback
import importlib
import requests, datetime
from urllib.error import URLError

## bunch of functions to use mastodon



#post to mastodon with multiple images
# CheckifImageExistsOnline(img_url): # checks if an online url exists
#
#tootwithmanyphoto(photo_dict, post_text, mastodon):  # post toot with multiple images
#
    ## uses these other functions 
#    upload_image_url_to_mastodon(url, foto_description, mastodon):  #downloads image-url to local, uploads to masto. Uses functions below:
#        download_photo2022(img_url, filename):  # downloads image-url to local disk, checks content-header image/jpeg
#        make_sure_path_exists(path):  # see if a specificlocal directory exists. If not makes it
#
# post to mastodon with 1 image uses: 
#    upload_image_to_mastodon(local_photo, foto_description, mastodon): #upload a single local photo
#    tootwithphoto(local_photo, foto_description, post_text, mastodon):



#this function makes a local directory if it does not exist already
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

## this function checks if an url exist (and can be reached)
def CheckifImageExistsOnline(img_url):
      try:
        image_on_web = urllib.request.urlopen(img_url)
        return True
      except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            #os._exit(0) 
            return False
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            return False



#see for using urllib https://realpython.com/urllib-request/
#this function downloads a photo from a url and stores it locally
def download_photo2022(img_url, filename):
    DOWNLOADED_IMAGE_PATH = "/tmpimages/"
    tmpdir = os.getcwd() + DOWNLOADED_IMAGE_PATH
    path = os.getcwd() + DOWNLOADED_IMAGE_PATH
    make_sure_path_exists(tmpdir) # or make it
    file_path = "%s%s" % (path, filename)
    print("file_path is", file_path) #debug
    try:
        image_on_web = urllib.request.urlopen(img_url)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            print("no image found, sleeping") #debug
            time.sleep(9)
            #os.system("./soorttweetrandom.py")
            os._exit(0) 
            return False
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        #print(image_on_web.headers)  #prints all headers
        print(image_on_web.getheader("Content-Type"))  #prints contenttype
        if (image_on_web.getheader("Content-Type")) == "image/jpeg":
            body = image_on_web.read()
            #with open(img_url, mode="wb") as html_file:
            #    html_file.write(body)
           #getcwd is working dir of script
       #first delete old fotofile
            downloaded_image = open(file_path, "wb")
            print("downloaded image is", downloaded_image) #debug
            downloaded_image.write(body)
            downloaded_image.close()
            image_on_web.close()
        else:
           print("no image found, sleeping") #debug
           time.sleep(9)
           #os.system("./soorttweetrandom.py")
           os._exit(0) 
           return False
    #except: traceback.print_exc()
    return file_path

#this function uploads one local foto to mastodon
#https://github.com/Horhik/Instagram2Fedi/blob/main/src/network.py
def upload_image_to_mastodon(local_photo, foto_description, mastodon):
    try:
        print(" Uploading Image...")
        print(datetime.datetime.now())
        media = mastodon.media_post(media_file = local_photo, mime_type = "image/jpeg", description = foto_description) # sending image to mastodon
        print("Uploaded!")
        print(datetime.datetime.now())
        return media["id"]
    except Exception as e:
        print("failed to upload image to mastodon. \n", e)
        print(datetime.datetime.now())

#this function downloads a photo form url to local and posts it to mastodon
#https://github.com/Horhik/Instagram2Fedi/blob/main/src/network.py
def upload_image_url_to_mastodon(url, foto_description, mastodon):
    try:
        file_path = download_photo2022(url, "image.jpg")
        if file_path:
            print("download of image succeeded, continue")
            #print("however, aborting test")
            #exit()
        else:
            print("download didnt work out, aborting on url", url)
            exit()
        print(" Uploading Image...")
        print(datetime.datetime.now())
        media = mastodon.media_post(media_file = file_path, mime_type = "image/jpeg", description = foto_description) # sending image to mastodon
        print("Uploaded!")
        print(datetime.datetime.now())
        return media["id"]
    except Exception as e:
        print("failed to upload image to mastodon. \n", e)
        print(datetime.datetime.now())


# this foto posts a toot with a local photo
#foto should be a local file
def tootwithphoto(local_photo, foto_description, post_text, mastodon):
    try:
        print("Creating Toot...", foto_description)
        print(datetime.datetime.now())
        id =upload_image_to_mastodon(local_photo, foto_description, mastodon)
        
        print("id photo is", id)
        mastodon.status_post(post_text, media_ids = id)
        print("tooth posted fine with foto", post_text)
    except Exception as e:
        print("Failed to create toot \n", e)
        print(datetime.datetime.now())

# this foto posts a toot with more photo's it downloads
# photos are in a dict with {" description" : "url"} entries
#foto should be a local file
def tootwithmanyphoto(photo_dict, post_text, mastodon):
    try:
        print("Creating Toots now...")
        print(datetime.datetime.now())
        ids = []
        #for x, y in thisdict.items():
        #  print(x, y)
        for x, y in photo_dict.items():
          url = y
          foto_description = x
          ids.append(upload_image_url_to_mastodon(url, foto_description, mastodon))
        #id =upload_image_to_mastodon(local_photo, foto_description, mastodon)
        
        print("ids photos are", ids)
        mastodon.status_post(post_text, media_ids = ids)
        print("tooth posted fine with foto", post_text)
    except Exception as e:
        print("Failed to create toot \n", e)
        print(datetime.datetime.now())


