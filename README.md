mastodon-bot <br/>
python examples to make a mastodon bot with autoposting
<br/><br/>
for my website / tree project https://www.bomengids.nl I like to auto-post content to social media.
While all the python libraries are there typically making code to use it takes some time.
<br/>
I worked a few weeks (evenings) on some code I now use in proicution to post to https://campaign.openworlds.info/@bomengidsnl
<br/><br/>

Basically these are the scripts / libraries
<br/><br/>
I post with the scripts:
<ul>
<li>./mastodon_post.campaign.py  #posts one mastodon toot with one image</li>
<li>./mastodon_post4picspecies.py  # posts one mastodon tooth with 4 images</li>
</ul>
<br/>

these two scripts use these libs:
<ul>
    <li>import hcmastodonlib  # has functions to post to mastodon</li>
    <li>import tokenlib   #   has all tokens and so on</li>

<br/>
hcmastodonlib #has these functions:
<ul>
    <li># post to mastodon with 1 image uses: </li>
    <ul>
        <li>upload_image_to_mastodon(local_photo, foto_description, mastodon): #upload a single local photo</li>
        <li>tootwithphoto(local_photo, foto_description, post_text, mastodon):</li>
    </ul>
</ul>
 <br/> <br/>

#post to mastodon with multiple images
<ul>
    <li>CheckifImageExistsOnline(img_url): # checks if an online url exists # optionally use:</li>
    <li>tootwithmanyphoto(photo_dict, post_text, mastodon):  # post toot with multiple images</li>
</ul>
<br>

tootwithmanyphoto(photo_dict, post_text, mastodon):  # post toot with multiple images<br/>
    ## uses these other functions 
    <ul>
        <li>upload_image_url_to_mastodon(url, foto_description, mastodon):  #downloads image-url to local, uploads to masto. Uses functions below:</li>
        <li>download_photo2022(img_url, filename):  # downloads image-url to local disk, checks content-header image/jpeg
        make_sure_path_exists(path):  # see if a specific local directory exists. If not makes it</li>  
        </ul>

        <br/>
I am sure there are better coders out there, but this is functional code to work with. 


