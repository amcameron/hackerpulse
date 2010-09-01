""" A collection of parsers to grab items from web services. """

from datetime import datetime
import json
from urllib2 import urlopen

class BaseFeedItem(object):
    """ Base class for each 'feed item' that we parse. """

    def __init__(self, timestamp=None, title=None, link=None):
        self.timestamp = timestamp
        self.title = title
        self.link = link

    def get_data(self):
        """ Return the timestamp, title, and link """
        return self.timestamp, self.title, self.link

class RedditFeedItem(BaseFeedItem):
    def __init__(self):
		raise NotImplementedError

class TwitterFeedItem(BaseFeedItem):
    def __init__(self):
		raise NotImplementedError

class BaseParser(object):
	""" Base class for parsers. """

	def __init__(self, username):
		self.username = username

	def run(self):
		raise NotImplementedError

class RedditParser(BaseParser):
    def run(self):
		raise NotImplementedError

class GitHubParser(BaseParser):
	api_url = "http://github.com/api/v2/json/"
	def run(self):
		# From what I can tell, we can't find "recent activity"
		# for a GitHub user using the API (json or otherwise).
		# However, we can get it by scraping their syndication
		# feed at http://github.com/username.atom
		# In the meanwhile, some pretty (useless) json stuff.
		#TODO scrape a syndication feed.
		response = urlopen(''.join(api_url, 'user/show/',
			self.username)).read()
		user_info = json.loads(response)
		raise NotImplementedError
