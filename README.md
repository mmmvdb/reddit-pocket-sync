#Sync Reddit saved posts to text
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE) [![Python version](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)

This script keeps your reddit account saved submissions backed up to a text flat file. Reddit has a hard limit of [1000 posts](https://www.reddit.com/r/help/comments/24znn6/i_just_learned_that_reddit_limits_the_number_of/) which was the primary motivation behind making this script. 

##Requirements

Run the following in the terminal
```shell
$ pip install -r requirements.txt
```

##Setup
Before using this, you must create your own reddit app to obtain a public and a secret key. This can be done [here](https://ssl.reddit.com/prefs/apps).

Once you obtain your keys, create a new file in any text editor with the following content -
> [mysettings]
> client_id =YOUR_PUBLIC_APP_ID

> client_secret = YOUR_SECRET_APP_ID

> password = YOUR_PASSWORD

> username = YOUR_USERNAME

Save it as `praw.ini` .
Place it in your local working directory.

##Running the script
The first time run the script from the terminal and give your consumer key.
```shell
$ python redditFavoritesGrab.py 
```

Borrowed and modified from [Vihang Godbole](https://github.com/vihanggodbole) obtained here [reddit-pocket-sync](https://github.com/vihanggodbole/reddit-pocket-sync)
