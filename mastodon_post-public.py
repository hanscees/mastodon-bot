#!/usr/bin/python3
import requests, datetime, time
import os, re
from mastodon import Mastodon
import hcmastodonlib
import tokenlib 

## as you can probably guess:
# tokens are storen in tokenlib_public
# functions to post to mastodon are in hcmastodonlib
##

## this script posts a toot with an image 

#setting up the text from several subtexts
# because its probably you want to keep many subtext constant while tooting with a bot

# the text you toot
Hellotxt = "Hello, this is a test toot. "
myname = "My name is secret"
moretext = "and I am testing some python code"
tweettxt = "%s (%s), %s " % (Hellotxt, myname, moretext)
print ("tweettext is \n", tweettxt)

# some hashtags that stay constant
hashtag1 = "#" + botname
hashtagcontent = "#trees #botany #nature"

#hashtags and tweettext together
post_text = str(tweettext) + "\n" + "posted by " + hashtag1 + " " + hashtagcontent + "\n" # creating post text
post_text = post_text[0:499]



# photo to post 
## remember everu photo needs a description for those who cant see
## test phto you are welcome to use
img_url="https://www.bomengids.nl/2022/species/Hongaarse_eik__Quercus_frainetto__Hungarian_oak__Ungarische_Eiche__Chene_de_Hongrie--Frainetto/blad-leaf-blatt-feuille-hoja/Hongaarse_eik__Quercus_frainetto__Hungarian_oak__Ungarische_Eiche__Chene_de_Hongrie--Frainetto2L.jpg"
foto_description="Photo of treespecies " 
print("foto_description is ", foto_description)


## now lets get the tokens for our bot
## we choose pixey for now
tokenlist=tokenlib_public.whattokenswehave()
print("tokenlist is, ", tokenlist)
tokendict=tokenlib_public.getmytokenfor("pixey.org")
#print("tokendict is ", tokendict)
pa_token = tokendict_public["pa_token"]
host_instance = tokendict_public["host_instance"]
botname = tokendict_public["botname"]
print("host instance to toot with is", host_instance)

# we need this to use pythons Mastodon.py package
mastodon = Mastodon(
    access_token = pa_token,
    api_base_url = host_instance
    # api_base_url = 'https://pixelfed.tokyo/'
)


#first lets download a pic right? 
image = "image.jpg"
# now download photo
local_photo = hcmastodonlib.download_photo2022(urlfoto, image)  #photo contains filepath or false!

#if download went well, let post our toot with foto

if local_photo:
    print("foto downloaded fine and is here:", local_photo)
    hcmastodonlib.tootwithphoto(local_photo, foto_description, post_text, mastodon)
else:
    print("download didnt work sorry, no toot posted")





