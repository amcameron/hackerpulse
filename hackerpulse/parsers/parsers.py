""" A collection of parsers to grab items from web services. """

from datetime import datetime

class BaseFeedItem(object):
    """ Base class for each 'feed item' that we parse. """

    def __init__(self):
        self.timestamp = None
        self.title = None
        self.link = None

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
	def run(self):
		raise NotImplementedError
