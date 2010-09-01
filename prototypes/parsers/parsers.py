""" A collection of parsers to grab items from web services. """

from datetime import datetime

class BaseFeedItem(object):
    """ Base class for each 'feed item' that we parse. """

    def __init__(self, timestamp=None, title=None, link=None):
        self.timestamp = timestamp
        self.title = title
        self.link = link

    def get_data(self):
        """ Return the timestamp, title, and link """
        return self.timestamp, self.title, self.link

class BaseParser(object):
	""" Base class for parsers. """

	def __init__(self, username):
		self.username = username

	def run(self):
		raise NotImplementedError
