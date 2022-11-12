# mastodon-bot
python examples to make a mastodon bot with autoposting

for my website / tree project https://www.bomengids.nl I like to auto-post content to social media.
While all the python libraries are there typically making code to use it takes some time.

I worked a few weeks (evenings) on some code I now use in proicution to post to https://campaign.openworlds.info/@bomengidsnl


Basically these are the scripts / libraries

I post with the scripts:
`
./mastodon_post.campaign.py  #posts one mastodon toot with one image
./mastodon_post4picspecies.py  # posts one mastodon tooth with 4 images
`

these two scripts use these libs:
import hcmastodonlib  # has functions to post to mastodon
import tokenlib   #   has all tokens and so on


hcmastodonlib #has these functions:
# post to mastodon with 1 image uses: 
    def upload_image_to_mastodon(local_photo, foto_description, mastodon): #upload a single local photo
    def tootwithphoto(local_photo, foto_description, post_text, mastodon):

#post to mastodon with multiple images
CheckifImageExistsOnline(img_url): # checks if an online url exists # optionally use:

tootwithmanyphoto(photo_dict, post_text, mastodon):  # post toot with multiple images
    ## uses these other functions 
    def upload_image_url_to_mastodon(url, foto_description, mastodon):  #downloads image-url to local, uploads to masto. Uses functions below:
        download_photo2022(img_url, filename):  # downloads image-url to local disk, checks content-header image/jpeg
        make_sure_path_exists(path):  # see if a specificlocal directory exists. If not makes it
      
I am sure there are better coders out there, but this is functional code to work with. 


