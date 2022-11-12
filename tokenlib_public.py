#!/usr/bin/python3


def whattokenswehave():
	tokenlist=["pixey.org", "mastodon.lol"]
	return tokenlist

def getmytokenfor(Mastodon_server):
    if Mastodon_server == "pixey.org":
        tokendict={
        "host_instance": 'https://pixey.org',
        "pa_token": "seclet-token-for-your-bot",  ## create tokens yourselfin your mastodon profile
        "botname": "thisisanicebot"}
    if Mastodon_server == "mastodon.lol":
        tokendict={
        "host_instance": 'https://mastodon.lol',
        "pa_token": "velyseclettoken",
        "botname": "othernicebot"}
    if Mastodon_server == "campaign.openworlds.info":
        tokendict={
        "host_instance": 'https://campaign.openworlds.info',
        "pa_token": "vellyvellyseclet",
        "botname": "botterdebotbot"}
    return tokendict

#tokendict=getmytokenfor("pixey.org")
#print("tokendict is ", tokendict)
#pa_token = tokendict["pa_token"]
#host_instance = tokendict["host_instance"]
#botname = tokendict["botname"]
#print("host instance is", host_instance)
