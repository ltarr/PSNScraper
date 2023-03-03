# PSNScraper

[`psn_scraper.py`](psn_scraper.py) is where the scraping happens.

[`sale_md.py`](sale_md.py) makes Reddit comments.

[`psn_to_csv.py`](psn_to_csv.py) creates a CSV with the sale data. This is useful for uploading to something like Google Sheets.

[`psn_reddit_gui.py`](psn_reddit_gui.py) is a GUI interface to post comments on a
certain Reddit thread.

## How to Install

First of all, you'll want to grab the code.

`git clone https://github.com/ltarr/PSNScraper.git`

Next, navigate to the new folder and run the following:

`pip install -r requirements.txt`

I recommend you use a virtual environment (venv, conda) to do this. It helps keep things working properly, and doesn't pollute your base environment.

## Configuration

### Playstation SHA256

In order to use the internal Playstation Store API, you must acquire a SHA256 hash. This must be set as the environment variable `PSN_SHA_256`.

The easiest way to get this that I have found is to follow these steps. You only need to do this once, so don't fret.

First, go to any sale you wish on the Playstation Store. Open the DevTools in your browser (easy way to do this is Ctrl+Shift+I in Chrome).

Next, go to the 'Network' tab. In your browser, press the next page button or go to any page on the sale. 

In the Network tab, find the entry that starts with `op?operationName=categoryGridRetrieve`. Look at the payload under the 'Payload Header'. Decode this by pressing 'View Decoded'. In the `extensions` parameter, you will see the code under "sha256Hash".

I will hopefully be posting a video to make this easier.

### Posting to Reddit
In order to post to Reddit, you'll need to need to register a developed app.

If you're logged in, you can do that [here](https://old.reddit.com/prefs/apps/). This will give you a client ID, and a client secret.

There are two ways about getting the Reddit configuration to work.

#### Environment Variables

In this option, you can set environment variables to identify yourself to Reddit.

The following variables are needed:

+ `praw_client_id`: This is your client ID from your registered Reddit development app.
+ `praw_client_secret`: This os your client secret from your registered Reddit development app.
+ `praw_user_agent`: This should be something helpful to Reddit to identify you in logs. The one I use is **windows:PSN Sales Generator:v0.1 (by u/\<username here\>)**.
+ `praw_username`: Your Reddit username.
+ `praw_password`: Your Reddit password.

#### praw.ini

In my opinion, this is the easier answer. Create a file named `praw.ini` in the directory. It will contain some configuration options. I've added an example version called `example_praw.ini`. Remember that it will need to be named `praw.ini` to work.

## How the API Works

TBD